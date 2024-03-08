from flask import Flask, request
from database import users_db, messages_db, message_schema

app = Flask(__name__)

@app.route('/message', methods=['POST'])
def message():
	user_email = request.headers.get('Authorization')
	user = users_db.get(user_email)

	if not user:
		return {'message': 'User not found.'}, 404

	data = request.get_json()
	for field in message_schema:
		if field not in data:
			return {'message': f'Missing field: {field}'}, 400

	data['sender_email'] = user_email
	messages_db[data['message_id']] = data

	return {'message': 'Message sent.'}, 201

@app.route('/block', methods=['POST'])
def block():
	user_email = request.headers.get('Authorization')
	user = users_db.get(user_email)

	if not user:
		return {'message': 'User not found.'}, 404

	data = request.get_json()
	blocked_user_email = data.get('blocked_user_email')

	if blocked_user_email not in user.get('blocked_users', []):
		user.setdefault('blocked_users', []).append(blocked_user_email)

	return {'message': 'User blocked.'}, 200

@app.route('/unblock', methods=['POST'])
def unblock():
	user_email = request.headers.get('Authorization')
	user = users_db.get(user_email)

	if not user:
		return {'message': 'User not found.'}, 404

	data = request.get_json()
	unblocked_user_email = data.get('unblocked_user_email')

	if unblocked_user_email in user.get('blocked_users', []):
		user['blocked_users'].remove(unblocked_user_email)

	return {'message': 'User unblocked.'}, 200
