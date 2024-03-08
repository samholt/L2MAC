from flask import Flask, request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
import jwt
import datetime
from functools import wraps

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secretkey'

users = {}
posts = {}

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
			current_user = users[data['user']]
		except:
			return jsonify({'message': 'Token is invalid!'}), 401
		return f(current_user, *args, **kwargs)
	return decorated

@app.route('/register', methods=['POST'])
def register():
	data = request.get_json()
	username = data['username']
	email = data['email']
	password = data['password']
	if email in users:
		return jsonify({'message': 'User already exists'}), 400
	users[email] = {
		'username': username,
		'password': generate_password_hash(password, method='sha256'),
		'posts': []
	}
	return jsonify({'message': 'Registered successfully'}), 200

@app.route('/login', methods=['POST'])
def login():
	data = request.get_json()
	email = data['email']
	password = data['password']
	if email not in users or not check_password_hash(users[email]['password'], password):
		return jsonify({'message': 'Invalid credentials'}), 400
	token = jwt.encode({'user': email, 'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=30)}, app.config['SECRET_KEY'])
	return jsonify({'token': token}), 200

@app.route('/post', methods=['POST'])
@token_required
def post(current_user):
	data = request.get_json()
	content = data['content']
	current_user['posts'].append(content)
	return jsonify({'message': 'Posted successfully'}), 200

@app.route('/posts', methods=['GET'])
@token_required
def get_posts(current_user):
	return jsonify({'posts': current_user['posts']}), 200

if __name__ == '__main__':
	app.run(debug=True)
