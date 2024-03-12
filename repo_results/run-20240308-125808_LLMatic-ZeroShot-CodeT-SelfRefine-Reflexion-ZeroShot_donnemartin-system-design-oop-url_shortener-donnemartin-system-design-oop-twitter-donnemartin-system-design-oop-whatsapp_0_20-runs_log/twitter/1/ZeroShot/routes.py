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
	if not user or not user.check_password(data['password']):
		return jsonify({'message': 'Invalid username or password'}), 401
	token = user.get_token()
	return jsonify({'access_token': token}), 200


@app.route('/post', methods=['POST'])
@jwt_required

def post():
	data = request.get_json()
	user_id = get_jwt_identity()
	new_post = Post(content=data['content'], user_id=user_id)
	db.session.add(new_post)
	db.session.commit()
	return jsonify({'message': 'Post created successfully'}), 201
