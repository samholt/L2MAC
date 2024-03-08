from flask import Flask, request, jsonify
from flask_jwt_extended import JWTManager, jwt_required, create_access_token
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['JWT_SECRET_KEY'] = 'super-secret'  # Change this!
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
jwt = JWTManager(app)
db = SQLAlchemy(app)


@app.route('/register', methods=['POST'])
def register():
	# TODO: Implement registration logic
	pass

@app.route('/login', methods=['POST'])
def login():
	# TODO: Implement login logic
	pass

@app.route('/profile', methods=['GET', 'POST'])
@jwt_required

def profile():
	# TODO: Implement profile management logic
	pass

@app.route('/post', methods=['POST'])
@jwt_required

def post():
	# TODO: Implement post creation logic
	pass

@app.route('/post/<int:post_id>', methods=['GET', 'DELETE'])
@jwt_required

def single_post(post_id):
	# TODO: Implement single post view/delete logic
	pass

@app.route('/post/<int:post_id>/like', methods=['POST'])
@jwt_required

def like_post(post_id):
	# TODO: Implement post like logic
	pass

@app.route('/follow/<int:user_id>', methods=['POST'])
@jwt_required

def follow(user_id):
	# TODO: Implement follow logic
	pass

@app.route('/message/<int:user_id>', methods=['POST'])
@jwt_required

def message(user_id):
	# TODO: Implement direct messaging logic
	pass

@app.route('/trending', methods=['GET'])
def trending():
	# TODO: Implement trending topics logic
	pass

if __name__ == '__main__':
	app.run(debug=True)
