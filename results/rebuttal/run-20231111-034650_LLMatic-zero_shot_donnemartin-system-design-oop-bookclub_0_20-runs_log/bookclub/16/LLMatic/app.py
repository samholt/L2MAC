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


class User:
	def __init__(self, username, password):
		self.username = username
		self.password = password

	@staticmethod
	def create_user(username, password):
		if username in DATABASE['users']:
			return 'User already exists'
		else:
			DATABASE['users'][username] = User(username, password)
			return 'User created successfully'

	@staticmethod
	def authenticate_user(username, password):
		if username in DATABASE['users'] and DATABASE['users'][username].password == password:
			return 'User authenticated'
		else:
			return 'Authentication failed'

	@staticmethod
	def get_user(username):
		if username in DATABASE['users']:
			return DATABASE['users'][username]
		else:
			return 'User not found'


class BookClub:
	def __init__(self, name, is_private):
		self.name = name
		self.is_private = is_private
		self.members = []

	@staticmethod
	def create_book_club(name, is_private):
		if name in DATABASE['book_clubs']:
			return 'Book club already exists'
		else:
			DATABASE['book_clubs'][name] = BookClub(name, is_private)
			return 'Book club created successfully'

	@staticmethod
	def get_book_club(name):
		if name in DATABASE['book_clubs']:
			return DATABASE['book_clubs'][name]
		else:
			return 'Book club not found'

	def add_member(self, username):
		if username in self.members:
			return 'User is already a member'
		else:
			self.members.append(username)
			return 'User added to the book club'

	def remove_member(self, username):
		if username in self.members:
			self.members.remove(username)
			return 'User removed from the book club'
		else:
			return 'User is not a member of the book club'


class Meeting:
	def __init__(self, meeting_id, book_club_name, date, time):
		self.meeting_id = meeting_id
		self.book_club_name = book_club_name
		self.date = date
		self.time = time

	@staticmethod
	def schedule_meeting(meeting_id, book_club_name, date, time):
		if meeting_id in DATABASE['meetings']:
			return 'Meeting already scheduled'
		else:
			DATABASE['meetings'][meeting_id] = Meeting(meeting_id, book_club_name, date, time)
			return 'Meeting scheduled successfully'

	@staticmethod
	def get_meeting(meeting_id):
		if meeting_id in DATABASE['meetings']:
			return DATABASE['meetings'][meeting_id]
		else:
			return 'Meeting not found'


@app.route('/register', methods=['POST'])
def register():
	username = request.json['username']
	password = request.json['password']
	return User.create_user(username, password)


@app.route('/login', methods=['POST'])
def login():
	username = request.json['username']
	password = request.json['password']
	return User.authenticate_user(username, password)


@app.route('/create_book_club', methods=['POST'])
def create_book_club():
	name = request.json['name']
	is_private = request.json['is_private']
	return BookClub.create_book_club(name, is_private)


@app.route('/get_book_club', methods=['GET'])
def get_book_club():
	name = request.args.get('name')
	return str(BookClub.get_book_club(name))


@app.route('/schedule_meeting', methods=['POST'])
def schedule_meeting():
	meeting_id = request.json['meeting_id']
	book_club_name = request.json['book_club_name']
	date = request.json['date']
	time = request.json['time']
	return Meeting.schedule_meeting(meeting_id, book_club_name, date, time)


@app.route('/get_meeting', methods=['GET'])
def get_meeting():
	meeting_id = request.args.get('meeting_id')
	return str(Meeting.get_meeting(meeting_id))


@app.route('/')
def home():
	return 'Welcome to the Book Club App!'


if __name__ == '__main__':
	app.run(debug=True)
