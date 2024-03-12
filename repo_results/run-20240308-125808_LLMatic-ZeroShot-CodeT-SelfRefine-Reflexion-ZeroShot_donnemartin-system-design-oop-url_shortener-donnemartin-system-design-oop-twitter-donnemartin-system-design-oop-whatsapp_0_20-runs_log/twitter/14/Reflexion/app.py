from flask import Flask, request, jsonify
from flask_jwt_extended import JWTManager, jwt_required, create_access_token, get_jwt_identity
from werkzeug.security import generate_password_hash, check_password_hash
from dataclasses import dataclass

app = Flask(__name__)
app.config['JWT_SECRET_KEY'] = 'super-secret'  # Change this!
jwt = JWTManager(app)

# Mock database
users = {}
posts = {}

@dataclass
class User:
	username: str
	password: str

@dataclass
class Post:
	user: str
	content: str

@app.route('/register', methods=['POST'])
def register():
	if not request.is_json:
		return jsonify({'msg': 'Missing JSON in request'}), 400

	username = request.json.get('username', None)
	password = request.json.get('password', None)

	if not username:
		return jsonify({'msg': 'Missing username parameter'}), 400
	if not password:
		return jsonify({'msg': 'Missing password parameter'}), 400

	if username in users:
		return jsonify({'msg': 'User already exists'}), 400

	users[username] = User(username, generate_password_hash(password))

	return jsonify({'msg': 'User created'}), 201

@app.route('/login', methods=['POST'])
def login():
	if not request.is_json:
		return jsonify({'msg': 'Missing JSON in request'}), 400

	username = request.json.get('username', None)
	password = request.json.get('password', None)

	if not username:
		return jsonify({'msg': 'Missing username parameter'}), 400
	if not password:
		return jsonify({'msg': 'Missing password parameter'}), 400

	user = users.get(username, None)

	if user is None or not check_password_hash(user.password, password):
		return jsonify({'msg': 'Bad username or password'}), 401

	access_token = create_access_token(identity=username)
	return jsonify(access_token=access_token), 200

@app.route('/post', methods=['POST'])
@jwt_required
def post():
	if not request.is_json:
		return jsonify({'msg': 'Missing JSON in request'}), 400

	content = request.json.get('content', None)

	if not content:
		return jsonify({'msg': 'Missing content parameter'}), 400

	username = get_jwt_identity()
	posts[username] = Post(username, content)

	return jsonify({'msg': 'Post created'}), 201

if __name__ == '__main__':
	app.run(debug=True)
