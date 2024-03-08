from flask import Flask, request, jsonify
from dataclasses import dataclass
from typing import Dict

app = Flask(__name__)

# Mock database
DATABASE = {}

@dataclass
class User:
	name: str
	email: str
	clubs: Dict[str, 'Club']

@dataclass
class Club:
	name: str
	description: str
	is_private: bool
	members: Dict[str, User]

@app.route('/create_user', methods=['POST'])
def create_user():
	data = request.get_json()
	user = User(name=data['name'], email=data['email'], clubs={})
	DATABASE[data['email']] = user
	return jsonify({'message': 'User created successfully'}), 201

@app.route('/create_club', methods=['POST'])
def create_club():
	data = request.get_json()
	club = Club(name=data['name'], description=data['description'], is_private=data['is_private'], members={})
	DATABASE[data['creator_email']].clubs[data['name']] = club
	return jsonify({'message': 'Club created successfully'}), 201

if __name__ == '__main__':
	app.run(debug=True)
