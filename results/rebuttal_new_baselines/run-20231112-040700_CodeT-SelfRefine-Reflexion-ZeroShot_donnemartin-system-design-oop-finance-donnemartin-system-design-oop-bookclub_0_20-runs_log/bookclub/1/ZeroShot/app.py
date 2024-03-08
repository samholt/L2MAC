from flask import Flask, request, jsonify
from dataclasses import dataclass
from typing import Dict

app = Flask(__name__)

# Mock database
DB = {
	'users': {},
	'clubs': {},
	'books': {},
	'meetings': {},
	'discussions': {},
	'resources': {}
}

@dataclass
class User:
	id: str
	name: str
	email: str
	clubs: Dict[str, str]
	books_read: Dict[str, str]
	books_to_read: Dict[str, str]
	follows: Dict[str, str]

@dataclass
class Club:
	id: str
	name: str
	description: str
	is_private: bool
	members: Dict[str, str]
	books: Dict[str, str]
	meetings: Dict[str, str]
	discussions: Dict[str, str]

@dataclass
class Book:
	id: str
	title: str
	author: str
	description: str
	reviews: Dict[str, str]

@dataclass
class Meeting:
	id: str
	club_id: str
	book_id: str
	date: str
	time: str

@dataclass
class Discussion:
	id: str
	club_id: str
	book_id: str
	user_id: str
	message: str
	replies: Dict[str, str]

@dataclass
class Resource:
	id: str
	title: str
	link: str
	contributor_id: str

@app.route('/users', methods=['POST'])
def create_user():
	data = request.get_json()
	user = User(**data)
	DB['users'][user.id] = user
	return jsonify(user), 201

@app.route('/clubs', methods=['POST'])
def create_club():
	data = request.get_json()
	club = Club(**data)
	DB['clubs'][club.id] = club
	return jsonify(club), 201

@app.route('/books', methods=['POST'])
def create_book():
	data = request.get_json()
	book = Book(**data)
	DB['books'][book.id] = book
	return jsonify(book), 201

@app.route('/meetings', methods=['POST'])
def create_meeting():
	data = request.get_json()
	meeting = Meeting(**data)
	DB['meetings'][meeting.id] = meeting
	return jsonify(meeting), 201

@app.route('/discussions', methods=['POST'])
def create_discussion():
	data = request.get_json()
	discussion = Discussion(**data)
	DB['discussions'][discussion.id] = discussion
	return jsonify(discussion), 201

@app.route('/resources', methods=['POST'])
def create_resource():
	data = request.get_json()
	resource = Resource(**data)
	DB['resources'][resource.id] = resource
	return jsonify(resource), 201

if __name__ == '__main__':
	app.run(debug=True)
