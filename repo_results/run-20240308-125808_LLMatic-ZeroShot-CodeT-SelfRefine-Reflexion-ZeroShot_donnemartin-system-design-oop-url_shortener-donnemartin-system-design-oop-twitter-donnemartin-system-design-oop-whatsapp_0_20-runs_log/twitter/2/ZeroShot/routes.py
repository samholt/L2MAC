from flask import request
from app import app, db, jwt
from models import User
from flask_jwt_extended import create_access_token

@app.route('/register', methods=['POST'])
def register():
	username = request.json.get('username', None)
	email = request.json.get('email', None)
	password = request.json.get('password', None)
	user = User(username=username, email=email, password=password)
	db.session.add(user)
	db.session.commit()
	return {'message': 'User created successfully'}, 201

@app.route('/login', methods=['POST'])
def login():
	username = request.json.get('username', None)
	password = request.json.get('password', None)
	user = User.query.filter_by(username=username, password=password).first()
	if user is None:
		return {'message': 'Invalid username or password'}, 401
	access_token = create_access_token(identity=username)
	return {'access_token': access_token}, 200
