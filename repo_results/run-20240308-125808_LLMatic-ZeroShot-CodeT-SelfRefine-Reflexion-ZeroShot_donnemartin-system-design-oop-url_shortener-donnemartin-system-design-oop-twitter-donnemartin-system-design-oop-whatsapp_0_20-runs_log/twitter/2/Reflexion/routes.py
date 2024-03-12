from flask import Flask, request, jsonify
from models import db, User, Post, Comment, Like, Follow, Message, Notification, bcrypt

app = Flask(__name__)

@app.route('/register', methods=['POST'])
def register():
	data = request.get_json()
	hashed_password = bcrypt.generate_password_hash(data['password']).decode('utf-8')
	user = User(email=data['email'], username=data['username'], password=hashed_password)
	db.session.add(user)
	db.session.commit()
	return jsonify({'message': 'Registered successfully'}), 201

@app.route('/login', methods=['POST'])
def login():
	data = request.get_json()
	user = User.query.filter_by(email=data['email']).first()
	if user and bcrypt.check_password_hash(user.password, data['password']):
		return jsonify({'message': 'Logged in successfully'}), 200
	return jsonify({'message': 'Invalid credentials'}), 401

@app.route('/post', methods=['POST'])
def create_post():
	data = request.get_json()
	post = Post(content=data['content'], user_id=data['user_id'])
	db.session.add(post)
	db.session.commit()
	return jsonify({'message': 'Post created successfully'}), 201

@app.route('/post/<int:post_id>', methods=['GET', 'DELETE'])
def handle_post(post_id):
	post = Post.query.get(post_id)
	if request.method == 'GET':
		return jsonify({'content': post.content, 'user_id': post.user_id}), 200
	elif request.method == 'DELETE':
		db.session.delete(post)
		db.session.commit()
		return jsonify({'message': 'Post deleted successfully'}), 200

@app.route('/comment', methods=['POST'])
def create_comment():
	data = request.get_json()
	comment = Comment(content=data['content'], post_id=data['post_id'], user_id=data['user_id'])
	db.session.add(comment)
	db.session.commit()
	return jsonify({'message': 'Comment created successfully'}), 201

@app.route('/like', methods=['POST'])
def create_like():
	data = request.get_json()
	like = Like(post_id=data['post_id'], user_id=data['user_id'])
	db.session.add(like)
	db.session.commit()
	return jsonify({'message': 'Like added successfully'}), 201

@app.route('/follow', methods=['POST'])
def create_follow():
	data = request.get_json()
	follow = Follow(follower_id=data['follower_id'], followed_id=data['followed_id'])
	db.session.add(follow)
	db.session.commit()
	return jsonify({'message': 'Follow added successfully'}), 201

@app.route('/message', methods=['POST'])
def create_message():
	data = request.get_json()
	message = Message(content=data['content'], sender_id=data['sender_id'], receiver_id=data['receiver_id'])
	db.session.add(message)
	db.session.commit()
	return jsonify({'message': 'Message sent successfully'}), 201

@app.route('/notification', methods=['POST'])
def create_notification():
	data = request.get_json()
	notification = Notification(content=data['content'], user_id=data['user_id'])
	db.session.add(notification)
	db.session.commit()
	return jsonify({'message': 'Notification created successfully'}), 201

if __name__ == '__main__':
	app.run(debug=True)
