from flask import Flask, request
from models import User, BookClub, Meeting
import sched, time

app = Flask(__name__)

# Mock database
users = {}
book_clubs = {}

s = sched.scheduler(time.time, time.sleep)

@app.route('/')
def home():
	return 'Hello, World!'

@app.route('/create', methods=['POST'])
def create_book_club():
	data = request.get_json()
	book_club = BookClub(data['name'], data['description'], data.get('privacy', 'public'))
	book_clubs[data['name']] = book_club
	return {'message': 'Book club created successfully'}, 201

@app.route('/join', methods=['POST'])
def join_book_club():
	data = request.get_json()
	user = User(data['username'], data['email'], data['password_hash'], data.get('first_name', ''), data.get('last_name', ''), data.get('bio', ''), data.get('profile_picture', ''))
	book_club = book_clubs.get(data['book_club'])
	if user and book_club:
		if not book_club.members:
			user.role = 'admin'
		book_club.add_member(user)
		users[data['username']] = user
		return {'message': 'Joined book club successfully'}, 200
	else:
		return {'message': 'User or book club not found'}, 404

@app.route('/view_profile', methods=['POST'])
def view_profile():
	data = request.get_json()
	user = users.get(data['username'])
	if user:
		return {'username': user.username, 'email': user.email, 'first_name': user.first_name, 'last_name': user.last_name, 'bio': user.bio, 'profile_picture': user.profile_picture}, 200
	else:
		return {'message': 'User not found'}, 404

@app.route('/edit_profile', methods=['POST'])
def edit_profile():
	data = request.get_json()
	user = users.get(data['username'])
	if user:
		user.first_name = data.get('first_name', user.first_name)
		user.last_name = data.get('last_name', user.last_name)
		user.bio = data.get('bio', user.bio)
		user.profile_picture = data.get('profile_picture', user.profile_picture)
		return {'message': 'Profile updated successfully'}, 200
	else:
		return {'message': 'User not found'}, 404

@app.route('/send_reminders', methods=['POST'])
def send_reminders():
	for book_club in book_clubs.values():
		for meeting in book_club.meetings:
			for member in book_club.members:
				print(f'Sending reminder to {member.email} about meeting on {meeting.date} at {meeting.time}')
	return {'message': 'Reminders sent successfully'}, 200

if __name__ == '__main__':
	app.run(debug=True)
