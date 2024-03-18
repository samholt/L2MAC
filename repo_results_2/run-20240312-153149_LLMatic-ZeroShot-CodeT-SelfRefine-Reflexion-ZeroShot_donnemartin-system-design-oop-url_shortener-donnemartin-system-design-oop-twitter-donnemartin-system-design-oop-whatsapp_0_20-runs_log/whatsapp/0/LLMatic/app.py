from flask import Flask, request, render_template

app = Flask(__name__, static_url_path='/static')

# Mock database
DATABASE = {
	'users': {},
	'messages': [],
	'groups': {},
	'statuses': {},
	'profile_pictures': {},
	'privacy_settings': {},
	'blocked_contacts': {},
	'group_members': {},
	'contacts': {}
}

@app.route('/')

def home():
	return render_template('index.html')

@app.route('/update_status', methods=['POST'])

def update_status():
	data = request.get_json()
	user_email = data['email']
	new_status = data['status']
	if user_email in DATABASE['users']:
		DATABASE['users'][user_email]['status'] = new_status
		return {'message': 'Status updated successfully'}, 200
	else:
		return {'message': 'User not found'}, 404

@app.route('/queue_message', methods=['POST'])

def queue_message():
	data = request.get_json()
	message = data['message']
	DATABASE['messages'].append(message)
	return {'message': 'Message queued successfully'}, 200

if __name__ == '__main__':
	app.run(debug=True)
