from flask import request, jsonify
from app import app, db, logger
from models import User, Post
from flask_jwt_extended import jwt_required, get_jwt_identity


@app.route('/register', methods=['POST'])
def register():
	data = request.get_json()
	if 'username' not in data or 'email' not in data or 'password' not in data:
		return jsonify({'message': 'Missing required fields'}), 400
	try:
		new_user = User(username=data['username'], email=data['email'], password=data['password'])
		db.session.add(new_user)
		db.session.commit()
	except Exception as e:
		logger.error(f'An error occurred while registering the user: {str(e)}')
		return jsonify({'message': 'An error occurred. Please try again later.'}), 500
	return jsonify({'message': 'User registered successfully'}), 201


@app.route('/login', methods=['POST'])
def login():
	data = request.get_json()
	if 'username' not in data or 'password' not in data:
		return jsonify({'message': 'Missing required fields'}), 400
	user = User.query.filter_by(username=data['username']).first()
	if user and user.check_password(data['password']):
		return jsonify({'access_token': user.get_token()}), 200
	return jsonify({'message': 'Invalid credentials'}), 401


@app.route('/post', methods=['POST'])
@jwt_required

def create_post():
	data = request.get_json()
	if 'content' not in data:
		return jsonify({'message': 'Missing required fields'}), 400
	try:
		new_post = Post(content=data['content'], user_id=get_jwt_identity())
		db.session.add(new_post)
		db.session.commit()
	except Exception as e:
		logger.error(f'An error occurred while creating the post: {str(e)}')
		return jsonify({'message': 'An error occurred. Please try again later.'}), 500
	return jsonify({'message': 'Post created successfully'}), 201
