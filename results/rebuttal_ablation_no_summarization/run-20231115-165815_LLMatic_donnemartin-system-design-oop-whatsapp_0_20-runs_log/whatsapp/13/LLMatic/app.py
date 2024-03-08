from flask import Flask, request

app = Flask(__name__)

users = {}

@app.route('/')
def home():
	return 'Hello, World!'

@app.route('/app')
def application():
	return '<html><body><h1>Welcome to the Application!</h1></body></html>'

@app.route('/signup', methods=['POST'])
def signup():
	user_data = request.get_json()
	if 'username' not in user_data or 'password' not in user_data:
		return {'message': 'Invalid request data'}, 400
	user_id = len(users) + 1
	user_data['blocked_contacts'] = []
	user_data['groups'] = []
	user_data['messages'] = []
	user_data['statuses'] = []
	user_data['online'] = False
	users[user_id] = user_data
	return {'user_id': user_id, 'message': 'User created successfully'}, 201

@app.route('/post_status/<int:user_id>', methods=['POST'])
def post_status(user_id):
	if user_id not in users:
		return {'message': 'User not found'}, 404
	status_data = request.get_json()
	if 'id' not in status_data or 'image' not in status_data or 'caption' not in status_data or 'visibility' not in status_data:
		return {'message': 'Invalid request data'}, 400
	users[user_id]['statuses'].append(status_data)
	return {'message': 'Status posted successfully'}, 200

@app.route('/update_status_visibility/<int:user_id>/<int:status_id>', methods=['POST'])
def update_status_visibility(user_id, status_id):
	if user_id not in users:
		return {'message': 'User or status not found'}, 404
	visibility = request.get_json().get('visibility')
	if visibility is None:
		return {'message': 'Invalid request data'}, 400
	for status in users[user_id]['statuses']:
		if status['id'] == status_id:
			status['visibility'] = visibility
			return {'message': 'Status visibility updated successfully'}, 200
	return {'message': 'User or status not found'}, 404

@app.route('/update_online_status/<int:user_id>', methods=['POST'])
def update_online_status(user_id):
	if user_id not in users:
		return {'message': 'User not found'}, 404
	status = request.get_json().get('status')
	if status is None:
		return {'message': 'Invalid request data'}, 400
	users[user_id]['online'] = status
	return {'message': 'Online status updated successfully'}, 200

if __name__ == '__main__':
	app.run(debug=True)
