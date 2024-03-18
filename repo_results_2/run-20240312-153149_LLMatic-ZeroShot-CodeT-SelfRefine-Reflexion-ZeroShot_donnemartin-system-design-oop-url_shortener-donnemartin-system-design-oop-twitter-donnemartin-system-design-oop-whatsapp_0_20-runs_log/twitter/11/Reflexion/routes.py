from flask import request, jsonify
from flask_jwt_extended import create_access_token
from app import app, db
from models import User, Post, Comment

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

@app.route('/post', methods=['POST'])
def post():
	user_id = request.json.get('user_id', None)
	content = request.json.get('content', None)
	post = Post(user_id=user_id, content=content)
	db.session.add(post)
	db.session.commit()
	return jsonify({'message': 'Post created successfully'}), 201

@app.route('/comment', methods=['POST'])
def comment():
	post_id = request.json.get('post_id', None)
	user_id = request.json.get('user_id', None)
	content = request.json.get('content', None)
	comment = Comment(post_id=post_id, user_id=user_id, content=content)
	db.session.add(comment)
	db.session.commit()
	return jsonify({'message': 'Comment added successfully'}), 201
