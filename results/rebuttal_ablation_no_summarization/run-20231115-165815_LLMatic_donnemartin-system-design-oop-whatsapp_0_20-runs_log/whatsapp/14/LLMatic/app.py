from flask import Flask, jsonify, request, render_template
import uuid
from cryptography.fernet import Fernet

app = Flask(__name__)

users = {}
messages = {}
statuses = {}
message_queue = {}
key = Fernet.generate_key()
cipher_suite = Fernet(key)

@app.route('/')
def home():
	return render_template('index.html')

@app.route('/status', methods=['POST'])
def status():
	data = request.get_json()
	user_id = data['user_id']
	status = data['status']
	users[user_id]['status'] = status
	return jsonify({'status': 'success'}), 200

@app.route('/message', methods=['POST'])
def message():
	data = request.get_json()
	from_user = data['from']
	to_user = data['to']
	message = data['message']
	if users[to_user]['status'] == 'offline':
		if to_user not in message_queue:
			message_queue[to_user] = []
		message_queue[to_user].append({'from': from_user, 'message': message})
	else:
		messages[to_user] = {'from': from_user, 'message': message}
	return jsonify({'status': 'success'}), 200

if __name__ == '__main__':
	app.run(debug=True)
