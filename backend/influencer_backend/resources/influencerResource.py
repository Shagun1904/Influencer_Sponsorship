import os
from flask import abort, request
from flask_restful import Resource, marshal_with, reqparse, fields
from sqlalchemy.exc import IntegrityError
from influencer_backend.extensions import db
from influencer_backend.models.influencers import Influencers
from influencer_backend import app
from werkzeug.utils import secure_filename

Parent_path="../../static/profiles/influencerPhotos"

parser= reqparse.RequestParser()
parser.add_argument("category",type=str,required=True)
parser.add_argument("niche", type=str, required=True)
parser.add_argument("reach",type=int,required=True)
parser.add_argument("furl",type=str,required=True)
parser.add_argument("iurl",type=str,required=True)
parser.add_argument("lurl",type=str,required=True)
parser.add_argument("user_id",type=int,required=True)

influencer_fields= {
    "id": fields.Integer,
    "category": fields.String,
    "niche": fields.String,
    "reach": fields.Integer,
    "furl": fields.String,
    "iurl": fields.String,
    "lurl": fields.String,
    "user_id": fields.Integer,
}

class InfluencerResource(Resource):
    @marshal_with(influencer_fields)
    def get(self, influencer_id=None):
        if influencer_id:
            influencer=Influencers.query.filter_by(id=influencer_id).first()
            if not influencer:
                abort(404,"user doesn't exit")
            else:
                return influencer, 200
        else:
            influencer= Influencers.query.all()
            return influencer, 200
    
    @marshal_with(influencer_fields)
    def put(self, influencer_id=None):
        if not influencer_id:
            abort(404, "invalid id")
        else:
            influencer=Influencers.query.filter_by(id=influencer_id).first()
            if not influencer:
                abort(404,"user doesn't not exist")
            args=parser.parse_args()
            influencer=Influencers.query.filter_by(id=influencer_id).first()
            for arg in args:
                if args[arg] is not None:
                    setattr(influencer, arg, args[arg])
            db.session.commit()
            return influencer, 200
        
    @marshal_with(influencer_fields)
    def post(self):
        data = parser.parse_args()
        influencer = Influencers(**data)
        try:
            db.session.add(influencer)
            db.session.commit()
        except IntegrityError as e:
            db.session.rollback()
            abort(409, "User already exists")
        return influencer, 201

    @marshal_with(influencer_fields)
    def delete(self, influencer_id):
        if not influencer_id:
            abort(404, {"error": "Invalid user_id {}.".format(influencer_id)})
        else:
            influencer = Influencers.query.filter_by(id=influencer_id).first()
            if not influencer:
                abort(404,"user doesn't not exist")
            db.session.delete(influencer)
            db.session.commit()
            return influencer, 200    