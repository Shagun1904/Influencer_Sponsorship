from flask_login import UserMixin
from sqlalchemy import Column, Integer, String, Boolean

from influencer_backend.extensions import db

class Users(db.Model,UserMixin):
    __tablename__="users"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(64), nullable=False)
    email = Column(String(100), nullable=False)
    userType = Column(String(50), nullable=False)
    password = Column(String(500), nullable=False)
    flag = Column(Boolean, nullable=False)
    sponsors = db.relationship('Sponsors', backref='users', lazy=True)
    influencers = db.relationship('Influencers', backref='users', lazy=True)
