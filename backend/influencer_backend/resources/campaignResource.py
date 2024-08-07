import os
from flask import abort, request
from flask_restful import Resource, marshal_with, reqparse, fields
from sqlalchemy.exc import IntegrityError
from influencer_backend.extensions import db
from influencer_backend.models.campaign import Campaign
from influencer_backend import app
from werkzeug.utils import secure_filename


parser= reqparse.RequestParser()
parser.add_argument("name",type=str,required=True)
parser.add_argument("description", type=str, required=True)
parser.add_argument("startDate",type=str,required=True)
parser.add_argument("endDate",type=str,required=True)
parser.add_argument("campaignBudget",type=int,required=True)
parser.add_argument("visibility",type=str,required=True)
parser.add_argument("goal",type=str,required=True)
parser.add_argument("sponsor_id",type=int,required=True)

campaign_fields= {
    "id": fields.Integer,
    "name": fields.String,
    "description": fields.String,
    "startDate": fields.String,
    "endDate": fields.String,
    "campaignBudget": fields.Integer,
    "visibility": fields.String,
    "goal": fields.String,
    "sponsor_id": fields.Integer,
}

class CampaignResource(Resource):
    @marshal_with(campaign_fields)
    def get(self, campaign_id=None):
        if campaign_id:
            campaign=Campaign.query.filter_by(id=campaign_id).first()
            if not campaign:
                abort(404,"campaign doesn't exit")
            else:
                return campaign, 200
        else:
            campaign= Campaign.query.all()
            return campaign, 200
    
    @marshal_with(campaign_fields)
    def put(self, campaign_id=None):
        if not campaign_id:
            abort(404, "invalid id")
        else:
            campaign=Campaign.query.filter_by(id=campaign_id).first()
            if not campaign:
                abort(404,"Campaign doesn't not exist")
            args=parser.parse_args()
            campaign=Campaign.query.filter_by(id=campaign_id).first()
            for arg in args:
                if args[arg] is not None:
                    setattr(campaign, arg, args[arg])
            db.session.commit()
            return campaign, 200
        
    @marshal_with(campaign_fields)
    def post(self):
        data = parser.parse_args()
        campaign = Campaign(**data)
        try:
            db.session.add(campaign)
            db.session.commit()
        except IntegrityError as e:
            db.session.rollback()
            abort(409, "Campaign already exists")
        return campaign, 201

    @marshal_with(campaign_fields)
    def delete(self, campaign_id):
        if not campaign_id:
            abort(404, {"error": "Invalid user_id {}.".format(campaign_id)})
        else:
            campaign = Campaign.query.filter_by(id=campaign_id).first()
            if not campaign:
                abort(404,"Campaign doesn't not exist")
            db.session.delete(campaign)
            db.session.commit()
            return campaign, 200    