from flask import Flask, request, jsonify
from dataclasses import dataclass
import jwt
import datetime

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secretkey'

# Mock database
users = {}
posts = {}

@dataclass
class User:
	id: int
	username: str
	email: str
	password: str
	bio: str
	website: str
	location: str
	private: bool

@dataclass
class Post:
	id: int
	user_id: int
	content: str
	image: str

@app.route('/register', methods=['POST'])
def register():
	data = request.get_json()
	new_user = User(len(users) + 1, data['username'], data['email'], data['password'], '', '', '', False)
	users[new_user.id] = new_user
	return jsonify({'message': 'Registered successfully'}), 200

@app.route('/login', methods=['POST'])
def login():
	data = request.get_json()
	for user in users.values():
		if user.email == data['email'] and user.password == data['password']:
			token = jwt.encode({'user_id': user.id, 'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=30)}, app.config['SECRET_KEY'])
			return jsonify({'token': token}), 200
	return jsonify({'message': 'Invalid credentials'}), 401

if __name__ == '__main__':
	app.run(debug=True)
