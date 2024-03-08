from flask import Flask, request
import datetime

app = Flask(__name__)

# Mock database
notifications_db = {}

@app.route('/notifications', methods=['POST'])

def create_notification():
	data = request.get_json()
	user_id = data['user_id']
	event_id = data['event_id']
	message = data['message']
	time = datetime.datetime.now()

	# Store the notification in the database
	notifications_db[user_id] = {'event_id': event_id, 'message': message, 'time': time}

	return {'status': 'Notification created'}, 201

@app.route('/notifications/<user_id>', methods=['GET'])

def get_notifications(user_id):
	# Get the notifications for the user
	if user_id in notifications_db:
		return notifications_db[user_id]
	else:
		return {'status': 'No notifications found for this user'}, 404
