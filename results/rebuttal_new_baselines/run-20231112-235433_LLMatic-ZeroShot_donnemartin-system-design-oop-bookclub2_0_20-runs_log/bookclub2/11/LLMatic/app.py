from flask import Flask, jsonify, request

app = Flask(__name__)

# Mock database
DATABASE = {
	'users': {},
	'clubs': {},
	'meetings': {},
	'discussions': {},
	'user_profiles': {}
}

@app.route('/')
def home():
	return jsonify({'message': 'Welcome to the application!'}), 200

@app.route('/register', methods=['POST'])
def register():
	data = request.get_json()
	username = data.get('username')
	password = data.get('password')
	if username in DATABASE['users']:
		return jsonify({'message': 'User already exists'}), 400
	DATABASE['users'][username] = {'password': password, 'clubs': []}
	return jsonify({'message': 'User registered successfully'}), 200

@app.route('/login', methods=['POST'])
def login():
	data = request.get_json()
	username = data.get('username')
	password = data.get('password')
	user = DATABASE['users'].get(username)
	if not user or user.get('password') != password:
		return jsonify({'message': 'Invalid username or password'}), 400
	return jsonify({'message': 'Logged in successfully'}), 200

@app.route('/create_club', methods=['POST'])
def create_club():
	data = request.get_json()
	club_name = data.get('club_name')
	privacy_setting = data.get('privacy_setting')
	admin = data.get('admin')
	if club_name in DATABASE['clubs']:
		return jsonify({'message': 'Club already exists'}), 400
	DATABASE['clubs'][club_name] = {'privacy_setting': privacy_setting, 'members': [admin], 'admins': [admin]}
	DATABASE['users'][admin]['clubs'].append(club_name)
	return jsonify({'message': 'Club created successfully'}), 200

@app.route('/join_club', methods=['POST'])
def join_club():
	data = request.get_json()
	club_name = data.get('club_name')
	username = data.get('username')
	club = DATABASE['clubs'].get(club_name)
	if not club or club['privacy_setting'] == 'private':
		return jsonify({'message': 'Cannot join club'}), 400
	club['members'].append(username)
	DATABASE['users'][username]['clubs'].append(club_name)
	return jsonify({'message': 'Joined club successfully'}), 200

@app.route('/manage_roles', methods=['POST'])
def manage_roles():
	data = request.get_json()
	club_name = data.get('club_name')
	username = data.get('username')
	role = data.get('role')
	admin = data.get('admin')
	club = DATABASE['clubs'].get(club_name)
	if not club or admin not in club['admins']:
		return jsonify({'message': 'Cannot manage roles'}), 400
	if role == 'admin':
		club['admins'].append(username)
	else:
		club['members'].append(username)
	return jsonify({'message': 'Role managed successfully'}), 200

@app.route('/schedule_meeting', methods=['POST'])
def schedule_meeting():
	data = request.get_json()
	meeting_id = data.get('meeting_id')
	club_name = data.get('club_name')
	date_time = data.get('date_time')
	attendees = data.get('attendees')
	if meeting_id in DATABASE['meetings']:
		return jsonify({'message': 'Meeting already exists'}), 400
	DATABASE['meetings'][meeting_id] = {'club_name': club_name, 'date_time': date_time, 'attendees': attendees}
	return jsonify({'message': 'Meeting scheduled successfully'}), 200

if __name__ == '__main__':
	app.run(debug=True)
