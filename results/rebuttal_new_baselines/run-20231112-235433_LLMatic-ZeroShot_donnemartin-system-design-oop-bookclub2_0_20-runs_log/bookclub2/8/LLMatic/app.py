from flask import Flask, request, jsonify, render_template
from user import User
from book_club import BookClub
from meeting import Meeting
from forum import Forum
from profile import Profile
from admin import Admin

app = Flask(__name__)

users = {}
book_clubs = {}
meetings = {}
forums = {}
profiles = {}
admins = {}

@app.route('/register', methods=['GET', 'POST'])
def register():
	if request.method == 'POST':
		data = request.get_json()
		username = data['username']
		password = data['password']
		email = data['email']
		user = User(username, password, email)
		users[username] = user
		return jsonify({'message': 'User registered successfully'}), 201
	return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
	if request.method == 'POST':
		data = request.get_json()
		username = data['username']
		password = data['password']
		user = users.get(username)
		if user and user.authenticate(username, password):
			return jsonify({'message': 'Login successful'}), 200
		return jsonify({'message': 'Invalid username or password'}), 401
	return render_template('login.html')

@app.route('/book_club', methods=['GET', 'POST'])
def create_book_club():
	if request.method == 'POST':
		data = request.get_json()
		name = data['name']
		description = data['description']
		is_private = data['is_private']
		book_club = BookClub(name, description, is_private)
		book_clubs[name] = book_club
		return jsonify({'message': 'Book club created successfully'}), 201
	return render_template('book_club.html')

@app.route('/meeting', methods=['GET', 'POST'])
def schedule_meeting():
	if request.method == 'POST':
		data = request.get_json()
		date = data['date']
		time = data['time']
		book = data['book']
		meeting = Meeting(date, time, book)
		meetings[book] = meeting
		return jsonify({'message': 'Meeting scheduled successfully'}), 201
	return render_template('meeting.html')

@app.route('/forum', methods=['GET', 'POST'])
def create_forum():
	if request.method == 'POST':
		data = request.get_json()
		book_club = data['book_club']
		book = data['book']
		forum = Forum(book_club, book)
		forums[book] = forum
		return jsonify({'message': 'Forum created successfully'}), 201
	return render_template('forum.html')

@app.route('/profile', methods=['GET', 'POST'])
def create_profile():
	if request.method == 'POST':
		data = request.get_json()
		username = data['username']
		user = users.get(username)
		if user:
			profile = Profile(user)
			profiles[username] = profile
			return jsonify({'message': 'Profile created successfully'}), 201
		return jsonify({'message': 'User not found'}), 404
	return render_template('profile.html')

@app.route('/admin', methods=['GET', 'POST'])
def create_admin():
	if request.method == 'POST':
		data = request.get_json()
		username = data['username']
		managed_book_clubs = data['managed_book_clubs']
		user = users.get(username)
		if user:
			admin = Admin(user, managed_book_clubs)
			admins[username] = admin
			return jsonify({'message': 'Admin created successfully'}), 201
		return jsonify({'message': 'User not found'}), 404
	return render_template('admin.html')

if __name__ == '__main__':
	app.run(debug=True)
