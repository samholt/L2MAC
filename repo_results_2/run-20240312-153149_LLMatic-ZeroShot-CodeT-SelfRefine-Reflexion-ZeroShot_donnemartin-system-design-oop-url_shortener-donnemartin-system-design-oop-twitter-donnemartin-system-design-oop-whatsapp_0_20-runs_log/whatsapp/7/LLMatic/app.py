from flask import Flask, request, jsonify
import datetime

app = Flask(__name__)

# Mock database
users = {}
statuses = {}

@app.route('/register', methods=['POST'])
def register():
	data = request.get_json()
	username = data['username']
	if username in users:
		return jsonify({'message': 'Username already exists'}), 400
	users[username] = {'friends': [], 'statuses': [], 'online': False, 'message_queue': []}
	return jsonify({'message': 'User registered successfully'}), 200

@app.route('/add_friend', methods=['POST'])
def add_friend():
	data = request.get_json()
	username = data['username']
	friend_username = data['friend_username']
	if username not in users or friend_username not in users:
		return jsonify({'message': 'User not found'}), 404
	if friend_username not in users[username]['friends']:
		users[username]['friends'].append(friend_username)
		message = f'{username} added you as a friend.'
		if not users[friend_username]['online'] and message not in users[friend_username]['message_queue']:
			users[friend_username]['message_queue'].append(message)
	return jsonify({'message': 'Friend added successfully'}), 200

@app.route('/post_status', methods=['POST'])
def post_status():
	data = request.get_json()
	username = data['username']
	image_url = data['image_url']
	visibility = data['visibility']
	if username not in users:
		return jsonify({'message': 'User not found'}), 404
	status_id = len(statuses) + 1
	statuses[status_id] = {'username': username, 'image_url': image_url, 'visibility': visibility, 'timestamp': datetime.datetime.now().isoformat()}
	if status_id not in users[username]['statuses']:
		users[username]['statuses'].append(status_id)
		message = f'{username} posted a new status.'
		for friend in users[username]['friends']:
			if not users[friend]['online'] and message not in users[friend]['message_queue']:
				users[friend]['message_queue'].append(message)
	return jsonify({'message': 'Status posted successfully'}), 200

@app.route('/get_statuses', methods=['GET'])
def get_statuses():
	username = request.args.get('username')
	if username not in users:
		return jsonify({'message': 'User not found'}), 404
	user_statuses = [statuses[id] for id in users[username]['statuses'] if (datetime.datetime.now() - datetime.datetime.fromisoformat(statuses[id]['timestamp'])).total_seconds() <= 86400]
	friend_statuses = [statuses[id] for friend in users[username]['friends'] for id in users[friend]['statuses'] if (datetime.datetime.now() - datetime.datetime.fromisoformat(statuses[id]['timestamp'])).total_seconds() <= 86400 and statuses[id]['visibility'] == 'friends']
	return jsonify({'user_statuses': user_statuses, 'friend_statuses': friend_statuses}), 200

@app.route('/update_status', methods=['POST'])
def update_status():
	data = request.get_json()
	username = data['username']
	online = data['online']
	if username not in users:
		return jsonify({'message': 'User not found'}), 404
	users[username]['online'] = online
	if online:
		messages = users[username]['message_queue']
		users[username]['message_queue'] = []
		return jsonify({'message': 'User is now online', 'messages': messages}), 200
	else:
		return jsonify({'message': 'User is now offline'}), 200

if __name__ == '__main__':
	app.run(debug=True)
