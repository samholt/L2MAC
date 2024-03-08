from flask import Flask, request, jsonify
from dataclasses import dataclass

app = Flask(__name__)

clubs = {}
users = {}

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

@app.route('/create_club', methods=['POST'])
def create_club():
	data = request.get_json()
	club = Club(data['name'], data['description'], data['is_private'], [])
	clubs[data['name']] = club
	return jsonify({'message': 'Club created successfully'}), 201

@app.route('/join_club', methods=['POST'])
def join_club():
	data = request.get_json()
	club = clubs.get(data['club_name'])
	if not club:
		return jsonify({'message': 'Club not found'}), 404
	if club.is_private and data['user_email'] not in club.members:
		return jsonify({'message': 'Cannot join private club without invitation'}), 403
	user = users.get(data['user_email'])
	if not user:
		user = User(data['user_name'], data['user_email'], [])
		users[data['user_email']] = user
	user.clubs.append(club.name)
	club.members.append(user.email)
	return jsonify({'message': 'Joined club successfully'}), 200

@app.route('/invite_to_club', methods=['POST'])
def invite_to_club():
	data = request.get_json()
	club = clubs.get(data['club_name'])
	if not club:
		return jsonify({'message': 'Club not found'}), 404
	if data['user_email'] not in club.members:
		club.members.append(data['user_email'])
	return jsonify({'message': 'User invited successfully'}), 200

if __name__ == '__main__':
	app.run(debug=True)
