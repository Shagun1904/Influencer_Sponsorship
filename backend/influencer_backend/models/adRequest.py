from flask_login import UserMixin
from sqlalchemy import Column, ForeignKey, Integer, String

from influencer_backend.extensions import db

class AdRequest(db.Model,UserMixin):
    __tablename__ = "adRequest"
    id=Column(Integer, primary_key=True, autoincrement=True)
    message=Column(String(200), index=True, nullable=False)
    requirement=Column(String(100), nullable=False)
    paymentAmount=Column(Integer, nullable=False)
    status=Column(String(10))
    sendBy=Column(String(10))
    campaign_id=Column(Integer, ForeignKey('campaign.id'), nullable=False)
    influencer_id=Column(Integer, ForeignKey('influencers.id'))
