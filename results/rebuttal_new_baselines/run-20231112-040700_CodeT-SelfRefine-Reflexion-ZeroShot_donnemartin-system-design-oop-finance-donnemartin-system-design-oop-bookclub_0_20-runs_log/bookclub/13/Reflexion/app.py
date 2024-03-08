from flask import Flask, request
from dataclasses import dataclass

app = Flask(__name__)

# Mock database
users = {}
clubs = {}

@dataclass
class User:
	name: str
	email: str
	clubs: list
	books: list

@dataclass
class Club:
	name: str
	description: str
	members: list

@app.route('/create_user', methods=['POST'])
def create_user():
	data = request.get_json()
	user = User(data['name'], data['email'], [], [])
	users[data['email']] = user
	return {'message': 'User created successfully'}, 201

@app.route('/create_club', methods=['POST'])
def create_club():
	data = request.get_json()
	club = Club(data['name'], data['description'], [])
	clubs[data['name']] = club
	return {'message': 'Club created successfully'}, 201

@app.route('/join_club', methods=['POST'])
def join_club():
	data = request.get_json()
	user = users[data['email']]
	club = clubs[data['club_name']]
	user.clubs.append(club)
	club.members.append(user)
	return {'message': 'Joined club successfully'}, 200

@app.route('/add_book', methods=['POST'])
def add_book():
	data = request.get_json()
	user = users[data['email']]
	user.books.append(data['book_name'])
	return {'message': 'Book added successfully'}, 200

if __name__ == '__main__':
	app.run(debug=True)
