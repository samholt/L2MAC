from flask import Flask, request

app = Flask(__name__)

# Mock database
DATABASE = {
	'users': {},
	'book_clubs': {},
	'meetings': {},
	'discussions': {},
	'book_selections': {},
	'user_profiles': {},
	'recommendations': {},
	'admin_actions': {},
	'notifications': {},
	'resources': {}
}

# User class
class User:
	def __init__(self, username, password):
		self.username = username
		self.password = password

	def create(self):
		DATABASE['users'][self.username] = self.password

	def authenticate(self, password):
		return DATABASE['users'].get(self.username) == password

	def get_info(self):
		return {'username': self.username, 'password': DATABASE['users'].get(self.username)}

# BookClub class
class BookClub:
	def __init__(self, club_name, is_private=False):
		self.club_name = club_name
		self.is_private = is_private
		self.members = []

	def create(self):
		DATABASE['book_clubs'][self.club_name] = {'is_private': self.is_private, 'members': self.members}

	def set_privacy(self, is_private):
		DATABASE['book_clubs'][self.club_name]['is_private'] = is_private

	def manage_member(self, username, action):
		if action == 'add':
			self.members.append(username)
		elif action == 'remove':
			self.members.remove(username)
		DATABASE['book_clubs'][self.club_name]['members'] = self.members

# Meeting class
class Meeting:
	def __init__(self, meeting_name, club_name, date_time):
		self.meeting_name = meeting_name
		self.club_name = club_name
		self.date_time = date_time

	def schedule(self):
		DATABASE['meetings'][self.meeting_name] = {'club_name': self.club_name, 'date_time': self.date_time}

# Discussion class
class Discussion:
	def __init__(self, discussion_name, club_name):
		self.discussion_name = discussion_name
		self.club_name = club_name
		self.comments = []

	def create(self):
		DATABASE['discussions'][self.discussion_name] = {'club_name': self.club_name, 'comments': self.comments}

	def post_comment(self, username, comment):
		self.comments.append({'username': username, 'comment': comment})
		DATABASE['discussions'][self.discussion_name]['comments'] = self.comments

# Book class
class Book:
	def __init__(self, book_name, club_name):
		self.book_name = book_name
		self.club_name = club_name
		self.votes = 0

	def suggest(self):
		DATABASE['book_selections'][self.book_name] = {'club_name': self.club_name, 'votes': self.votes}

	def vote(self):
		self.votes += 1
		DATABASE['book_selections'][self.book_name]['votes'] = self.votes

@app.route('/')
def home():
	return 'Welcome to the Book Club App!'

@app.route('/register', methods=['POST'])
def register():
	data = request.get_json()
	user = User(data['username'], data['password'])
	user.create()
	return 'User registered successfully', 201

@app.route('/login', methods=['POST'])
def login():
	data = request.get_json()
	user = User(data['username'], data['password'])
	if user.authenticate(data['password']):
		return 'User logged in successfully', 200
	else:
		return 'Invalid username or password', 401

@app.route('/create_club', methods=['POST'])
def create_club():
	data = request.get_json()
	club = BookClub(data['club_name'], data['is_private'])
	club.create()
	return 'Book club created successfully', 201

@app.route('/set_privacy', methods=['POST'])
def set_privacy():
	data = request.get_json()
	club = BookClub(data['club_name'])
	club.set_privacy(data['is_private'])
	return 'Book club privacy set successfully', 200

@app.route('/manage_member', methods=['POST'])
def manage_member():
	data = request.get_json()
	club = BookClub(data['club_name'])
	club.manage_member(data['username'], data['action'])
	return 'Member managed successfully', 200

@app.route('/schedule_meeting', methods=['POST'])
def schedule_meeting():
	data = request.get_json()
	meeting = Meeting(data['meeting_name'], data['club_name'], data['date_time'])
	meeting.schedule()
	return 'Meeting scheduled successfully', 201

@app.route('/create_discussion', methods=['POST'])
def create_discussion():
	data = request.get_json()
	discussion = Discussion(data['discussion_name'], data['club_name'])
	discussion.create()
	return 'Discussion created successfully', 201

@app.route('/post_comment', methods=['POST'])
def post_comment():
	data = request.get_json()
	discussion = Discussion(data['discussion_name'], data['club_name'])
	discussion.post_comment(data['username'], data['comment'])
	return 'Comment posted successfully', 201

@app.route('/suggest_book', methods=['POST'])
def suggest_book():
	data = request.get_json()
	book = Book(data['book_name'], data['club_name'])
	book.suggest()
	return 'Book suggested successfully', 201

@app.route('/vote_book', methods=['POST'])
def vote_book():
	data = request.get_json()
	book = Book(data['book_name'], data['club_name'])
	book.vote()
	return 'Book voted successfully', 200

if __name__ == '__main__':
	app.run(debug=True)
