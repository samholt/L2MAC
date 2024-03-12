from flask import Flask, request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
import jwt
import datetime
from functools import wraps

app = Flask(__name__)

users = {}
posts = {}

app.config['SECRET_KEY'] = 'thisissecret'


# Decorator for verifying the JWT
def token_required(f):
	@wraps(f)
	def decorated(*args, **kwargs):
		token = None
		if 'x-access-token' in request.headers:
			token = request.headers['x-access-token']
		if not token:
			return jsonify({'message': 'Token is missing!'}), 401
		try:
			data = jwt.decode(token, app.config['SECRET_KEY'])
			current_user = users[data['username']]
		except:
			return jsonify({'message': 'Token is invalid!'}), 401
		return f(current_user, *args, **kwargs)
	return decorated


@app.route('/register', methods=['POST'])
def register():
	data = request.get_json()
	username = data['username']
	email = data['email']
	password = generate_password_hash(data['password'], method='sha256')
	users[username] = {'username': username, 'email': email, 'password': password}
	return jsonify({'message': 'User registered successfully!'}), 201


@app.route('/login', methods=['POST'])
def login():
	data = request.get_json()
	username = data['username']
	password = data['password']
	if username in users and check_password_hash(users[username]['password'], password):
		token = jwt.encode({'username': username, 'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=30)}, app.config['SECRET_KEY'])
		return jsonify({'token': token.decode('UTF-8')}), 200
	return jsonify({'message': 'Invalid username or password!'}), 401


@app.route('/post', methods=['POST'])
@token_required
def create_post(current_user):
	data = request.get_json()
	content = data['content']
	if len(content) > 280:
		return jsonify({'message': 'Post content exceeds the limit of 280 characters!'}), 400
	posts[len(posts)] = {'username': current_user['username'], 'content': content}
	return jsonify({'message': 'Post created successfully!'}), 201


@app.route('/posts', methods=['GET'])
@token_required
def get_posts(current_user):
	user_posts = [post for post in posts.values() if post['username'] == current_user['username']]
	return jsonify({'posts': user_posts}), 200


if __name__ == '__main__':
	app.run(debug=True)
