from flask import Flask, request
from database import users, posts, comments, messages, notifications
from models import User, Post, Comment, Message, Notification

app = Flask(__name__)

@app.route('/register', methods=['POST'])
def register():
	# TODO: Implement user registration
	pass

@app.route('/login', methods=['POST'])
def login():
	# TODO: Implement user login
	pass

@app.route('/reset_password', methods=['POST'])
def reset_password():
	# TODO: Implement password reset
	pass

@app.route('/edit_profile', methods=['POST'])
def edit_profile():
	# TODO: Implement profile editing
	pass

@app.route('/toggle_privacy', methods=['POST'])
def toggle_privacy():
	# TODO: Implement privacy toggling
	pass

@app.route('/create_post', methods=['POST'])
def create_post():
	# TODO: Implement post creation
	pass

@app.route('/delete_post', methods=['POST'])
def delete_post():
	# TODO: Implement post deletion
	pass

@app.route('/like_post', methods=['POST'])
def like_post():
	# TODO: Implement post liking
	pass

@app.route('/retweet', methods=['POST'])
def retweet():
	# TODO: Implement retweeting
	pass

@app.route('/reply', methods=['POST'])
def reply():
	# TODO: Implement replying
	pass

@app.route('/follow', methods=['POST'])
def follow():
	# TODO: Implement following
	pass

@app.route('/unfollow', methods=['POST'])
def unfollow():
	# TODO: Implement unfollowing
	pass

@app.route('/timeline', methods=['GET'])
def timeline():
	# TODO: Implement timeline viewing
	pass

@app.route('/notifications', methods=['GET'])
def notifications():
	# TODO: Implement notifications viewing
	pass

@app.route('/trending', methods=['GET'])
def trending():
	# TODO: Implement trending topics viewing
	pass

@app.route('/recommendations', methods=['GET'])
def recommendations():
	# TODO: Implement user recommendations
	pass

if __name__ == '__main__':
	app.run(debug=True)
