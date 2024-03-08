from flask import request, jsonify
from flask_jwt_extended import create_access_token, jwt_required
from app import app, db
from models import User

@app.route('/register', methods=['POST'])
def register():
	username = request.json.get('username', None)
	email = request.json.get('email', None)
	password = request.json.get('password', None)
	user = User(username=username, email=email, password=password)
	db.session.add(user)
	db.session.commit()
	return jsonify({'message': 'User registered successfully'}), 201

@app.route('/login', methods=['POST'])
def login():
	username = request.json.get('username', None)
	password = request.json.get('password', None)
	user = User.query.filter_by(username=username, password=password).first()
	if user is None:
		return jsonify({'message': 'Invalid username or password'}), 401
	access_token = create_access_token(identity=username)
	return jsonify(access_token=access_token), 200
