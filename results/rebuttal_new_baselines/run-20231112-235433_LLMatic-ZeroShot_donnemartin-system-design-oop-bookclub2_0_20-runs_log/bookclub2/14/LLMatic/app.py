from flask import Flask, request
import datetime

app = Flask(__name__)

# Mock database
DATABASE = {
	'users': {},
	'book_clubs': {},
	'meetings': {},
	'discussions': {},
	'books': {},
	'votes': {}
}

# User class
class User:
	def __init__(self, username, password, email):
		self.username = username
		self.password = password
		self.email = email
		self.book_clubs = []
		self.following = []
		self.reading_list = []
		self.recommendations = []

	def add_to_reading_list(self, book):
		self.reading_list.append(book)

	def add_recommendation(self, book):
		self.recommendations.append(book)

# BookClub class
class BookClub:
	def __init__(self, name, privacy, admin):
		self.name = name
		self.privacy = privacy
		self.admin = admin
		self.members = [admin]
		self.books = []

# Meeting class
class Meeting:
	def __init__(self, date, time, book_club):
		self.date = date
		self.time = time
		self.book_club = book_club

# Vote class
class Vote:
	def __init__(self, book_club, book, votes):
		self.book_club = book_club
		self.book = book
		self.votes = votes

# User registration
@app.route('/register', methods=['POST'])
def register():
	data = request.get_json()
	new_user = User(data['username'], data['password'], data['email'])
	DATABASE['users'][new_user.username] = new_user
	return 'User registered successfully!'

# User login
@app.route('/login', methods=['POST'])
def login():
	data = request.get_json()
	user = DATABASE['users'].get(data['username'])
	if user and user.password == data['password']:
		return 'Login successful!'
	else:
		return 'Invalid username or password'

# Create book club
@app.route('/create_book_club', methods=['POST'])
def create_book_club():
	data = request.get_json()
	admin = DATABASE['users'].get(data['admin'])
	if admin:
		new_book_club = BookClub(data['name'], data['privacy'], admin)
		DATABASE['book_clubs'][new_book_club.name] = new_book_club
		admin.book_clubs.append(new_book_club)
		return 'Book club created successfully!'
	else:
		return 'Invalid admin'

# Join book club
@app.route('/join_book_club', methods=['POST'])
def join_book_club():
	data = request.get_json()
	user = DATABASE['users'].get(data['username'])
	book_club = DATABASE['book_clubs'].get(data['book_club'])
	if book_club and user:
		book_club.members.append(user)
		user.book_clubs.append(book_club)
		return 'Joined book club successfully!'
	else:
		return 'Invalid book club or user'

# Schedule meeting
@app.route('/schedule_meeting', methods=['POST'])
def schedule_meeting():
	data = request.get_json()
	book_club = DATABASE['book_clubs'].get(data['book_club'])
	if book_club:
		new_meeting = Meeting(data['date'], data['time'], book_club)
		DATABASE['meetings'][new_meeting.date] = new_meeting
		return 'Meeting scheduled successfully!'
	else:
		return 'Invalid book club'

# Create vote
@app.route('/create_vote', methods=['POST'])
def create_vote():
	data = request.get_json()
	book_club = DATABASE['book_clubs'].get(data['book_club'])
	book = DATABASE['books'].get(data['book'])
	if book_club and book:
		new_vote = Vote(book_club, book, [])
		DATABASE['votes'][new_vote.book] = new_vote
		return 'Vote created successfully!'
	else:
		return 'Invalid book club or book'

# Count votes
@app.route('/count_votes', methods=['GET'])
def count_votes():
	data = request.get_json()
	vote = DATABASE['votes'].get(data['book'])
	if vote:
		return str(len(vote.votes))
	else:
		return 'Invalid book'

# Follow user
@app.route('/follow_user', methods=['POST'])
def follow_user():
	data = request.get_json()
	user = DATABASE['users'].get(data['username'])
	user_to_follow = DATABASE['users'].get(data['user_to_follow'])
	if user and user_to_follow:
		user.following.append(user_to_follow)
		return 'User followed successfully!'
	else:
		return 'Invalid user'

# Add book to reading list
@app.route('/add_to_reading_list', methods=['POST'])
def add_to_reading_list():
	data = request.get_json()
	user = DATABASE['users'].get(data['username'])
	book = DATABASE['books'].get(data['book'])
	if user and book:
		user.add_to_reading_list(book)
		return 'Book added to reading list successfully!'
	else:
		return 'Invalid user or book'

# Add book recommendation
@app.route('/add_recommendation', methods=['POST'])
def add_recommendation():
	data = request.get_json()
	user = DATABASE['users'].get(data['username'])
	book = DATABASE['books'].get(data['book'])
	if user and book:
		user.add_recommendation(book)
		return 'Book recommended successfully!'
	else:
		return 'Invalid user or book'

@app.route('/')
def home():
	return 'Welcome to the Book Club App!'

if __name__ == '__main__':
	app.run(debug=True)
