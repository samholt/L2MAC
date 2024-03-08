from flask import request, jsonify
from app import app, db, jwt
from app.models import User, Post
from flask_jwt_extended import create_access_token

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
	if user and user.password == data['password']:
		access_token = create_access_token(identity=user.username)
		return jsonify(access_token=access_token), 200
	return jsonify({'message': 'Invalid credentials'}), 401

@app.route('/post', methods=['POST'])
def post():
	data = request.get_json()
	new_post = Post(body=data['body'], user_id=data['user_id'])
	db.session.add(new_post)
	db.session.commit()
	return jsonify({'message': 'Post created successfully'}), 201

@app.route('/posts', methods=['GET'])
def get_posts():
	posts = Post.query.all()
	return jsonify(posts), 200

@app.route('/post/<int:id>', methods=['DELETE'])
def delete_post(id):
	post = Post.query.get(id)
	if post:
		db.session.delete(post)
		db.session.commit()
		return jsonify({'message': 'Post deleted successfully'}), 200
	return jsonify({'message': 'Post not found'}), 404
