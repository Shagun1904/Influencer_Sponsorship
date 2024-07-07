from flask_login import UserMixin
from sqlalchemy import Column, ForeignKey, Integer, String

from influencer_backend.extensions import db

class Influencers(db.Model,UserMixin):
    __tablename__="influencers"
    id=Column(Integer, primary_key=True, autoincrement=True)
    category=Column(String(64), index=True)
    niche=Column(String(100), nullable=False)
    reach=Column(Integer, nullable=False)
    user_id=Column(Integer, ForeignKey('users.id'), nullable=False)