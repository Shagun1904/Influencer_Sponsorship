from flask_login import UserMixin
from sqlalchemy import Column, ForeignKey, Integer, String

from influencer_backend.extensions import db

class Campaign(db.Model,UserMixin):
    __tablename__ = "campaign"
    id=Column(Integer, primary_key=True, autoincrement=True)
    name=Column(String(64), index=True)
    description=Column(String(100), nullable=False)
    startDate= Column(String(10), nullable=False)
    endDate= Column(String(10), nullable=False)
    campaignBudget=Column(Integer, nullable=False)
    visibility=Column(String(10), nullable=False)
    goal=Column(String(100), nullable=False)
    sponsor_id=Column(Integer, ForeignKey('sponsors.id'), nullable=False)
