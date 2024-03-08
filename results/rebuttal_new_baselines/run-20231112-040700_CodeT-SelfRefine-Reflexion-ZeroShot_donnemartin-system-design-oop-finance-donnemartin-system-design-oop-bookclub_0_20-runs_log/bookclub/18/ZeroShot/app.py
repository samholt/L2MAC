from flask import Flask, request, jsonify
from dataclasses import dataclass

app = Flask(__name__)

# Mock database
DATABASE = {
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
	books_read: list
	clubs_joined: list

@dataclass
class Club:
	id: str
	name: str
	description: str
	is_private: bool
	members: list

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
	scheduled_time: str

@dataclass
class Discussion:
	id: str
	club_id: str
	book_id: str
	user_id: str
	message: str

@dataclass
class Resource:
	id: str
	title: str
	link: str

@app.route('/user', methods=['POST'])
def create_user():
	data = request.get_json()
	user = User(**data)
	DATABASE['users'][user.id] = user
	return jsonify(user), 201

@app.route('/club', methods=['POST'])
def create_club():
	data = request.get_json()
	club = Club(**data)
	DATABASE['clubs'][club.id] = club
	return jsonify(club), 201

@app.route('/book', methods=['POST'])
def create_book():
	data = request.get_json()
	book = Book(**data)
	DATABASE['books'][book.id] = book
	return jsonify(book), 201

@app.route('/meeting', methods=['POST'])
def schedule_meeting():
	data = request.get_json()
	meeting = Meeting(**data)
	DATABASE['meetings'][meeting.id] = meeting
	return jsonify(meeting), 201

@app.route('/discussion', methods=['POST'])
def create_discussion():
	data = request.get_json()
	discussion = Discussion(**data)
	DATABASE['discussions'][discussion.id] = discussion
	return jsonify(discussion), 201

@app.route('/resource', methods=['POST'])
def create_resource():
	data = request.get_json()
	resource = Resource(**data)
	DATABASE['resources'][resource.id] = resource
	return jsonify(resource), 201

if __name__ == '__main__':
	app.run(debug=True)
