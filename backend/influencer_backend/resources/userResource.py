from flask import abort
from flask_restful import Resource, marshal_with, reqparse, fields
from sqlalchemy.exc import IntegrityError
from influencer_backend.main.routes import token_required
from influencer_backend.extensions import db
from influencer_backend.models.users import Users

parser= reqparse.RequestParser()
parser.add_argument("name",type=str)
parser.add_argument("email", type=str, required=True)
parser.add_argument("password",type=str,required=True)
parser.add_argument("userType",type=str,required=True)
parser.add_argument("flag",type=bool,required=True)
parser.add_argument("status",type=str,required=True)

user_fields= {
    "id": fields.Integer,
    "name": fields.String,
    "email": fields.String,
    "userType": fields.String,
    "password": fields.String,
    "flag": fields.Boolean,
    "status": fields.String
}

class UserResource(Resource):
    @token_required
    @marshal_with(user_fields)
    def get(self, user_id=None):
        if user_id:
            user=Users.query.filter_by(id=user_id).first()
            if not user:
                abort(404,"user doesn't exit")
            else:
                return user, 200
        else:
            users=Users.query.all()
            return users, 200
    
    @marshal_with(user_fields)
    def put(self, user_id=None):
        if not user_id:
            abort(404, "invalid id")
        else:
            user=Users.query.filter_by(id=user_id).first()
            if not user:
                abort(404,"user doesn't exist")
            args=parser.parse_args()
            user=Users.query.filter_by(id=user_id).first()
            for arg in args:
                if args[arg] is not None:
                    setattr(user, arg, args[arg])
            db.session.commit()
            return user, 200
        
    @marshal_with(user_fields)
    def post(self):
        args = parser.parse_args()
        user = Users(**args)
        try:
            db.session.add(user)
            db.session.commit()
        except IntegrityError as e:
            db.session.rollback()
            abort(409, "User already exists")
        return user, 201

    @marshal_with(user_fields)
    def delete(self, user_id):
        if not user_id:
            abort(404, {"error": "Invalid user_id {}.".format(user_id)})
        else:
            user = Users.query.filter_by(id=user_id).first()
            if not user:
                abort(404,"user doesn't not exist")
            db.session.delete(user)
            db.session.commit()
            return user, 200    