from flask import Flask, request
from dataclasses import dataclass
from typing import List

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
	clubs: List[str] = []
	books_read: List[str] = []
	wish_list: List[str] = []
	following: List[str] = []

@dataclass
class Club:
	id: str
	name: str
	description: str
	is_private: bool
	members: List[str] = []
	books: List[str] = []

@dataclass
class Book:
	id: str
	title: str
	author: str
	description: str

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

@app.route('/user/create', methods=['POST'])
def create_user():
	data = request.get_json()
	user = User(**data)
	DB['users'][user.id] = user
	return {'id': user.id}, 201

@app.route('/club/create', methods=['POST'])
def create_club():
	data = request.get_json()
	club = Club(**data)
	DB['clubs'][club.id] = club
	return {'id': club.id}, 201

@app.route('/book/create', methods=['POST'])
def create_book():
	data = request.get_json()
	book = Book(**data)
	DB['books'][book.id] = book
	return {'id': book.id}, 201

@app.route('/meeting/create', methods=['POST'])
def create_meeting():
	data = request.get_json()
	meeting = Meeting(**data)
	DB['meetings'][meeting.id] = meeting
	return {'id': meeting.id}, 201

@app.route('/discussion/create', methods=['POST'])
def create_discussion():
	data = request.get_json()
	discussion = Discussion(**data)
	DB['discussions'][discussion.id] = discussion
	return {'id': discussion.id}, 201

@app.route('/resource/create', methods=['POST'])
def create_resource():
	data = request.get_json()
	resource = Resource(**data)
	DB['resources'][resource.id] = resource
	return {'id': resource.id}, 201

if __name__ == '__main__':
	app.run(debug=True)
