import os
from flask import abort, request
from flask_restful import Resource, marshal_with, reqparse, fields
from sqlalchemy.exc import IntegrityError
from influencer_backend.extensions import db
from influencer_backend.models.adRequest import AdRequest
from influencer_backend import app
from werkzeug.utils import secure_filename

parser= reqparse.RequestParser()
parser.add_argument("message",type=str,required=True)
parser.add_argument("requirement", type=str, required=True)
parser.add_argument("paymentAmount",type=int,required=True)
parser.add_argument("status",type=str,required=True)
parser.add_argument("sendBy",type=str)
parser.add_argument("campaign_id",type=int,required=True)
parser.add_argument("influencer_id",type=int)
parser.add_argument("sponsor_id",type=int)

adRequest_fields= {
    "id": fields.Integer,
    "message": fields.String,
    "requirement": fields.String,
    "paymentAmount": fields.Integer,
    "status": fields.String,
    "sendBy": fields.String,
    "campaign_id": fields.Integer,
    "influencer_id": fields.Integer,
    "sponsor_id": fields.Integer
}

class AdRequestResource(Resource):
    @marshal_with(adRequest_fields)
    def get(self, adRequest_id=None):
        if adRequest_id:
            adRequest=AdRequest.query.filter_by(id=adRequest_id).first()
            if not adRequest:
                abort(404,"Request doesn't exit")
            else:
                return adRequest, 200
        else:
            adRequest= AdRequest.query.all()
            return adRequest, 200
    
    @marshal_with(adRequest_fields)
    def put(self, adRequest_id=None):
        if not adRequest_id:
            abort(404, "invalid id")
        else:
            adRequest=AdRequest.query.filter_by(id=adRequest_id).first()
            if not adRequest:
                abort(404,"Request doesn't not exist")
            args=parser.parse_args()
            adRequest=AdRequest.query.filter_by(id=adRequest_id).first()
            for arg in args:
                if args[arg] is not None:
                    setattr(adRequest, arg, args[arg])
            db.session.commit()
            return adRequest, 200
        
    @marshal_with(adRequest_fields)
    def post(self):
        data = parser.parse_args()
        adRequest = AdRequest(**data)
        try:
            db.session.add(adRequest)
            db.session.commit()
        except IntegrityError as e:
            db.session.rollback()
            abort(409, "Request already exists")
        return adRequest, 201

    @marshal_with(adRequest_fields)
    def delete(self, adRequest_id):
        if not adRequest_id:
            abort(404, {"error": "Invalid user_id {}.".format(adRequest_id)})
        else:
            adRequest = AdRequest.query.filter_by(id=adRequest_id).first()
            if not adRequest:
                abort(404,"Request doesn't not exist")
            db.session.delete(adRequest)
            db.session.commit()
            return adRequest, 200    