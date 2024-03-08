from flask import Flask, request, render_template
import base64

app = Flask(__name__)

# Mock database
users_db = {'test@example.com': {'status': 'offline'}}
groups_db = {}
offline_messages = {}

@app.route('/')
def home():
	return render_template('chat.html')

@app.route('/groups', methods=['POST'])
def create_group():
	data = request.get_json()
	group_name = data['group_name']
	admin_email = data['email']
	participants = data['participants']
	groups_db[group_name] = {'admin': admin_email, 'participants': participants}
	return {'message': 'Group created'}, 201

@app.route('/groups/<group_name>/participants', methods=['POST', 'DELETE'])
def manage_participants(group_name):
	data = request.get_json()
	participant_email = data['participant_email']
	if request.method == 'POST':
		groups_db[group_name]['participants'].append(participant_email)
		return {'message': 'Participant added'}, 200
	elif request.method == 'DELETE':
		groups_db[group_name]['participants'].remove(participant_email)
		return {'message': 'Participant removed'}, 200

@app.route('/groups/<group_name>/admin', methods=['POST'])
def manage_admin(group_name):
	data = request.get_json()
	admin_email = data['admin_email']
	permissions = data['permissions']
	groups_db[group_name]['admin'] = admin_email
	return {'message': 'Admin roles updated'}, 200

@app.route('/users/<email>/status', methods=['POST'])
def update_status(email):
	data = request.get_json()
	status = data['status']
	users_db[email]['status'] = status
	if status == 'online' and email in offline_messages:
		for message in offline_messages[email]:
			# send message
			pass
		offline_messages[email] = []
	return {'message': 'Status updated'}, 200
