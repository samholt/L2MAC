from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

users = {}
groups = {}
message_queue = {}

@app.route('/')
def home():
	return render_template('index.html')

@app.route('/signup', methods=['POST'])
def signup():
	user_id = str(len(users) + 1)
	user_data = request.get_json()
	user_data['blocked_contacts'] = []
	user_data['groups'] = {}
	user_data['messages'] = []
	user_data['images'] = []
	user_data['statuses'] = []
	user_data['online'] = False
	users[user_id] = user_data
	return jsonify({'user_id': user_id}), 201

@app.route('/post_status', methods=['POST'])
def post_status():
	user_id = request.args.get('user_id')
	status_data = request.get_json()
	if user_id in users:
		users[user_id]['statuses'].append(status_data)
		return jsonify({'message': 'Status posted'}), 200
	else:
		return jsonify({'error': 'User not found'}), 404

@app.route('/view_status', methods=['GET'])
def view_status():
	user_id = request.args.get('user_id')
	if user_id in users:
		return jsonify({'statuses': users[user_id]['statuses']}), 200
	else:
		return jsonify({'error': 'User not found'}), 404

@app.route('/update_status', methods=['POST'])
def update_status():
	user_id = request.args.get('user_id')
	status = request.get_json().get('status')
	if user_id in users:
		users[user_id]['online'] = status
		if status and user_id in message_queue:
			users[user_id]['messages'].extend(message_queue[user_id])
			message_queue.pop(user_id)
		return jsonify({'message': 'Status updated'}), 200
	else:
		return jsonify({'error': 'User not found'}), 404

@app.route('/send_message', methods=['POST'])
def send_message():
	sender_id = request.args.get('sender_id')
	receiver_id = request.args.get('receiver_id')
	message = request.get_json().get('message')
	if sender_id not in users:
		return jsonify({'error': 'Sender not found'}), 404
	if receiver_id in users:
		if users[receiver_id]['online']:
			users[receiver_id]['messages'].append({'from': sender_id, 'message': message})
		else:
			if receiver_id not in message_queue:
				message_queue[receiver_id] = []
			message_queue[receiver_id].append({'from': sender_id, 'message': message})
		return jsonify({'message': 'Message sent'}), 200
	else:
		return jsonify({'error': 'Receiver not found'}), 404
