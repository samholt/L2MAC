from flask import Flask, request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from database import get_user, add_user
from models import User
import uuid


app = Flask(__name__)


@app.route('/register', methods=['POST'])
def register():
	data = request.get_json()
	username = data.get('username')
	password = data.get('password')
	if not username or not password:
		return jsonify({'message': 'Missing username or password'}), 400
	if get_user(username):
		return jsonify({'message': 'Username already exists'}), 400
	user = User(id=str(uuid.uuid4()), username=username, password=generate_password_hash(password), urls=[])
	add_user(user)
	return jsonify({'message': 'User registered successfully'}), 200


@app.route('/login', methods=['POST'])
def login():
	data = request.get_json()
	username = data.get('username')
	password = data.get('password')
	user = get_user(username)
	if not user or not check_password_hash(user.password, password):
		return jsonify({'message': 'Invalid username or password'}), 400
	return jsonify({'message': 'Logged in successfully'}), 200

