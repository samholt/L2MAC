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

	def join_club(self, club):
		self.clubs[club.name] = club

@dataclass
class Club:
	name: str
	description: str
	is_private: bool
	members: Dict[str, User]

	def add_member(self, user):
		self.members[user.name] = user

@app.route('/create_user', methods=['POST'])
def create_user():
	data = request.get_json()
	user = User(name=data['name'], email=data['email'], clubs={})
	DATABASE[user.name] = user
	return jsonify({'message': 'User created successfully'}), 201

@app.route('/create_club', methods=['POST'])
def create_club():
	data = request.get_json()
	club = Club(name=data['name'], description=data['description'], is_private=data['is_private'], members={})
	DATABASE[club.name] = club
	return jsonify({'message': 'Club created successfully'}), 201

@app.route('/join_club', methods=['POST'])
def join_club():
	data = request.get_json()
	user = DATABASE.get(data['user_name'])
	club = DATABASE.get(data['club_name'])
	if not user or not club:
		return jsonify({'message': 'User or club not found'}), 404
	user.join_club(club)
	club.add_member(user)
	return jsonify({'message': 'User joined club successfully'}), 200

if __name__ == '__main__':
	app.run(debug=True)
