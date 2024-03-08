from flask import Flask, request, jsonify
from flask_jwt_extended import JWTManager
from models import db, User, Post, Comment, Like, Follow, Message, Notification, TrendingTopic
from services import UserService, PostService, CommentService, LikeService, FollowService, MessageService, NotificationService, TrendingTopicService

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
app.config['JWT_SECRET_KEY'] = 'super-secret'  # Change this!

jwt = JWTManager(app)
db.init_app(app)

@app.route('/register', methods=['POST'])
def register():
	# Registration logic here
	pass

@app.route('/login', methods=['POST'])
def login():
	# Login logic here
	pass

@app.route('/profile', methods=['GET', 'PUT'])
def profile():
	# Profile management logic here
	pass

@app.route('/post', methods=['POST', 'DELETE'])
def post():
	# Post creation/deletion logic here
	pass

@app.route('/like', methods=['POST', 'DELETE'])
def like():
	# Like/unlike logic here
	pass

@app.route('/follow', methods=['POST', 'DELETE'])
def follow():
	# Follow/unfollow logic here
	pass

@app.route('/message', methods=['POST'])
def message():
	# Direct messaging logic here
	pass

@app.route('/notification', methods=['GET'])
def notification():
	# Notification retrieval logic here
	pass

@app.route('/trending', methods=['GET'])
def trending():
	# Trending topics retrieval logic here
	pass

if __name__ == '__main__':
	app.run(debug=True)
