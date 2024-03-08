from flask import Flask, request, jsonify
from dataclasses import dataclass

app = Flask(__name__)

# Mock database
DATABASE = {}

@dataclass
class User:
	name: str
	email: str
	clubs: list

@dataclass
class Club:
	name: str
	description: str
	is_private: bool
	members: list

@app.route('/create_user', methods=['POST'])
def create_user():
	data = request.get_json()
	user = User(**data)
	DATABASE[user.name] = user
	return jsonify({'message': 'User created'}), 201

@app.route('/create_club', methods=['POST'])
def create_club():
	data = request.get_json()
	club = Club(**data)
	DATABASE[club.name] = club
	return jsonify({'message': 'Club created'}), 201

if __name__ == '__main__':
	app.run(debug=True)
