from flask import Flask, request, jsonify
from dataclasses import dataclass

app = Flask(__name__)

clubs = {}
users = {}

@dataclass
class Club:
	name: str
description: str
is_private: bool
members: list

@dataclass
class User:
	name: str
email: str
clubs: list

@app.route('/create_club', methods=['POST'])
def create_club():
	data = request.get_json()
	club = Club(**data)
	clubs[club.name] = club
	return jsonify({'message': 'Club created successfully'}), 201

@app.route('/join_club', methods=['POST'])
def join_club():
	data = request.get_json()
	user = users.get(data['user_name'])
	club = clubs.get(data['club_name'])
	if not user or not club:
		return jsonify({'message': 'User or club not found'}), 404
	if club.is_private:
		return jsonify({'message': 'Cannot join a private club'}), 403
	user.clubs.append(club)
	club.members.append(user)
	return jsonify({'message': 'Joined club successfully'}), 200

if __name__ == '__main__':
	app.run(debug=True)
