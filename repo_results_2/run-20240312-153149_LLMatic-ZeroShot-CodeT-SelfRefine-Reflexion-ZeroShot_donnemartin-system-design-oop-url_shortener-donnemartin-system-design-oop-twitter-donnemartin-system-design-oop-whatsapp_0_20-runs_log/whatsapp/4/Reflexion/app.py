from flask import Flask, request, jsonify
from dataclasses import dataclass

app = Flask(__name__)

users = {}
sessions = {}

@dataclass
class User:
	id: str
	email: str
	password: str

@app.route('/register', methods=['POST'])
def register():
	data = request.get_json()
	user = User(id=data['id'], email=data['email'], password=data['password'])
	users[user.id] = user
	return jsonify({'id': user.id}), 201

@app.route('/login', methods=['POST'])
def login():
	data = request.get_json()
	user = users.get(data['id'])
	if user and user.password == data['password']:
		sessions[user.id] = 'Logged In'
		return jsonify({'id': user.id}), 200
	return 'Unauthorized', 401

if __name__ == '__main__':
	app.run(debug=True)
