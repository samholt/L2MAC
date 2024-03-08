from flask import Flask, request, jsonify
from dataclasses import dataclass

app = Flask(__name__)

# Mock database
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

@app.route('/create_user', methods=['POST'])
def create_user():
	data = request.get_json()
	user = User(data['name'], [])
	users[data['name']] = user
	return jsonify({'message': 'User created successfully'}), 201

@app.route('/join_club', methods=['POST'])
def join_club():
	data = request.get_json()
	user = users.get(data['user_name'])
	club = clubs.get(data['club_name'])
	if not user or not club:
		return jsonify({'message': 'User or club not found'}), 404
	if club.is_private:
		return jsonify({'message': 'Cannot join private club'}), 403
	user.clubs.append(club.name)
	club.members.append(user.name)
	return jsonify({'message': 'Joined club successfully'}), 200

if __name__ == '__main__':
	app.run(debug=True)
