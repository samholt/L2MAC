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
	clubs: Dict[str, 'Club']

@app.route('/create_club', methods=['POST'])
def create_club():
	data = request.get_json()
	club = Club(data['name'], data['description'], data['is_private'], {})
	clubs[data['name']] = club
	return jsonify({'message': 'Club created successfully'}), 201

@app.route('/join_club', methods=['POST'])
def join_club():
	data = request.get_json()
	club = clubs.get(data['club_name'])
	user = users.get(data['user_name'])
	if club and user:
		if not club.is_private or (club.is_private and data.get('invite_code') == 'SECRET'):
			club.members[data['user_name']] = user
			user.clubs[data['club_name']] = club
			return jsonify({'message': 'Joined club successfully'}), 200
	return jsonify({'message': 'Failed to join club'}), 400

if __name__ == '__main__':
	app.run(debug=True)
