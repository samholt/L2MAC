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

@app.route('/create_user', methods=['POST'])
def create_user():
	data = request.get_json()
	if data['name'] in users:
		return jsonify({'message': 'User already exists'}), 400
	user = User(data['name'], data['email'], [])
	users[data['name']] = user
	return jsonify({'message': 'User created successfully'}), 201

@app.route('/create_club', methods=['POST'])
def create_club():
	data = request.get_json()
	if data['name'] in clubs:
		return jsonify({'message': 'Club already exists'}), 400
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
		return jsonify({'message': 'Cannot join a private club'}), 403
	user = users.get(data['user_name'])
	if not user:
		return jsonify({'message': 'User not found'}), 404
	club.members.append(user)
	user.clubs.append(club)
	return jsonify({'message': 'Joined club successfully'}), 200

if __name__ == '__main__':
	app.run(debug=True)
