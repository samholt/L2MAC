from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
app.config['JWT_SECRET_KEY'] = 'super-secret'  # Change this!

db = SQLAlchemy(app)
jwt = JWTManager(app)

@app.route('/register', methods=['POST'])
def register():
	# TODO: Implement registration logic
	pass

@app.route('/login', methods=['POST'])
def login():
	# TODO: Implement login logic
	pass

@app.route('/profile', methods=['GET', 'POST'])
def profile():
	# TODO: Implement profile view/edit logic
	pass

@app.route('/post', methods=['POST'])
def create_post():
	# TODO: Implement post creation logic
	pass

@app.route('/post/<int:post_id>', methods=['GET', 'DELETE'])
def post(post_id):
	# TODO: Implement post view/delete logic
	pass

@app.route('/post/<int:post_id>/like', methods=['POST'])
def like_post(post_id):
	# TODO: Implement post like logic
	pass

@app.route('/post/<int:post_id>/comment', methods=['POST'])
def comment_post(post_id):
	# TODO: Implement post comment logic
	pass

@app.route('/follow/<int:user_id>', methods=['POST'])
def follow(user_id):
	# TODO: Implement follow logic
	pass

@app.route('/message/<int:user_id>', methods=['POST'])
def message(user_id):
	# TODO: Implement direct message logic
	pass

@app.route('/trending', methods=['GET'])
def trending():
	# TODO: Implement trending topics logic
	pass

if __name__ == '__main__':
	app.run(debug=True)
