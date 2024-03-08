from flask import Flask, request, jsonify
from dataclasses import dataclass

app = Flask(__name__)

# Mock database
users = {}
clubs = {}
meetings = {}
discussions = {}


@dataclass
class User:
	id: str
	name: str
	clubs: list
	reading_list: list
	recommendations: list


@dataclass
class Club:
	id: str
	name: str
	members: list
	privacy: str
	admin: str


@dataclass
class Meeting:
	id: str
	club_id: str
	date: str
	reminder: bool


@dataclass
class Discussion:
	id: str
	club_id: str
	book: str
	comments: list


@app.route('/user', methods=['POST'])
def create_user():
	data = request.get_json()
	user = User(**data)
	users[user.id] = user
	return jsonify(user), 201


@app.route('/club', methods=['POST'])
def create_club():
	data = request.get_json()
	club = Club(**data)
	clubs[club.id] = club
	return jsonify(club), 201


@app.route('/meeting', methods=['POST'])
def create_meeting():
	data = request.get_json()
	meeting = Meeting(**data)
	meetings[meeting.id] = meeting
	return jsonify(meeting), 201


@app.route('/discussion', methods=['POST'])
def create_discussion():
	data = request.get_json()
	discussion = Discussion(**data)
	discussions[discussion.id] = discussion
	return jsonify(discussion), 201


if __name__ == '__main__':
	app.run(debug=True)
