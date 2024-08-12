from flask import Flask
from flask_cors import CORS
from config import LocalConfig

#creating flask app instance
def app(config_class=LocalConfig):
    app=Flask(__name__)
    app.config.from_object(config_class)
    app.app_context().push()

    from influencer_backend.extensions import db, api
    db.init_app(app)

    CORS(
        app,
        origins="http://localhost:8081"
    )

    from tasks import celery_app
    celery_app.conf.update(app.config)

    #Register Blueprints Here
    from influencer_backend.main import login_bp as lbp
    app.register_blueprint(lbp)

    #Register Resources Here
    from influencer_backend.resources.userResource import UserResource
    from influencer_backend.resources.influencerResource import InfluencerResource
    from influencer_backend.resources.sponsorsResource import SponsorResource
    from influencer_backend.resources.campaignResource import CampaignResource
    from influencer_backend.resources.adRequestResource import AdRequestResource

    api.add_resource(UserResource, "/user", "/user/<int:user_id>")
    api.add_resource(InfluencerResource, "/influencer", "/influencer/<int:influencer_id>")
    api.add_resource(SponsorResource, "/sponsor", "/sponsor/<int:sponsor_id>")
    api.add_resource(CampaignResource, "/campaign", "/campaign/<int:campaign_id>")
    api.add_resource(AdRequestResource, "/adRequest", "/adRequest/<int:adRequest_id>")

    api.init_app(app)

    @app.route('/demo')
    def demopage():
        return '<h1> welcome </h1>'
    
    @app.route("/add/<int:x>/<int:y>")
    def add(x, y):
        from backend.tasks import add
        result =add.delay(x, y)
        return {"task_id": result.id}

    return app