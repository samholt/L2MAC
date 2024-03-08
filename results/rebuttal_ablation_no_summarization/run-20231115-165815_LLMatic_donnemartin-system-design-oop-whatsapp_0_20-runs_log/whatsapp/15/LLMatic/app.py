from flask import Flask, request, render_template
import hashlib
import time

app = Flask(__name__)

# Mock database
users_db = {}
groups_db = {}

@app.route('/')
def home():
	return render_template('index.html')

@app.route('/api/users', methods=['POST'])
def create_user():
	data = request.get_json()
	users_db[data['email']] = {'messages': [], 'read_receipts': {}, 'status': None, 'status_visibility': [], 'contacts': [], 'message_queue': []}
	return {'message': 'User created'}, 201

@app.route('/api/update_status', methods=['POST'])
def update_status():
	data = request.get_json()
	users_db[data['email']]['status'] = data['status']
	if data['status'] == 'online':
		for message in users_db[data['email']]['message_queue']:
			users_db[data['email']]['messages'].append(message)
		users_db[data['email']]['message_queue'] = []
	return {'message': 'Status updated'}, 200

@app.route('/api/add_contact', methods=['POST'])
def add_contact():
	data = request.get_json()
	users_db[data['email']]['contacts'].append(data['contact_email'])
	return {'message': 'Contact added'}, 200

@app.route('/api/send_message', methods=['POST'])
def send_message():
	data = request.get_json()
	message = {'from': data['from_email'], 'to': data['to_email'], 'message': data['message'], 'timestamp': time.time()}
	if users_db[data['to_email']]['status'] == 'offline':
		users_db[data['to_email']]['message_queue'].append(message)
	else:
		users_db[data['from_email']]['messages'].append(message)
		users_db[data['to_email']]['messages'].append(message)
	return {'message': 'Message sent'}, 200

@app.route('/api/create_group', methods=['POST'])
def create_group():
	data = request.get_json()
	groups_db[data['group_name']] = {'members': data['emails'], 'admins': [data['emails'][0]], 'messages': []}
	return {'message': 'Group created'}, 201

@app.route('/api/update_status_visibility', methods=['POST'])
def update_status_visibility():
	data = request.get_json()
	users_db[data['email']]['status_visibility'] = data['status_visibility']
	return {'message': 'Status visibility updated'}, 200

if __name__ == '__main__':
	app.run(port=5001)
