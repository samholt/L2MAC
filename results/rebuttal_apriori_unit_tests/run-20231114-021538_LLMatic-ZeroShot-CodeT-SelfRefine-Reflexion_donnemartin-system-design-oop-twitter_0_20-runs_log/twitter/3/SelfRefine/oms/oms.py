from flask import Flask, request, jsonify
from database import Database
from user import User
from post import Post
from message import Message
from notification import Notification
from trending import Trending

app = Flask(__name__)
db = Database()

@app.route('/register', methods=['POST'])
def register():
	data = request.get_json()
	user = User(**data)
	db.add_user(user)
	return jsonify({'message': 'User registered successfully'}), 201

@app.route('/login', methods=['POST'])
def login():
	data = request.get_json()
	user = db.users.get(data['id'])
	if user and user.password == data['password']:
		return jsonify({'message': 'Login successful'}), 200
	return jsonify({'message': 'Invalid credentials'}), 401

@app.route('/post', methods=['POST'])
def post():
	data = request.get_json()
	post = Post(**data)
	db.add_post(post)
	return jsonify({'message': 'Post created successfully'}), 201

@app.route('/message', methods=['POST'])
def message():
	data = request.get_json()
	message = Message(**data)
	db.add_message(message)
	return jsonify({'message': 'Message sent successfully'}), 201

@app.route('/notification', methods=['POST'])
def notification():
	data = request.get_json()
	notification = Notification(**data)
	db.add_notification(notification)
	return jsonify({'message': 'Notification created successfully'}), 201

@app.route('/trending', methods=['POST'])
def trending():
	data = request.get_json()
	trending = Trending(**data)
	db.add_trending(trending)
	return jsonify({'message': 'Trending topic added successfully'}), 201

if __name__ == '__main__':
	app.run(debug=True)
