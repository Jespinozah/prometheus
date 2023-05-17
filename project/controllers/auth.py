# blueprints/basic_endpoints/__init__.py
from flask import Blueprint, request, make_response, jsonify
from datetime import datetime, timedelta
from jwt.exceptions import ExpiredSignatureError
from project.dao.userDao import UserDao
from project.models.user import User
from project.models.userData import UserData


import jwt

bpAuth = Blueprint('user', __name__, url_prefix='/auth')


@bpAuth.route('/login', methods=['POST'])
def login():
    auth = request.json
    if not auth or not auth.get('password') or not auth.get('username'):
        return make_response({"message": "User or password missing"}, 400)
    
    user_data: User= UserDao.get_user_by_username(username = auth.get('username'))
    user_dict: dict = UserData(user_data).__dict__
    if user_dict.get("password") ==auth.get('password'):
        token = jwt.encode({
            'public_id': '1',
            'exp': datetime.utcnow() + timedelta(minutes=5),
        }, 'ENTROPY', "HS256")
        return make_response({'username': auth.get('username'), 'token': token }, 200)        
    return make_response({"message": "Usuario or password are invalid"}, 401)


@bpAuth.route('/validate', methods=['POST'])
def validateToken():
    try:
        auth = request.json
        payload = jwt.decode(auth.get('token'),'ENTROPY',"HS256")
    except ExpiredSignatureError:
        return  make_response( {"message": "Token expirado"}, 200)
    except Exception:
        return  make_response( {"message": "error"}, 200)
    return  make_response( {"message": "Token valido"}, 200)