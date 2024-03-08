from flask import Flask, request

app = Flask(__name__)

# Mock database
notifications_db = {}

@app.route('/notifications', methods=['POST'])

def create_notification():
	data = request.get_json()
	user_id = data['user_id']
	message = data['message']
	
	# Store the notification in the mock database
	notifications_db[user_id] = message
	return {'status': 'Notification created'}, 201

@app.route('/notifications/<user_id>', methods=['GET'])

def get_notification(user_id):
	# Retrieve the notification from the mock database
	message = notifications_db.get(user_id)
	if message:
		return {'user_id': user_id, 'message': message}, 200
	else:
		return {'error': 'Notification not found'}, 404
