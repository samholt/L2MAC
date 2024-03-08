from flask import Flask, request, jsonify
from dataclasses import dataclass
from typing import Dict

app = Flask(__name__)

# Mock database
DB = {
	'users': {},
	'clubs': {},
	'meetings': {},
	'forums': {},
	'profiles': {},
	'admins': {}
}

@dataclass
class User:
	id: str
	name: str

@dataclass
class Club:
	id: str
	name: str
	privacy: str
	creator: User

@dataclass
class Meeting:
	id: str
	club: Club
	date: str

@dataclass
class Forum:
	id: str
	club: Club

@dataclass
class Profile:
	id: str
	user: User
	reading_list: Dict[str, str]

@dataclass
class Admin:
	id: str
	user: User

@app.route('/create_user', methods=['POST'])
def create_user():
	data = request.get_json()
	user = User(id=data['id'], name=data['name'])
	DB['users'][user.id] = user
	return jsonify({'message': 'User created'}), 201

@app.route('/create_club', methods=['POST'])
def create_club():
	data = request.get_json()
	creator = DB['users'].get(data['creator_id'])
	club = Club(id=data['id'], name=data['name'], privacy=data['privacy'], creator=creator)
	DB['clubs'][club.id] = club
	return jsonify({'message': 'Club created'}), 201

@app.route('/create_meeting', methods=['POST'])
def create_meeting():
	data = request.get_json()
	club = DB['clubs'].get(data['club_id'])
	meeting = Meeting(id=data['id'], club=club, date=data['date'])
	DB['meetings'][meeting.id] = meeting
	return jsonify({'message': 'Meeting created'}), 201

@app.route('/create_forum', methods=['POST'])
def create_forum():
	data = request.get_json()
	club = DB['clubs'].get(data['club_id'])
	forum = Forum(id=data['id'], club=club)
	DB['forums'][forum.id] = forum
	return jsonify({'message': 'Forum created'}), 201

@app.route('/create_profile', methods=['POST'])
def create_profile():
	data = request.get_json()
	user = DB['users'].get(data['user_id'])
	profile = Profile(id=data['id'], user=user, reading_list=data['reading_list'])
	DB['profiles'][profile.id] = profile
	return jsonify({'message': 'Profile created'}), 201

@app.route('/create_admin', methods=['POST'])
def create_admin():
	data = request.get_json()
	user = DB['users'].get(data['user_id'])
	admin = Admin(id=data['id'], user=user)
	DB['admins'][admin.id] = admin
	return jsonify({'message': 'Admin created'}), 201

if __name__ == '__main__':
	app.run(debug=True)
