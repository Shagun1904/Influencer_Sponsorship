from flask import Blueprint

login_bp = Blueprint('main', __name__)

from influencer_backend.main import routes