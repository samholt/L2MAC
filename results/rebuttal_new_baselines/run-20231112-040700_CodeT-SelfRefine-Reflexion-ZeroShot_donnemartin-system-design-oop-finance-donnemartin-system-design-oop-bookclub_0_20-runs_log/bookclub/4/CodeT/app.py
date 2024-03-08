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
	clubs: list

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
	if club.is_private:
		return jsonify({'message': 'This is a private club'}), 403
	user = users.get(data['user_name'])
	if not user:
		return jsonify({'message': 'User not found'}), 404
	club.members.append(user)
	user.clubs.append(club)
	return jsonify({'message': 'Joined club successfully'}), 200

if __name__ == '__main__':
	app.run(debug=True)
