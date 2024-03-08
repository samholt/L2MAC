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
	club = Club(**data)
	clubs[club.name] = club
	return jsonify(club), 201

@app.route('/join_club', methods=['POST'])
def join_club():
	data = request.get_json()
	club_name = data['club_name']
	user_name = data['user_name']
	club = clubs.get(club_name)
	user = users.get(user_name)
	if not club or not user:
		return jsonify({'error': 'Club or user not found'}), 404
	if club.is_private:
		return jsonify({'error': 'Cannot join private club'}), 403
	club.members.append(user_name)
	user.clubs.append(club_name)
	return jsonify({'success': 'Joined club'}), 200

@app.route('/create_user', methods=['POST'])
def create_user():
	data = request.get_json()
	user = User(**data)
	users[user.name] = user
	return jsonify(user), 201

if __name__ == '__main__':
	app.run(debug=True)
