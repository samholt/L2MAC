from flask import Flask, request
from database import users_db, posts_db, notifications_db, notification_schema

app = Flask(__name__)

@app.route('/notify', methods=['POST'])
def notify():
	data = request.get_json()
	user_email = data.get('user_email')
	user = users_db.get(user_email)

	if not user:
		return {'message': 'User not found.'}, 404

	for field in notification_schema:
		if field not in data:
			return {'message': f'Missing field: {field}'}, 400

	notifications_db[user_email] = data

	return {'message': 'Notification created.'}, 201

@app.route('/get_notifications', methods=['GET'])
def get_notifications():
	user_email = request.args.get('user_email')
	user = users_db.get(user_email)

	if not user:
		return {'message': 'User not found.'}, 404

	notifications = [notification for notification in notifications_db.values() if notification['user_email'] == user_email]

	return {'notifications': notifications}, 200
