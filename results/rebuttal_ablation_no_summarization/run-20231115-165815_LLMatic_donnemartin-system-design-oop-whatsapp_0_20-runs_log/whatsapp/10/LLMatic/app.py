from flask import Flask, request, send_from_directory
import os
import json

app = Flask(__name__, static_folder='static')

# Mock database
users = {}
groups = {}
statuses = {}
messages = {}

@app.route('/<path:path>')
def send_static(path):
	return send_from_directory('static', path)

@app.route('/create_group', methods=['POST'])
def create_group():
	email = request.json['email']
	group_name = request.json['group_name']
	picture = request.json['picture']
	participants = request.json['participants']
	
	if email not in users:
		return json.dumps({'error': 'User does not exist'}), 400
	
	if group_name in groups:
		return json.dumps({'error': 'Group already exists'}), 400
	
	groups[group_name] = {
		'admin': email,
		'picture': picture,
		'participants': participants,
		'admins': [email]
	}
	
	return json.dumps({'success': 'Group created'}), 200

@app.route('/add_participant', methods=['POST'])
def add_participant():
	email = request.json['email']
	group_name = request.json['group_name']
	participant_email = request.json['participant_email']
	
	if email not in users or participant_email not in users:
		return json.dumps({'error': 'User does not exist'}), 400
	
	if group_name not in groups or email not in groups[group_name]['participants']:
		return json.dumps({'error': 'Group does not exist or user not in group'}), 400
	
	groups[group_name]['participants'].append(participant_email)
	
	return json.dumps({'success': 'Participant added'}), 200

@app.route('/remove_participant', methods=['POST'])
def remove_participant():
	email = request.json['email']
	group_name = request.json['group_name']
	participant_email = request.json['participant_email']
	
	if email not in users or participant_email not in users:
		return json.dumps({'error': 'User does not exist'}), 400
	
	if group_name not in groups or email not in groups[group_name]['participants']:
		return json.dumps({'error': 'Group does not exist or user not in group'}), 400
	
	groups[group_name]['participants'].remove(participant_email)
	
	return json.dumps({'success': 'Participant removed'}), 200

@app.route('/manage_admins', methods=['POST'])
def manage_admins():
	email = request.json['email']
	group_name = request.json['group_name']
	admins = request.json['admins']
	
	if email not in users:
		return json.dumps({'error': 'User does not exist'}), 400
	
	if group_name not in groups or email not in groups[group_name]['admins']:
		return json.dumps({'error': 'Group does not exist or user not an admin'}), 400
	
	groups[group_name]['admins'] = admins
	
	return json.dumps({'success': 'Admins updated'}), 200

@app.route('/post_status', methods=['POST'])
def post_status():
	email = request.json['email']
	image = request.json['image']
	timestamp = request.json['timestamp']
	
	if email not in users:
		return json.dumps({'error': 'User does not exist'}), 400
	
	statuses[email] = {
		'image': image,
		'timestamp': timestamp,
		'visible_to': []
	}
	
	return json.dumps({'success': 'Status posted'}), 200

@app.route('/update_status_visibility', methods=['POST'])
def update_status_visibility():
	email = request.json['email']
	status = request.json['status']
	contacts = request.json['contacts']
	
	if email not in users or status not in statuses:
		return json.dumps({'error': 'User or status does not exist'}), 400
	
	statuses[status]['visible_to'] = contacts
	
	return json.dumps({'success': 'Status visibility updated'}), 200

@app.route('/update_online_status', methods=['POST'])
def update_online_status():
	email = request.json['email']
	status = request.json['status']
	
	if email not in users:
		return json.dumps({'error': 'User does not exist'}), 400
	
	users[email]['online'] = status
	
	if status == 'online':
		# Send queued messages
		for message in messages.get(email, []):
			# Here we would send the message
			print(f'Sending message: {message}')
		messages[email] = []
	
	return json.dumps({'success': 'Online status updated'}), 200

if __name__ == '__main__':
	app.run(debug=True)
