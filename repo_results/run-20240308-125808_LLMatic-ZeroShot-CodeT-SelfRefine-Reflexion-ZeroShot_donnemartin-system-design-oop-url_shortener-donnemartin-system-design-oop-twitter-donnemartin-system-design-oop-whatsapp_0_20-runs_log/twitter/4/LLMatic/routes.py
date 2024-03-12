from flask import Flask, request, jsonify
from services import UserService, PostService, SocialInteractionService, TrendingDiscoveryService

app = Flask(__name__)

user_service = UserService()
post_service = PostService()
social_service = SocialInteractionService()
trending_service = TrendingDiscoveryService()

@app.route('/register', methods=['POST'])
def register():
	data = request.get_json()
	return jsonify(user_service.register_user(data))

@app.route('/login', methods=['POST'])
def login():
	data = request.get_json()
	return jsonify(user_service.login_user(data))

@app.route('/reset_password', methods=['POST'])
def reset_password():
	data = request.get_json()
	return jsonify(user_service.reset_password(data))

@app.route('/edit_profile', methods=['POST'])
def edit_profile():
	data = request.get_json()
	return jsonify(user_service.edit_profile(data))

@app.route('/create_post', methods=['POST'])
def create_post():
	data = request.get_json()
	return jsonify(post_service.create_post(data))

@app.route('/delete_post', methods=['POST'])
def delete_post():
	data = request.get_json()
	return jsonify(post_service.delete_post(data))

@app.route('/like_post', methods=['POST'])
def like_post():
	data = request.get_json()
	return jsonify(social_service.like_post(data))

@app.route('/create_comment', methods=['POST'])
def create_comment():
	data = request.get_json()
	return jsonify(social_service.create_comment(data))

@app.route('/delete_comment', methods=['POST'])
def delete_comment():
	data = request.get_json()
	return jsonify(social_service.delete_comment(data))

@app.route('/follow_user', methods=['POST'])
def follow_user():
	data = request.get_json()
	return jsonify(social_service.follow_user(data))

@app.route('/unfollow_user', methods=['POST'])
def unfollow_user():
	data = request.get_json()
	return jsonify(social_service.unfollow_user(data))

@app.route('/send_message', methods=['POST'])
def send_message():
	data = request.get_json()
	return jsonify(social_service.send_message(data))

@app.route('/delete_message', methods=['POST'])
def delete_message():
	data = request.get_json()
	return jsonify(social_service.delete_message(data))

@app.route('/view_notifications', methods=['GET'])
def view_notifications():
	return jsonify(trending_service.create_notification())

@app.route('/view_trending', methods=['GET'])
def view_trending():
	return jsonify(trending_service.update_trending_topic())
