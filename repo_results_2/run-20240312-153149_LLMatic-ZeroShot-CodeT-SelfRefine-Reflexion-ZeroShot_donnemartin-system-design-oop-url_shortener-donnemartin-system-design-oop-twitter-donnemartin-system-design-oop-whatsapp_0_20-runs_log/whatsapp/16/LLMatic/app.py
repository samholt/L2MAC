from flask import Flask, request
import hashlib

app = Flask(__name__)

# Mock database
users_db = {}

@app.route('/user', methods=['POST'])
def create_user():
	data = request.get_json()
	data['status'] = 'online'
	data['queue'] = []
	data['messages'] = []
	users_db[data['email']] = data
	return {'message': 'User created successfully'}, 201

@app.route('/user/<email>', methods=['GET'])
def get_user(email):
	user = users_db.get(email)
	if not user:
		return {'message': 'User not found'}, 404
	return user, 200

@app.route('/user/status', methods=['POST'])
def update_status():
	data = request.get_json()
	user = users_db.get(data['email'])
	if not user:
		return {'message': 'User not found'}, 404
	user['status'] = data['status']
	if data['status'] == 'online':
		for message in user['queue']:
			users_db[message['receiver']]['messages'].append(message)
		user['queue'] = []
	return {'message': 'Status updated successfully'}, 200

@app.route('/message/send', methods=['POST'])
def send_message():
	data = request.get_json()
	if data['sender'] not in users_db or data['receiver'] not in users_db:
		return {'message': 'User not found'}, 404
	message = {'sender': data['sender'], 'receiver': data['receiver'], 'message': hashlib.sha256(data['message'].encode()).hexdigest(), 'read': False}
	if users_db[data['receiver']]['status'] == 'offline':
		users_db[data['receiver']]['queue'].append(message)
	else:
		users_db[data['receiver']]['messages'].append(message)
	return {'message': 'Message sent successfully'}, 200

if __name__ == '__main__':
	app.run(debug=True)
