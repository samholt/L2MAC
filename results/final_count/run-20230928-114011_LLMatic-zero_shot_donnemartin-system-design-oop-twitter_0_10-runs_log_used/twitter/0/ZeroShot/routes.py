from flask import request, jsonify
from app import app, db
from models import User, Post
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
	if user and user.check_password(data['password']):
		return jsonify({'token': user.get_token()}), 200
	return jsonify({'message': 'Invalid username or password'}), 401


@app.route('/post', methods=['POST'])
@jwt_required

def create_post():
	data = request.get_json()
	new_post = Post(content=data['content'], user_id=get_jwt_identity())
	db.session.add(new_post)
	db.session.commit()
	return jsonify({'message': 'Post created successfully'}), 201
