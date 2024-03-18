from flask import Flask, request

app = Flask(__name__)

# Mock database
users_db = {'test@example.com': {'online': True, 'queue': [], 'inbox': []}}
groups_db = {}

# Mock encryption and decryption function
def mock_cipher_suite(text, operation):
	return text[::-1] if operation == 'encrypt' else text[::-1]

@app.route('/user', methods=['POST'])
def create_user():
	data = request.get_json()
	users_db[data['email']] = {'password': data['password'], 'online': data['online'], 'queue': [], 'inbox': []}
	return {'message': 'User created successfully'}, 201

@app.route('/user/<email>', methods=['GET'])
def get_user(email):
	if email not in users_db:
		return {'message': 'User not found'}, 404
	user = users_db[email]
	return {'online': user['online'], 'inbox': user['inbox'], 'queue': user['queue']}, 200

@app.route('/user/<email>/online', methods=['POST'])
def set_online(email):
	data = request.get_json()
	if email not in users_db:
		return {'message': 'User not found'}, 404
	users_db[email]['online'] = data['online']
	if data['online']:
		for message in users_db[email]['queue']:
			users_db[email]['inbox'].append(message)
		users_db[email]['queue'] = []
	return {'message': 'User online status updated successfully'}, 200

@app.route('/user/<email>/status', methods=['POST'])
def post_status(email):
	data = request.get_json()
	if email not in users_db:
		return {'message': 'User not found'}, 404
	if users_db[email]['online']:
		users_db[email]['status'] = {'image': data['image'], 'duration': data['duration'], 'visibility': data['visibility']}
	else:
		users_db[email]['queue'].append({'image': data['image'], 'duration': data['duration'], 'visibility': data['visibility']})
	return {'message': 'Status posted successfully'}, 200
