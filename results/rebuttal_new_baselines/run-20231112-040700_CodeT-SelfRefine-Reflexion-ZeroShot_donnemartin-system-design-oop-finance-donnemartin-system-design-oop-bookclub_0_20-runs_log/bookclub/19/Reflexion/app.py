from flask import Flask, request
from dataclasses import dataclass

app = Flask(__name__)

# Mock database
users = {}
clubs = {}

@dataclass
class User:
	id: int
	name: str
	clubs: list

@dataclass
class Club:
	id: int
	name: str
	members: list

@app.route('/create_user', methods=['POST'])
def create_user():
	data = request.get_json()
	user = User(id=data['id'], name=data['name'], clubs=[])
	users[user.id] = user
	return {'message': 'User created successfully'}, 201

@app.route('/create_club', methods=['POST'])
def create_club():
	data = request.get_json()
	club = Club(id=data['id'], name=data['name'], members=[])
	clubs[club.id] = club
	return {'message': 'Club created successfully'}, 201

@app.route('/join_club', methods=['POST'])
def join_club():
	data = request.get_json()
	user = users[data['user_id']]
	club = clubs[data['club_id']]
	user.clubs.append(club.id)
	club.members.append(user.id)
	return {'message': 'User joined club successfully'}, 200

if __name__ == '__main__':
	app.run(debug=True)
