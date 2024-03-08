from flask import Flask, request, jsonify
from dataclasses import dataclass
from typing import List

app = Flask(__name__)

clubs = {}
users = {}

@dataclass
class Club:
	name: str
	description: str
	is_private: bool
	members: List[str]

@dataclass
class User:
	name: str
	clubs: List[str]

@app.route('/create_club', methods=['POST'])
def create_club():
	data = request.get_json()
	if 'name' in data and data['name'] in clubs:
		return jsonify({'error': 'Club already exists'}), 400
	club = Club(**data)
	clubs[club.name] = club
	return jsonify(club), 201

@app.route('/join_club', methods=['POST'])
def join_club():
	data = request.get_json()
	user_name = data['user_name']
	club_name = data['club_name']
	if club_name not in clubs or user_name not in users:
		return jsonify({'error': 'Invalid user or club'}), 400
	club = clubs[club_name]
	user = users[user_name]
	if user_name in club.members:
		return jsonify({'error': 'User already a member'}), 400
	club.members.append(user_name)
	user.clubs.append(club_name)
	return jsonify(club), 200

@app.route('/leave_club', methods=['POST'])
def leave_club():
	data = request.get_json()
	user_name = data['user_name']
	club_name = data['club_name']
	if club_name not in clubs or user_name not in users:
		return jsonify({'error': 'Invalid user or club'}), 400
	club = clubs[club_name]
	user = users[user_name]
	if user_name not in club.members:
		return jsonify({'error': 'User not a member'}), 400
	club.members.remove(user_name)
	user.clubs.remove(club_name)
	return jsonify(club), 200

if __name__ == '__main__':
	app.run(debug=True)
