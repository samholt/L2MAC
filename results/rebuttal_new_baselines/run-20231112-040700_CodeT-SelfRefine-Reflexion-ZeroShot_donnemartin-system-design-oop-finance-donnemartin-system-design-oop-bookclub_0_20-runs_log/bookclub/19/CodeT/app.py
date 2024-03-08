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
	members: Dict

@dataclass
class User:
	name: str
	email: str
	clubs: Dict

@app.route('/create_club', methods=['POST'])
def create_club():
	data = request.get_json()
	club = Club(**data)
	clubs[club.name] = club
	return jsonify({'message': 'Club created successfully'}), 201

@app.route('/join_club', methods=['POST'])
def join_club():
	data = request.get_json()
	club_name = data['club_name']
	user_name = data['user_name']
	club = clubs.get(club_name)
	user = users.get(user_name)
	if not club or not user:
		return jsonify({'message': 'Club or User not found'}), 404
	if club.is_private:
		return jsonify({'message': 'This club is private'}), 403
	club.members[user_name] = user
	user.clubs[club_name] = club
	return jsonify({'message': 'Joined club successfully'}), 200

if __name__ == '__main__':
	app.run(debug=True)
