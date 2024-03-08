from flask import Blueprint, request
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import create_access_token
from models import User, users_db

views = Blueprint('views', __name__)

@views.route('/register', methods=['POST'])
def register():
	data = request.get_json()
	hashed_password = generate_password_hash(data['password'], method='sha256')
	new_user = User(data['email'], data['username'], hashed_password)
	users_db[data['email']] = new_user
	return {'message': 'User created'}, 201

@views.route('/login', methods=['POST'])
def login():
	data = request.get_json()
	user_in_db = users_db.get(data['email'])
	if not user_in_db or not check_password_hash(user_in_db.password, data['password']):
		return {'message': 'Invalid credentials'}, 401
	token = create_access_token(identity=data['email'])
	return {'access_token': token}, 200
