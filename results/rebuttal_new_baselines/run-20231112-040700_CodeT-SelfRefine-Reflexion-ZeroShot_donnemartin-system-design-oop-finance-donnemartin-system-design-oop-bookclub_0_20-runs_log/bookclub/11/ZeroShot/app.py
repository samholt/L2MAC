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

if __name__ == '__main__':
	app.run(debug=True)
