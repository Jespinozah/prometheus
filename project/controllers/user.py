# blueprints/basic_endpoints/__init__.py
from flask import Blueprint, request, make_response, jsonify
from datetime import datetime, timedelta
from jwt.exceptions import ExpiredSignatureError
from project.dao.userDao import UserDao
from project.models.user import User
from project.models.userData import UserData
from flasgger import swag_from



import jwt

bpUser = Blueprint('users', __name__, url_prefix='/users')

@bpUser.route('/', methods=['GET'])
def get_user():
    
    all_users: list = UserDao.get_users()
    user_dicts = []
    for user_data in all_users:
        user_dict = UserData(user_data).__dict__
        user_dicts.append(user_dict)

    return make_response({'users': user_dicts }, 200)        

