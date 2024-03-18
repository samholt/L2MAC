from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from user import User
from post import Post

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
db = SQLAlchemy(app)

@app.route('/register', methods=['POST'])
def register():
	data = request.get_json()
	user = User(**data)
	db.session.add(user)
	db.session.commit()
	return jsonify(user.to_dict()), 201

@app.route('/login', methods=['POST'])
def login():
	data = request.get_json()
	email = data.get('email')
	password = data.get('password')
	user = User.query.filter_by(email=email).first()
	if not user or not user.check_password(password):
		return jsonify({'message': 'Invalid email or password'}), 401
	return jsonify(user.to_dict()), 200

@app.route('/users/<email>', methods=['GET', 'PUT'])
def user(email):
	user = User.query.filter_by(email=email).first()
	if request.method == 'GET':
		if not user:
			return jsonify({'message': 'User not found'}), 404
		return jsonify(user.to_dict()), 200
	elif request.method == 'PUT':
		data = request.get_json()
		if not user:
			return jsonify({'message': 'User not found'}), 404
		user.update(**data)
	db.session.commit()
	return jsonify(user.to_dict()), 200

@app.route('/posts', methods=['POST'])
def create_post():
	data = request.get_json()
	post = Post(**data)
	db.session.add(post)
	db.session.commit()
	return jsonify(post.to_dict()), 201

@app.route('/posts/<post_id>', methods=['GET', 'DELETE'])
def post(post_id):
	post = Post.query.filter_by(id=post_id).first()
	if request.method == 'GET':
		if not post:
			return jsonify({'message': 'Post not found'}), 404
		return jsonify(post.to_dict()), 200
	elif request.method == 'DELETE':
		if not post:
			return jsonify({'message': 'Post not found'}), 404
	db.session.delete(post)
	db.session.commit()
	return jsonify({'message': 'Post deleted'}), 200

if __name__ == '__main__':
	app.run(debug=True)
