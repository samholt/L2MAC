from flask import Flask, request
from dataclasses import dataclass
import json

app = Flask(__name__)

# Mock database
DATABASE = {
	'users': {},
	'clubs': {},
	'books': {},
	'meetings': {}
}

@dataclass
class User:
	id: str
	name: str
	clubs: list
	books: list

@dataclass
class Club:
	id: str
	name: str
	members: list
	books: list
	meetings: list

@dataclass
class Book:
	id: str
	title: str
	author: str

@dataclass
class Meeting:
	id: str
	club_id: str
	book_id: str
	date: str

@app.route('/user', methods=['POST'])
def create_user():
	data = request.get_json()
	user = User(**data)
	DATABASE['users'][user.id] = user
	return json.dumps(user.__dict__), 201

@app.route('/club', methods=['POST'])
def create_club():
	data = request.get_json()
	club = Club(**data)
	DATABASE['clubs'][club.id] = club
	return json.dumps(club.__dict__), 201

@app.route('/book', methods=['POST'])
def create_book():
	data = request.get_json()
	book = Book(**data)
	DATABASE['books'][book.id] = book
	return json.dumps(book.__dict__), 201

@app.route('/meeting', methods=['POST'])
def create_meeting():
	data = request.get_json()
	meeting = Meeting(**data)
	DATABASE['meetings'][meeting.id] = meeting
	return json.dumps(meeting.__dict__), 201

if __name__ == '__main__':
	app.run(debug=True)
