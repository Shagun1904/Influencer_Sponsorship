from flask import abort
from flask_restful import Resource, marshal_with, reqparse, fields
from sqlalchemy.exc import IntegrityError
from influencer_backend.extensions import db
from influencer_backend.models.sponsors import Sponsors

parser= reqparse.RequestParser()
parser.add_argument("companyName",type=str,required=True)
parser.add_argument("industry", type=str, required=True)
parser.add_argument("budget",type=int,required=True)
parser.add_argument("user_id",type=int,required=True)

sponsor_fields= {
    "id": fields.Integer,
    "companyName": fields.String,
    "industry": fields.String,
    "budget": fields.Integer,
    "user_id": fields.Integer,
}

class SponsorResource(Resource):
    @marshal_with(sponsor_fields)
    def get(self, sponsor_id=None):
        if sponsor_id:
            sponsor=Sponsors.query.filter_by(id=sponsor_id).first()
            if not sponsor:
                abort(404,"user doesn't exit")
            else:
                return sponsor, 200
        else:
            sponsor= Sponsors.query.all()
            return sponsor, 200
    
    @marshal_with(sponsor_fields)
    def put(self, sponsor_id=None):
        if not sponsor_id:
            abort(404, "invalid id")
        else:
            sponsor=Sponsors.query.filter_by(id=sponsor_id).first()
            if not sponsor:
                abort(404,"user doesn't not exist")
            args=parser.parse_args()
            sponsor=Sponsors.query.filter_by(id=sponsor_id).first()
            for arg in args:
                if args[arg] is not None:
                    setattr(sponsor, arg, args[arg])
            db.session.commit()
            return sponsor, 200
        
    @marshal_with(sponsor_fields)
    def post(self):
        args = parser.parse_args()
        sponsor = Sponsors(**args)
        try:
            db.session.add(sponsor)
            db.session.commit()
        except IntegrityError as e:
            db.session.rollback()
            abort(409, "User already exists")
        return sponsor, 201

    @marshal_with(sponsor_fields)
    def delete(self, sponsor_id):
        if not sponsor_id:
            abort(404, {"error": "Invalid user_id {}.".format(sponsor_id)})
        else:
            sponsor = Sponsors.query.filter_by(id=sponsor_id).first()
            if not sponsor:
                abort(404,"user doesn't not exist")
            db.session.delete(sponsor)
            db.session.commit()
            return sponsor, 200    