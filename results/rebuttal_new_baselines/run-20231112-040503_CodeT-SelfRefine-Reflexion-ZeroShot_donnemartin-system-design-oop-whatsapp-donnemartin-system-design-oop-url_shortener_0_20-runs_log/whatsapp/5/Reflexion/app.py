from flask import Flask, request, jsonify
from dataclasses import dataclass

app = Flask(__name__)

@dataclass
class User:
	id: str
	email: str
	password: str

users_db = {}

@app.route('/register', methods=['POST'])
def register():
	data = request.get_json()
	user = User(**data)
	users_db[user.id] = user
	return jsonify(user), 201

@app.route('/login', methods=['POST'])
def login():
	data = request.get_json()
	user = users_db.get(data['id'])
	if user and user.password == data['password']:
		return jsonify(user), 200
	return {'message': 'Invalid credentials'}, 401

if __name__ == '__main__':
	app.run(debug=True)
