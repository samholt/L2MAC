from flask import Flask, request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
import jwt
import datetime
from functools import wraps

app = Flask(__name__)
app.config['SECRET_KEY'] = 'thisissecret'

users = {}
sessions = {}


def token_required(f):
	@wraps(f)
	def decorated(*args, **kwargs):
		token = None
		if 'x-access-token' in request.headers:
			token = request.headers['x-access-token']
		if not token:
			return jsonify({'message' : 'Token is missing!'}), 401
		try:
			data = jwt.decode(token, app.config['SECRET_KEY'])
			current_user = sessions.get(data['username'])
		except:
			return jsonify({'message' : 'Token is invalid!'}), 401
		return f(current_user, *args, **kwargs)
	return decorated


@app.route('/register', methods=['POST'])

def register():
	data = request.get_json()
	hashed_password = generate_password_hash(data['password'], method='sha256')
	users[data['username']] = {'password': hashed_password}
	return jsonify({'message' : 'New user registered!'}), 201


@app.route('/login', methods=['POST'])

def login():
	data = request.get_json()
	user = users.get(data['username'])
	if not user or not check_password_hash(user['password'], data['password']):
		return jsonify({'message' : 'Login failed!'}), 401
	token = jwt.encode({'username' : data['username'], 'exp' : datetime.datetime.utcnow() + datetime.timedelta(minutes=30)}, app.config['SECRET_KEY'])
	sessions[data['username']] = {'token': token}
	return jsonify({'token' : token.decode('UTF-8')}), 200


@app.route('/post', methods=['POST'])
@token_required
def post(current_user):
	data = request.get_json()
	current_user['posts'] = current_user.get('posts', []) + [data['post']]
	return jsonify({'message' : 'New post created!'}), 201


if __name__ == '__main__':
	app.run(debug=True)
