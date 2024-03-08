from flask import Flask, request
from dataclasses import dataclass

app = Flask(__name__)

clubs = {}
users = {}

@dataclass
class User:
	name: str
	email: str
	books_read: list
	clubs_joined: list

@dataclass
class Club:
	name: str
	description: str
	members: list
	books: list

@app.route('/create_user', methods=['POST'])
def create_user():
	data = request.get_json()
	user = User(name=data['name'], email=data['email'], books_read=[], clubs_joined=[])
	users[data['email']] = user
	return {'message': 'User created successfully'}, 201

@app.route('/create_club', methods=['POST'])
def create_club():
	data = request.get_json()
	club = Club(name=data['name'], description=data['description'], members=[], books=[])
	clubs[data['name']] = club
	return {'message': 'Club created successfully'}, 201

if __name__ == '__main__':
	app.run(debug=True)
