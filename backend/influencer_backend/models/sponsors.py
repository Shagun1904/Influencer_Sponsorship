from flask_login import UserMixin
from sqlalchemy import Column, ForeignKey, Integer, String

from influencer_backend.extensions import db

class Sponsors(db.Model,UserMixin):
    __tablename__="sponsors"
    id=Column(Integer, primary_key=True, autoincrement=True)
    companyName=Column(String(64), index=True, unique=True)
    industry=Column(String(100), nullable=False)
    budget=Column(String(50), nullable=False)
    user_id=Column(Integer, ForeignKey('users.id'), nullable=False)
