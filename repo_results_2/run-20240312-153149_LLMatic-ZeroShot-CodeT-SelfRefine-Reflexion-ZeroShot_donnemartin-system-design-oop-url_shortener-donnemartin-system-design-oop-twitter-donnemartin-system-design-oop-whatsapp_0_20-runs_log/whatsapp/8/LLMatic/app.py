from flask import Flask, request, render_template
import random
import string
import time

app = Flask(__name__)

# Mock database
users_db = {}
group_chats_db = {}

@app.route('/user', methods=['GET', 'POST'])
def create_user():
	if request.method == 'POST':
		data = dict(request.form)
		data['messages'] = []
		data['group_chats'] = []
		data['statuses'] = []
		data['last_activity'] = time.time()
		data['queue'] = []
		users_db[data.get('email')] = data
		return render_template('post_status.html')
	return render_template('register.html')

@app.route('/status', methods=['GET', 'POST'])
def post_status():
	if request.method == 'POST':
		data = dict(request.form)
		status_id = ''.join(random.choices(string.ascii_uppercase + string.digits, k=10))
		status_data = {'id': status_id, 'content': data.get('content'), 'visibility': data.get('visibility'), 'timestamp': time.time()}
		users_db[data.get('email')]['statuses'].append(status_data)
		users_db[data.get('email')]['last_activity'] = time.time()
		return render_template('manage_visibility.html', status_id=status_id)
	return render_template('post_status.html')

@app.route('/status/visibility', methods=['GET', 'POST'])
def manage_visibility():
	if request.method == 'POST':
		data = dict(request.form)
		status_id = data.get('status_id')
		for status in users_db[data.get('email')]['statuses']:
			if status['id'] == status_id:
				status['visibility'] = data.get('visibility')
				users_db[data.get('email')]['last_activity'] = time.time()
				return render_template('manage_visibility.html', message='Visibility updated', status_id=status_id)
		return render_template('manage_visibility.html', message='Status not found', status_id=status_id)
	return render_template('manage_visibility.html')

@app.route('/check_online', methods=['GET'])
def check_online():
	data = dict(request.args)
	user = users_db.get(data.get('email'))
	if user and time.time() - user['last_activity'] < 300:
		return 'Online'
	return 'Offline'

@app.route('/send_message', methods=['POST'])
def send_message():
	data = dict(request.form)
	user = users_db.get(data.get('email'))
	if user:
		if time.time() - user['last_activity'] < 300:
			# User is online, send the message directly
			user['messages'].append(data.get('message'))
		else:
			# User is offline, add the message to the queue
			user['queue'].append(data.get('message'))
		user['last_activity'] = time.time()
		return 'Message sent'
	return 'User not found'

@app.route('/receive_messages', methods=['GET'])
def receive_messages():
	data = dict(request.args)
	user = users_db.get(data.get('email'))
	if user:
		# Send all queued messages
		messages = user['queue']
		user['queue'] = []
		user['last_activity'] = time.time()
		return {'messages': messages}
	return 'User not found'

if __name__ == '__main__':
	app.run(debug=True)
