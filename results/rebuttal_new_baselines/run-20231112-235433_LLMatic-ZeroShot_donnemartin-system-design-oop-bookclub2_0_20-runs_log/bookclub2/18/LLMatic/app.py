from flask import Flask, request
from user import User
from book_club import BookClub
from meeting import Meeting
from forum import Forum
from thread import Thread
from comment import Comment
from profile import Profile
from admin import Admin

app = Flask(__name__)

users = {}
book_clubs = {}
meetings = {}
forums = {}
threads = {}
comments = {}
profiles = {}
admins = {}

@app.route('/')
def home():
	return 'Hello, World!'

@app.route('/register', methods=['POST'])
def register():
	data = request.get_json()
	user = User(data['username'], data['password'], data['email'])
	users[user.username] = user
	profiles[user.username] = Profile(user.username)
	return 'User registered successfully', 201

@app.route('/login', methods=['POST'])
def login():
	data = request.get_json()
	user = users.get(data['username'])
	if user and user.authenticate_user(data['username'], data['password']):
		return 'User logged in successfully', 200
	return 'Invalid username or password', 401

@app.route('/book_club', methods=['POST'])
def create_book_club():
	data = request.get_json()
	book_club = BookClub(data['name'], data['privacy_setting'])
	book_clubs[book_club.name] = book_club
	return 'Book club created successfully', 201

@app.route('/meeting', methods=['POST'])
def schedule_meeting():
	data = request.get_json()
	meeting = Meeting(data['date'], data['time'], data['book_club'])
	meetings[meeting.date] = meeting
	return 'Meeting scheduled successfully', 201

@app.route('/forum', methods=['POST'])
def create_forum():
	data = request.get_json()
	forum = Forum(data['book_club'])
	forums[forum.book_club] = forum
	return 'Forum created successfully', 201

@app.route('/thread', methods=['POST'])
def create_thread():
	data = request.get_json()
	thread = Thread(data['title'], data['author'])
	threads[thread.title] = thread
	return 'Thread created successfully', 201

@app.route('/comment', methods=['POST'])
def post_comment():
	data = request.get_json()
	comment = Comment(data['content'], data['author'], data['thread'])
	comments[comment.content] = comment
	return 'Comment posted successfully', 201

@app.route('/profile', methods=['GET'])
def view_profile():
	username = request.args.get('username')
	profile = profiles.get(username)
	if profile:
		return {'followers': [user.username for user in profile.followers], 'reading_list': profile.reading_list}, 200
	return 'Profile not found', 404

@app.route('/admin', methods=['POST'])
def admin_action():
	data = request.get_json()
	admin = admins.get(data['username'])
	if admin:
		if data['action'] == 'moderate_content':
			return admin.moderate_content(data['content']), 200
		elif data['action'] == 'manage_users':
			return admin.manage_users(data['user']), 200
	return 'Admin not found or invalid action', 404

if __name__ == '__main__':
	app.run(debug=True)
