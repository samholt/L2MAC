from flask import Flask, request, jsonify
from dataclasses import dataclass

app = Flask(__name__)

# Mock database
DATABASE = {}

@dataclass
class User:
	name: str
	email: str
	books_read: list
	books_to_read: list
	clubs: list

@dataclass
class BookClub:
	name: str
	description: str
	is_private: bool
	members: list
	books: list
	meetings: list

@app.route('/create_user', methods=['POST'])
def create_user():
	data = request.get_json()
	user = User(**data)
	DATABASE[user.email] = user
	return jsonify({'message': 'User created successfully'}), 201

@app.route('/create_club', methods=['POST'])
def create_club():
	data = request.get_json()
	club = BookClub(**data)
	DATABASE[club.name] = club
	return jsonify({'message': 'Book club created successfully'}), 201

@app.route('/join_club', methods=['POST'])
def join_club():
	data = request.get_json()
	user = DATABASE[data['user_email']]
	club = DATABASE[data['club_name']]
	user.clubs.append(club.name)
	club.members.append(user.email)
	return jsonify({'message': 'User joined the club successfully'}), 200

@app.route('/add_book', methods=['POST'])
def add_book():
	data = request.get_json()
	user = DATABASE[data['user_email']]
	user.books_to_read.append(data['book'])
	return jsonify({'message': 'Book added to reading list successfully'}), 200

@app.route('/mark_book_as_read', methods=['POST'])
def mark_book_as_read():
	data = request.get_json()
	user = DATABASE[data['user_email']]
	book = data['book']
	user.books_to_read.remove(book)
	user.books_read.append(book)
	return jsonify({'message': 'Book marked as read successfully'}), 200

@app.route('/create_meeting', methods=['POST'])
def create_meeting():
	data = request.get_json()
	club = DATABASE[data['club_name']]
	meeting = data['meeting']
	club.meetings.append(meeting)
	return jsonify({'message': 'Meeting created successfully'}), 200

if __name__ == '__main__':
	app.run(debug=True)
