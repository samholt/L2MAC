from flask import Flask, request, jsonify

app = Flask(__name__)

# Mock database
DATABASE = {
	'users': {},
	'book_clubs': {},
	'meetings': {},
	'discussions': {},
	'books': {}
}

# User class
class User:
	def __init__(self, username, password, email):
		self.username = username
		self.password = password
		self.email = email
		self.book_clubs = []

# BookClub class
class BookClub:
	def __init__(self, name, privacy, members, current_book):
		self.name = name
		self.privacy = privacy
		self.members = members
		self.current_book = current_book

# User registration
@app.route('/register', methods=['POST'])
def register():
	data = request.get_json()
	new_user = User(data['username'], data['password'], data['email'])
	DATABASE['users'][new_user.username] = new_user
	return jsonify({'message': 'User registered successfully'}), 200

# User login
@app.route('/login', methods=['POST'])
def login():
	data = request.get_json()
	user = DATABASE['users'].get(data['username'])
	if user and user.password == data['password']:
		return jsonify({'message': 'Login successful'}), 200
	else:
		return jsonify({'message': 'Invalid username or password'}), 401

# Create book club
@app.route('/create_book_club', methods=['POST'])
def create_book_club():
	data = request.get_json()
	new_book_club = BookClub(data['name'], data['privacy'], [data['username']], data['current_book'])
	DATABASE['book_clubs'][new_book_club.name] = new_book_club
	DATABASE['users'][data['username']].book_clubs.append(new_book_club.name)
	return jsonify({'message': 'Book club created successfully'}), 200

# Join book club
@app.route('/join_book_club', methods=['POST'])
def join_book_club():
	data = request.get_json()
	book_club = DATABASE['book_clubs'].get(data['book_club_name'])
	if book_club and book_club.privacy == 'public':
		book_club.members.append(data['username'])
		DATABASE['users'][data['username']].book_clubs.append(book_club.name)
		return jsonify({'message': 'Joined book club successfully'}), 200
	else:
		return jsonify({'message': 'Book club not found or is private'}), 401

@app.route('/')
def home():
	return 'Welcome to the Book Club App!'

if __name__ == '__main__':
	app.run(debug=True)
