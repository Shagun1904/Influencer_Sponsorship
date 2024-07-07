from flask_login import UserMixin
from sqlalchemy import Column, Integer, String

from influencer_backend.extensions import db

class Users(db.Model,UserMixin):
    __tablename__="users"
    id=Column(Integer, primary_key=True, autoincrement=True)
    name=Column(String(64), index=True, unique=True)
    email=Column(String(100), nullable=False)
    userType=Column(String(50), nullable=False)
    password=Column(String(500), nullable=False)
    sponsors = db.relationship('Sponsors', backref='user', lazy=True)
    influencers = db.relationship('Influencers', backref='user', lazy=True)