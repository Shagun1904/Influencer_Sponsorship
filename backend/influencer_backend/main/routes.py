from datetime import datetime, timedelta
from functools import wraps
from flask import jsonify, make_response, request
from influencer_backend.models.users import Users
from config import LocalConfig
from influencer_backend.main import login_bp
from jwt import encode, decode

#JWT Token
def token_required(f):
    @wraps(f)
    def decorator(*args, **kwargs):
        token=None

        if "Authorization" in request.headers:
            token= request.headers["Authorization"].split(" ")[1]

        response= {"message": {"error": ""}}

        if not token:
            response["message"]["error"]="JWT Token Missing!!"
            return make_response(response, 401)
        
        jwt_data=None
        try:
            jwt_data=decode(
                token,
                LocalConfig.JWT_SECRET_KEY,
                algorithms=["HS256"]
            )
            user=Users.query.filter_by(name=jwt_data["name"]).first()
            if not user:
                response["message"]["error"] = f"User {jwt_data['name']} doesn't exist"
                return make_response(response, 404)
            
            token_exp = datetime.utcfromtimestamp(jwt_data["exp"])
            current_time = datetime.utcnow()
            if token_exp < current_time:
                response["message"]["error"] = "Token expired"
                return make_response(response, 401)
            
        except Exception as e:
            return{
                "message": "Something went wrong",
                "data": None,
                "error": str(e)
            }, 500
        
        return f(*args, **kwargs)
    
    return decorator

@login_bp.route("/login", methods=["POST"])
def login():
    try:
        data = request.json
        print(data)
        if not data:
            return jsonify( 
                {
                "message": "Please enter all details",
                "data": None,
                "error": "Bad request"
            }), 400
        
        user = Users.query.filter_by(email=data["email"]).first()
        if not user:
            return jsonify({
                "message": "User does't exist. Please sign up to continue",
                "data": data["email"],
                "error": "Not found"
            }), 404
        
        if not user.password==data["password"]:
            return jsonify({
                "message": "Wrong credentials",
                "data": data["email"],
                "error": "Unauthorized"
            }), 401
        print(user)
        jwt = encode(
            {
                "name": user.name,
                "userType": user.userType,
                "user_id": user.id,
                "exp": datetime.utcnow() + timedelta(minutes=120),
            },
            LocalConfig.JWT_SECRET_KEY,
            algorithm="HS256",
        )
        return (
            jsonify(
            {
                "status": "ok",
                "jwt": jwt,
                "name": user.name,
                "userType": user.userType,
                "user_id": user.id,
                "exp": (datetime.utcnow() + timedelta(minutes=120)).strftime('%Y-%m-%d %H:%M:%S'),
            }
        ), 
        200,
        )
    
    except Exception as e:
        return jsonify({
            "message": "Something went wrong",
            "data": None,
            "error": str(e)
        }), 500