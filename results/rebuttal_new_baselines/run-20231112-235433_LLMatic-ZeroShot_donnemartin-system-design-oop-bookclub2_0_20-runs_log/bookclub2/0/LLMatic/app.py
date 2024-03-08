from flask import Flask, request
from user import User
from book_club import BookClub
from meeting import Meeting
from discussion import Discussion
from admin import Admin

app = Flask(__name__)

# Mock database
users = {}
book_clubs = {}
meetings = {}
discussions = {}
admins = {}

@app.route('/register', methods=['POST'])
def register():
	data = request.get_json()
	user = User(data['username'], data['password'], data['email'])
	users[data['username']] = user
	return {'message': 'User registered successfully'}, 201

@app.route('/login', methods=['POST'])
def login():
	data = request.get_json()
	user = users.get(data['username'])
	if user and user.password == data['password']:
		return {'message': 'Logged in successfully'}, 200
	return {'message': 'Invalid username or password'}, 401

@app.route('/book_clubs', methods=['POST'])
def create_book_club():
	data = request.get_json()
	book_club = BookClub(data['name'], data['privacy_settings'], [], [data['admin']])
	book_clubs[data['name']] = book_club
	return {'message': 'Book club created successfully'}, 201

@app.route('/meetings', methods=['POST'])
def schedule_meeting():
	data = request.get_json()
	meeting = Meeting(data['date'], data['time'], data['book_club'], data['attendees'])
	meetings[data['date']] = meeting
	return {'message': 'Meeting scheduled successfully'}, 201

@app.route('/discussions', methods=['POST'])
def create_discussion():
	data = request.get_json()
	discussion = Discussion(data['book_club'], data['topic'])
	discussions[data['topic']] = discussion
	return {'message': 'Discussion created successfully'}, 201

@app.route('/admins', methods=['POST'])
def create_admin():
	data = request.get_json()
	admin = Admin(data['user'], data['dashboard'])
	admins[data['user']] = admin
	return {'message': 'Admin created successfully'}, 201

if __name__ == '__main__':
	app.run(debug=True)
