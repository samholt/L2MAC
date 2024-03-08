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
	creator_email = data['creator_email']
	if creator_email not in DATABASE:
		return jsonify({'message': 'User does not exist'}), 400
	club = Club(name=data['name'], description=data['description'], is_private=data['is_private'], members={})
	DATABASE[creator_email].clubs[data['name']] = club
	return jsonify({'message': 'Club created successfully'}), 201

@app.route('/add_member', methods=['POST'])
def add_member():
	data = request.get_json()
	club_name = data['club_name']
	member_email = data['member_email']
	for user in DATABASE.values():
		if club_name in user.clubs:
			if member_email in DATABASE:
				if member_email in user.clubs[club_name].members:
					return jsonify({'message': 'Member already exists in the club'}), 400
				user.clubs[club_name].members[member_email] = DATABASE[member_email]
				return jsonify({'message': 'Member added successfully'}), 201
	return jsonify({'message': 'Club or member does not exist'}), 400

if __name__ == '__main__':
	app.run(debug=True)
