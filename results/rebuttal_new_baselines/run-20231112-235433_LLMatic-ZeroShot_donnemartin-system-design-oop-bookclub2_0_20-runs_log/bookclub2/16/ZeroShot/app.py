from flask import Flask, request
from dataclasses import dataclass
import json

app = Flask(__name__)

# Mock database
DATABASE = {}

@dataclass
class User:
	id: str
	name: str
	clubs: list
	reading_list: list

@dataclass
class Club:
	id: str
	name: str
	members: list
	books: list
	meetings: list

@app.route('/create_user', methods=['POST'])
def create_user():
	data = request.get_json()
	user = User(**data)
	DATABASE[user.id] = user
	return {'status': 'User created'}, 201

@app.route('/create_club', methods=['POST'])
def create_club():
	data = request.get_json()
	club = Club(**data)
	DATABASE[club.id] = club
	return {'status': 'Club created'}, 201

@app.route('/join_club', methods=['POST'])
def join_club():
	data = request.get_json()
	user_id = data['user_id']
	club_id = data['club_id']
	user = DATABASE[user_id]
	club = DATABASE[club_id]
	user.clubs.append(club_id)
	club.members.append(user_id)
	return {'status': 'Joined club'}, 200

if __name__ == '__main__':
	app.run(debug=True)
