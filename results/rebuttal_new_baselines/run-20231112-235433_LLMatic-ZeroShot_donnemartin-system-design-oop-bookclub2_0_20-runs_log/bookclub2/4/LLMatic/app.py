from flask import Flask, request
from models import User, BookClub, Meeting
import time
import threading

app = Flask(__name__)

# Mock database
users = {}
bookclubs = {}

@app.route('/')
def home():
	return 'Hello, World!'

@app.route('/create', methods=['POST'])
def create():
	data = request.get_json()
	user = users.get(data['username'])
	if not user:
		return 'User not found', 404
	bookclub = BookClub(data['name'], data['privacy_setting'], user)
	bookclubs[data['name']] = bookclub
	return 'Book club created', 201

@app.route('/join', methods=['POST'])
def join():
	data = request.get_json()
	user = users.get(data['username'])
	bookclub = bookclubs.get(data['bookclub'])
	if not user or not bookclub:
		return 'User or book club not found', 404
	bookclub.add_member(user)
	return 'User joined book club', 200

@app.route('/update_privacy', methods=['POST'])
def update_privacy():
	data = request.get_json()
	user = users.get(data['username'])
	bookclub = bookclubs.get(data['bookclub'])
	if not user or not bookclub:
		return 'User or book club not found', 404
	if bookclub.creator != user:
		return 'Only the club creator can update the privacy settings', 403
	bookclub.privacy_setting = data['privacy_setting']
	return 'Privacy setting updated', 200

@app.route('/update_role', methods=['POST'])
def update_role():
	data = request.get_json()
	user = users.get(data['username'])
	bookclub = bookclubs.get(data['bookclub'])
	if not user or not bookclub:
		return 'User or book club not found', 404
	if bookclub.creator != user:
		return 'Only the club creator can update member roles', 403
	member = users.get(data['member'])
	if not member or member not in bookclub.members:
		return 'Member not found in the book club', 404
	bookclub.update_member_role(member, data['role'])
	return 'Member role updated', 200

@app.route('/create_meeting', methods=['POST'])
def create_meeting():
	data = request.get_json()
	user = users.get(data['username'])
	bookclub = bookclubs.get(data['bookclub'])
	if not user or not bookclub:
		return 'User or book club not found', 404
	if bookclub.creator != user:
		return 'Only the club creator can create meetings', 403
	meeting = Meeting(data['date'], data['time'], data['location'])
	bookclub.add_meeting(meeting)
	return 'Meeting created', 201

@app.route('/update_meeting', methods=['POST'])
def update_meeting():
	data = request.get_json()
	user = users.get(data['username'])
	bookclub = bookclubs.get(data['bookclub'])
	if not user or not bookclub:
		return 'User or book club not found', 404
	if bookclub.creator != user:
		return 'Only the club creator can update meetings', 403
	meeting = Meeting(data['date'], data['time'], data['location'])
	bookclub.update_meeting(meeting, data['new_date'], data['new_time'], data['new_location'])
	return 'Meeting updated', 200

@app.route('/delete_meeting', methods=['POST'])
def delete_meeting():
	data = request.get_json()
	user = users.get(data['username'])
	bookclub = bookclubs.get(data['bookclub'])
	if not user or not bookclub:
		return 'User or book club not found', 404
	if bookclub.creator != user:
		return 'Only the club creator can delete meetings', 403
	meeting = Meeting(data['date'], data['time'], data['location'])
	bookclub.delete_meeting(meeting)
	return 'Meeting deleted', 200

# Function to send reminders for upcoming meetings

def send_reminders():
	while True:
		for bookclub in bookclubs.values():
			for meeting in bookclub.meetings:
				if not meeting.reminder_sent:
					print(f'Sending reminder for meeting on {meeting.date} at {meeting.time} in {meeting.location} to all members of {bookclub.name}')
					meeting.reminder_sent = True
		time.sleep(60)

# Start the reminder thread
threading.Thread(target=send_reminders).start()

if __name__ == '__main__':
	app.run(debug=True)
