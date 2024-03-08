from flask import Flask, request, jsonify
from user import User
from auth import generate_token, decode_token
from post import Post
from search import Search
from message import Message
from notification import Notification
from trending import add_post_to_db, add_user_to_db, get_trending_hashtags, recommend_users

app = Flask(__name__)

@app.route('/register', methods=['POST'])
def register():
	data = request.get_json()
	user = User(data['email'], data['username'], data['password'])
	result = user.register()
	add_user_to_db(result)
	return jsonify(result), 201

@app.route('/login', methods=['POST'])
def login():
	data = request.get_json()
	token = generate_token(data['username'])
	return jsonify({'token': token}), 200

@app.route('/post', methods=['POST'])
def create_post():
	data = request.get_json()
	post = Post(data['user'], data['text'])
	result = post.create_post()
	add_post_to_db(result)
	return jsonify(result), 201

@app.route('/search', methods=['GET'])
def search():
	data = request.get_json()
	search = Search(data['data'])
	result = search.search_by_keyword(data['keyword'])
	return jsonify(result), 200

@app.route('/message', methods=['POST'])
def send_message():
	data = request.get_json()
	message = Message(data['sender'], data['recipient'], data['text'])
	result = message.send_message()
	return jsonify(result), 200

@app.route('/notification', methods=['POST'])
def send_notification():
	data = request.get_json()
	notification = Notification(data['user'], data['event'])
	result = notification.send_notification()
	return jsonify(result), 200

@app.route('/trending', methods=['GET'])
def trending():
	return jsonify(get_trending_hashtags()), 200

@app.route('/recommend', methods=['GET'])
def recommend():
	data = request.get_json()
	recommendations = recommend_users(data['user'])
	if data['user'] in recommendations:
		recommendations.remove(data['user'])
	return jsonify(recommendations), 200

if __name__ == '__main__':
	app.run(debug=True)
