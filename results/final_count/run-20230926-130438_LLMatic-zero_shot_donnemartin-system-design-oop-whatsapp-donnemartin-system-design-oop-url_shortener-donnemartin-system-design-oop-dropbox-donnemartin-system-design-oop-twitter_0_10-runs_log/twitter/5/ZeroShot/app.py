from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager, create_access_token, jwt_required

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
app.config['JWT_SECRET_KEY'] = 'super-secret'  # Change this!

db = SQLAlchemy(app)
jwt = JWTManager(app)


@app.route('/register', methods=['POST'])
def register():
	# TODO: Implement user registration
	pass


@app.route('/login', methods=['POST'])
def login():
	# TODO: Implement user login
	pass


@app.route('/profile', methods=['GET', 'POST'])
@jwt_required

def profile():
	# TODO: Implement profile view/edit
	pass


@app.route('/post', methods=['POST'])
@jwt_required

def post():
	# TODO: Implement post creation
	pass


@app.route('/post/<int:post_id>', methods=['GET', 'DELETE'])
@jwt_required

def post_detail(post_id):
	# TODO: Implement post view/delete
	pass


@app.route('/post/<int:post_id>/like', methods=['POST'])
@jwt_required

def like_post(post_id):
	# TODO: Implement post liking
	pass


@app.route('/follow/<int:user_id>', methods=['POST'])
@jwt_required

def follow(user_id):
	# TODO: Implement user following
	pass


@app.route('/message/<int:user_id>', methods=['POST'])
@jwt_required

def message(user_id):
	# TODO: Implement direct messaging
	pass


@app.route('/trending', methods=['GET'])
@jwt_required

def trending():
	# TODO: Implement trending topics
	pass


if __name__ == '__main__':
	app.run(debug=True)
