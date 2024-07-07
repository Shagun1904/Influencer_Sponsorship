from influencer_backend import app
from influencer_backend.extensions import db

#main method
if __name__=='__main__':
    app2=app()
    db.create_all()
    app2.run(debug=True)