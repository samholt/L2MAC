from flask import request, jsonify
from werkzeug.exceptions import BadRequest
from models import User, Post, Reply, db
import jwt
import datetime

from app import app

@app.route('/')
def home():
	return 'Welcome to the Home Page'

@app.route('/register', methods=['POST'])
def register():
	data = request.get_json()
	new_user = User(email=data['email'], username=data['username'])
	new_user.set_password(data['password'])
	db.session.add(new_user)
	db.session.commit()
	return jsonify({'message': 'registered successfully'}), 201

@app.route('/login', methods=['POST'])
def login():
	data = request.get_json()
	user = User.query.filter_by(username=data['username']).first()
	if not user or not user.check_password(data['password']):
		raise BadRequest('Invalid credentials')
	token = jwt.encode({'user_id': user.id, 'exp' : datetime.datetime.utcnow() + datetime.timedelta(minutes=30)}, app.config['SECRET_KEY'])
	return jsonify({'token' : token})

@app.route('/profile', methods=['GET', 'PUT'])
def profile():
	data = request.get_json()
	user = User.query.get(data['user_id'])
	if request.method == 'GET':
		if user.is_private:
			return jsonify({'message': 'This profile is private.'}), 403
		return jsonify({'username': user.username, 'email': user.email, 'profile_picture': user.profile_picture, 'bio': user.bio, 'website_link': user.website_link, 'location': user.location}), 200
	elif request.method == 'PUT':
		user.profile_picture = data.get('profile_picture', user.profile_picture)
		user.bio = data.get('bio', user.bio)
		user.website_link = data.get('website_link', user.website_link)
		user.location = data.get('location', user.location)
		user.is_private = data.get('is_private', user.is_private)
		db.session.commit()
		return jsonify({'message': 'Profile updated successfully'}), 200

@app.route('/post', methods=['POST'])
def create_post():
	data = request.get_json()
	new_post = Post(content=data['content'], images=data.get('images'), user_id=data['user_id'])
	db.session.add(new_post)
	db.session.commit()
	return jsonify({'message': 'Post created successfully'}), 201

@app.route('/post/<int:post_id>', methods=['GET', 'DELETE'])
def manage_post(post_id):
	post = Post.query.get(post_id)
	if request.method == 'GET':
		return jsonify({'content': post.content, 'images': post.images, 'user_id': post.user_id, 'likes': post.likes, 'retweets': post.retweets, 'replies': [reply.content for reply in post.replies]}), 200
	elif request.method == 'DELETE':
		db.session.delete(post)
		db.session.commit()
		return jsonify({'message': 'Post deleted successfully'}), 200

@app.route('/post/<int:post_id>/like', methods=['POST'])
def like_post(post_id):
	post = Post.query.get(post_id)
	post.likes += 1
	db.session.commit()
	return jsonify({'message': 'Post liked successfully'}), 200

@app.route('/post/<int:post_id>/retweet', methods=['POST'])
def retweet_post(post_id):
	post = Post.query.get(post_id)
	post.retweets += 1
	db.session.commit()
	return jsonify({'message': 'Post retweeted successfully'}), 200

@app.route('/post/<int:post_id>/reply', methods=['POST'])
def reply_post(post_id):
	data = request.get_json()
	new_reply = Reply(content=data['content'], user_id=data['user_id'], post_id=post_id)
	db.session.add(new_reply)
	db.session.commit()
	return jsonify({'message': 'Reply posted successfully'}), 201

@app.route('/follow', methods=['POST'])
def follow():
	data = request.get_json()
	user = User.query.get(data['user_id'])
	user_to_follow = User.query.get(data['user_to_follow_id'])
	user.follow(user_to_follow)
	db.session.commit()
	return jsonify({'message': 'Followed user successfully'}), 200

@app.route('/unfollow', methods=['POST'])
def unfollow():
	data = request.get_json()
	user = User.query.get(data['user_id'])
	user_to_unfollow = User.query.get(data['user_to_unfollow_id'])
	user.unfollow(user_to_unfollow)
	db.session.commit()
	return jsonify({'message': 'Unfollowed user successfully'}), 200

@app.route('/search', methods=['GET'])
def search():
	keyword = request.args.get('keyword')
	users = User.search(keyword)
	posts = Post.search(keyword)
	return jsonify({'users': [user.username for user in users], 'posts': [post.content for post in posts]}), 200

@app.route('/filter', methods=['GET'])
def filter():
	filter_type = request.args.get('filter_type')
	keyword = request.args.get('keyword')
	posts = Post.filter(filter_type, keyword)
	return jsonify({'posts': [post.content for post in posts]}), 200
