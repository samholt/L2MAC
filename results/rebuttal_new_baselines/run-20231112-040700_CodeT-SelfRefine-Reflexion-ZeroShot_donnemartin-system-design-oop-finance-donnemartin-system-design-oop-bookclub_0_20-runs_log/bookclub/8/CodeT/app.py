from flask import Flask, request, jsonify
from dataclasses import dataclass
from typing import Dict

app = Flask(__name__)

# Mock database
clubs = {}
users = {}

@dataclass
class Club:
	name: str
	description: str
	is_private: bool
	members: Dict[str, 'User']

@dataclass
class User:
	name: str
	email: str
	clubs: Dict[str, Club]

@app.route('/create_club', methods=['POST'])
def create_club():
	data = request.get_json()
	club = Club(data['name'], data['description'], data['is_private'], {})
	clubs[data['name']] = club
	return jsonify({'message': 'Club created successfully'}), 201

@app.route('/create_user', methods=['POST'])
def create_user():
	data = request.get_json()
	user = User(data['name'], data['email'], {})
	users[data['name']] = user
	return jsonify({'message': 'User created successfully'}), 201

@app.route('/join_club', methods=['POST'])
def join_club():
	data = request.get_json()
	user = users[data['user_name']]
	club = clubs[data['club_name']]
	if club.is_private:
		return jsonify({'message': 'This club is private'}), 403
	user.clubs[club.name] = club
	club.members[user.name] = user
	return jsonify({'message': 'User joined the club successfully'}), 200

if __name__ == '__main__':
	app.run(debug=True)
