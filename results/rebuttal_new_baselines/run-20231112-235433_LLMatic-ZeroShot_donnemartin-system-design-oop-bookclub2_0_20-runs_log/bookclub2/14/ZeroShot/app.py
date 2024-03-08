from flask import Flask, request, jsonify
from dataclasses import dataclass

app = Flask(__name__)

# Mock database
DATABASE = {
	'users': {},
	'clubs': {},
	'meetings': {},
	'forums': {},
	'comments': {},
	'votes': {},
	'profiles': {},
	'follows': {},
	'reading_lists': {},
	'recommendations': {},
	'admins': {},
	'moderations': {},
	'analytics': {}
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

@dataclass
class Meeting:
	id: str
	club_id: str
	schedule: str

@dataclass
class Forum:
	id: str
	club_id: str

@dataclass
class Comment:
	id: str
	user_id: str
	forum_id: str
	content: str

@dataclass
class Vote:
	id: str
	user_id: str
	book: str

@dataclass
class Profile:
	id: str
	user_id: str
	bio: str

@dataclass
class Follow:
	id: str
	follower_id: str
	followee_id: str

@dataclass
class ReadingList:
	id: str
	user_id: str
	books: list

@dataclass
class Recommendation:
	id: str
	user_id: str
	book: str

@dataclass
class Admin:
	id: str
	user_id: str

@dataclass
class Moderation:
	id: str
	admin_id: str
	content_id: str
	action: str

@dataclass
class Analytics:
	id: str
	metric: str
	value: int

if __name__ == '__main__':
	app.run(debug=True)
