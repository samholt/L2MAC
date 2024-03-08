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
	follows: list

@dataclass
class Club:
	id: str
	name: str
	members: list
	privacy: str

@dataclass
class Meeting:
	id: str
	club_id: str
	date: str

@app.route('/create_user', methods=['POST'])
def create_user():
	data = request.get_json()
	user = User(**data)
	DATABASE['users'][user.id] = user
	return json.dumps(user.__dict__), 200

@app.route('/create_club', methods=['POST'])
def create_club():
	data = request.get_json()
	club = Club(**data)
	DATABASE['clubs'][club.id] = club
	return json.dumps(club.__dict__), 200

@app.route('/join_club', methods=['POST'])
def join_club():
	data = request.get_json()
	user_id = data['user_id']
	club_id = data['club_id']
	DATABASE['users'][user_id].clubs.append(club_id)
	DATABASE['clubs'][club_id].members.append(user_id)
	return 'Joined club', 200

@app.route('/schedule_meeting', methods=['POST'])
def schedule_meeting():
	data = request.get_json()
	meeting = Meeting(**data)
	DATABASE['meetings'][meeting.id] = meeting
	return json.dumps(meeting.__dict__), 200

if __name__ == '__main__':
	app.run(debug=True)
