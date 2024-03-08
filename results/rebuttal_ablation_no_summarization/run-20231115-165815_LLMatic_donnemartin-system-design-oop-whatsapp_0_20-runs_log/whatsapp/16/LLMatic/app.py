from flask import Flask, request, jsonify, render_template
import uuid
import time

app = Flask(__name__)

# Mock database
users = {}
groups = {}
statuses = {}
messages = {}

@app.route('/create_user', methods=['GET', 'POST'])
def create_user():
	if request.method == 'POST':
		user_id = str(uuid.uuid4())
		users[user_id] = {'email': request.form['email'], 'name': request.form['name'], 'online': False}
		messages[user_id] = []
		return jsonify({'user_id': user_id}), 201
	else:
		return render_template('create_user.html')

@app.route('/create_group', methods=['GET', 'POST'])
def create_group():
	if request.method == 'POST':
		group_id = str(uuid.uuid4())
		groups[group_id] = {'name': request.form['name'], 'picture': request.form['picture'], 'participants': [], 'admins': []}
		return jsonify({'group_id': group_id}), 201
	else:
		return render_template('create_group.html')

@app.route('/add_participant', methods=['GET', 'POST'])
def add_participant():
	if request.method == 'POST':
		group_id = request.form['group_id']
		user_id = request.form['user_id']
		if user_id not in users or group_id not in groups:
			return jsonify({'error': 'Invalid user or group id'}), 400
		groups[group_id]['participants'].append(user_id)
		return jsonify({'message': 'Participant added successfully'}), 200
	else:
		return render_template('add_participant.html')

@app.route('/remove_participant', methods=['GET', 'POST'])
def remove_participant():
	if request.method == 'POST':
		group_id = request.form['group_id']
		user_id = request.form['user_id']
		if user_id not in users or group_id not in groups:
			return jsonify({'error': 'Invalid user or group id'}), 400
		if user_id in groups[group_id]['participants']:
			groups[group_id]['participants'].remove(user_id)
		return jsonify({'message': 'Participant removed successfully'}), 200
	else:
		return render_template('remove_participant.html')

@app.route('/update_admin', methods=['GET', 'POST'])
def update_admin():
	if request.method == 'POST':
		group_id = request.form['group_id']
		user_id = request.form['user_id']
		if user_id not in users or group_id not in groups:
			return jsonify({'error': 'Invalid user or group id'}), 400
		if user_id in groups[group_id]['participants']:
			groups[group_id]['admins'].append(user_id)
		return jsonify({'message': 'Admin updated successfully'}), 200
	else:
		return render_template('update_admin.html')

@app.route('/post_status', methods=['GET', 'POST'])
def post_status():
	if request.method == 'POST':
		user_id = request.form['user_id']
		if user_id not in users:
			return jsonify({'error': 'Invalid user id'}), 400
		status_id = str(uuid.uuid4())
		statuses[status_id] = {'user_id': user_id, 'image': request.form['image'], 'visibility': request.form['visibility'], 'timestamp': time.time()}
		return jsonify({'status_id': status_id}), 201
	else:
		return render_template('post_status.html')

@app.route('/send_message', methods=['POST'])
def send_message():
	from_user_id = request.form['from_user_id']
	to_user_id = request.form['to_user_id']
	message = request.form['message']
	if from_user_id not in users or to_user_id not in users:
		return jsonify({'error': 'Invalid user id'}), 400
	if users[to_user_id]['online']:
		# send message directly
		return jsonify({'message': 'Message sent'}), 200
	else:
		# queue message
		messages[to_user_id].append({'from': from_user_id, 'message': message})
		return jsonify({'message': 'Message queued'}), 200

@app.route('/check_online_status', methods=['GET'])
def check_online_status():
	user_id = request.args.get('user_id')
	if user_id not in users:
		return jsonify({'error': 'Invalid user id'}), 400
	return jsonify({'online': users[user_id]['online']}), 200

@app.route('/update_online_status', methods=['POST'])
def update_online_status():
	user_id = request.form['user_id']
	online = request.form['online'] == 'True'
	if user_id not in users:
		return jsonify({'error': 'Invalid user id'}), 400
	users[user_id]['online'] = online
	if online and messages[user_id]:
		# send queued messages
		queued_messages = messages[user_id]
		messages[user_id] = []
		return jsonify({'message': 'Online status updated, queued messages sent', 'queued_messages': queued_messages}), 200
	else:
		return jsonify({'message': 'Online status updated'}), 200

if __name__ == '__main__':
	app.run(debug=True)
