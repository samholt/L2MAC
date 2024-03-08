from flask import Flask, jsonify, request
from werkzeug.security import generate_password_hash, check_password_hash

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
	if not username or not password:
		return jsonify({'message': 'Username and password are required'}), 400
	if username in DATABASE['users']:
		return jsonify({'message': 'Username already exists'}), 400
	DATABASE['users'][username] = generate_password_hash(password)
	return jsonify({'message': 'User registered successfully'}), 200

@app.route('/login', methods=['POST'])
def login():
	data = request.get_json()
	username = data.get('username')
	password = data.get('password')
	if not username or not password:
		return jsonify({'message': 'Username and password are required'}), 400
	if username not in DATABASE['users'] or not check_password_hash(DATABASE['users'][username], password):
		return jsonify({'message': 'Invalid username or password'}), 400
	return jsonify({'message': 'Logged in successfully'}), 200

@app.route('/create_club', methods=['POST'])
def create_club():
	data = request.get_json()
	club_name = data.get('club_name')
	description = data.get('description')
	privacy = data.get('privacy')
	if not club_name or not description or not privacy:
		return jsonify({'message': 'Club name, description and privacy settings are required'}), 400
	if club_name in DATABASE['clubs']:
		return jsonify({'message': 'Club name already exists'}), 400
	DATABASE['clubs'][club_name] = {'description': description, 'privacy': privacy, 'members': {}}
	return jsonify({'message': 'Club created successfully'}), 200

@app.route('/join_club', methods=['POST'])
def join_club():
	data = request.get_json()
	club_name = data.get('club_name')
	username = data.get('username')
	if not club_name or not username:
		return jsonify({'message': 'Club name and username are required'}), 400
	if club_name not in DATABASE['clubs']:
		return jsonify({'message': 'Club does not exist'}), 400
	if username not in DATABASE['users']:
		return jsonify({'message': 'User does not exist'}), 400
	if username in DATABASE['clubs'][club_name]['members']:
		return jsonify({'message': 'User is already a member of this club'}), 400
	DATABASE['clubs'][club_name]['members'][username] = 'member'
	return jsonify({'message': 'User joined the club successfully'}), 200

@app.route('/manage_roles', methods=['POST'])
def manage_roles():
	data = request.get_json()
	club_name = data.get('club_name')
	username = data.get('username')
	role = data.get('role')
	if not club_name or not username or not role:
		return jsonify({'message': 'Club name, username and role are required'}), 400
	if club_name not in DATABASE['clubs']:
		return jsonify({'message': 'Club does not exist'}), 400
	if username not in DATABASE['users']:
		return jsonify({'message': 'User does not exist'}), 400
	if username not in DATABASE['clubs'][club_name]['members']:
		return jsonify({'message': 'User is not a member of this club'}), 400
	DATABASE['clubs'][club_name]['members'][username] = role
	return jsonify({'message': 'Role updated successfully'}), 200

if __name__ == '__main__':
	app.run(debug=True)
