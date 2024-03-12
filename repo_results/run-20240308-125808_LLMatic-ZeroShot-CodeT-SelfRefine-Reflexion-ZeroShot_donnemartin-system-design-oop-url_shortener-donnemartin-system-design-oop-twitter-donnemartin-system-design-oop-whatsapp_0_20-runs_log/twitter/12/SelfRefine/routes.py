from flask import request
from app import app, db, jwt
from models import User
from flask_jwt_extended import create_access_token
from werkzeug.security import check_password_hash

@app.route('/register', methods=['POST'])
def register():
	if not request.is_json:
		return {'msg': 'Missing JSON in request'}, 400
	username = request.json.get('username', None)
	email = request.json.get('email', None)
	password = request.json.get('password', None)
	if not username:
		return {'msg': 'Missing username parameter'}, 400
	if not email:
		return {'msg': 'Missing email parameter'}, 400
	if not password:
		return {'msg': 'Missing password parameter'}, 400
	if User.query.filter_by(username=username).first() is not None:
		return {'msg': 'Username already exists'}, 400
	if User.query.filter_by(email=email).first() is not None:
		return {'msg': 'Email already exists'}, 400
	user = User(username=username, email=email, password=password)
	db.session.add(user)
	db.session.commit()
	return {'msg': 'User created successfully'}, 201

@app.route('/login', methods=['POST'])
def login():
	if not request.is_json:
		return {'msg': 'Missing JSON in request'}, 400
	username = request.json.get('username', None)
	password = request.json.get('password', None)
	if not username:
		return {'msg': 'Missing username parameter'}, 400
	if not password:
		return {'msg': 'Missing password parameter'}, 400
	user = User.query.filter_by(username=username).first()
	if user and check_password_hash(user.password, password):
		access_token = create_access_token(identity=username)
		return {'access_token': access_token}, 200
	else:
		return {'msg': 'Invalid credentials'}, 401
