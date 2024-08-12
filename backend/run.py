from tasks import daily_run
from influencer_backend import app
from influencer_backend.extensions import db

def add_admin():
    from influencer_backend.models.users import Users
    data = Users.query.all()
    if not data:
        admin = Users(name="admin", email="admin@gmail.com", userType="admin", password="admin", flag=False, status="approved")
        db.session.add(admin)
        db.session.commit()

#main method
if __name__=='__main__':
    app2=app()
    db.create_all()
    add_admin()
    daily_run()
    app2.run(debug=True)