from flask import request, jsonify
from app import app, db
from models import User
from flask_jwt_extended import jwt_required, get_jwt_identity


@app.route('/register', methods=['POST'])
def register():
	data = request.get_json()
	new_user = User(username=data['username'], email=data['email'], password=data['password'])
	db.session.add(new_user)
	db.session.commit()
	return jsonify({'message': 'User registered successfully'}), 201


@app.route('/login', methods=['POST'])
def login():
	data = request.get_json()
	user = User.query.filter_by(username=data['username']).first()
	if not user or not user.check_password(data['password']):
		return jsonify({'message': 'Invalid username or password'}), 401
	return jsonify({'token': user.get_token()}), 200
