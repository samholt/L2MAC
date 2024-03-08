from flask import Flask, request, jsonify
from flask_jwt_extended import JWTManager
from models import db, User, Post, Comment, Like, Follow, Message, Notification

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
	# Authentication logic here
	pass

@app.route('/post', methods=['POST'])
def create_post():
	# Post creation logic here
	pass

@app.route('/post/<int:post_id>', methods=['DELETE'])
def delete_post(post_id):
	# Post deletion logic here
	pass

@app.route('/post/<int:post_id>/like', methods=['POST'])
def like_post(post_id):
	# Post liking logic here
	pass

@app.route('/post/<int:post_id>/comment', methods=['POST'])
def comment_post(post_id):
	# Post commenting logic here
	pass

@app.route('/follow/<int:user_id>', methods=['POST'])
def follow_user(user_id):
	# User following logic here
	pass

@app.route('/message', methods=['POST'])
def send_message():
	# Message sending logic here
	pass

@app.route('/notification', methods=['GET'])
def get_notifications():
	# Notification retrieval logic here
	pass

if __name__ == '__main__':
	app.run(debug=True)
