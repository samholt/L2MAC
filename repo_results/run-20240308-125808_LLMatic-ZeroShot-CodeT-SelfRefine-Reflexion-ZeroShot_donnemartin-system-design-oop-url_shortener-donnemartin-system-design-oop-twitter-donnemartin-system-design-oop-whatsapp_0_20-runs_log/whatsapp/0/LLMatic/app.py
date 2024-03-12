from flask import Flask, jsonify, request, render_template

app = Flask(__name__)

users = {}
groups = {}
messages = {}
queue = {}

@app.route('/')
def home():
	return render_template('chat.html')

@app.route('/user/<email>/status', methods=['POST'])
def update_status(email):
	status = request.json.get('status')
	if email in users:
		users[email]['online'] = status
		if status == 'online':
			# send queued messages
			if email in queue:
				messages[email] = messages.get(email, []) + queue[email]
				del queue[email]
		return jsonify({'status': 'success'}), 200
	else:
		return jsonify({'status': 'failure', 'message': 'User not found'}), 404

@app.route('/message', methods=['POST'])
def send_message():
	message = request.json.get('message')
	receiver = request.json.get('receiver')
	if receiver in users:
		if users[receiver]['online'] == 'online':
			messages[receiver] = messages.get(receiver, []) + [message]
			if receiver in queue:
				del queue[receiver]
		else:
			queue[receiver] = queue.get(receiver, []) + [message]
		return jsonify({'status': 'success'}), 200
	else:
		return jsonify({'status': 'failure', 'message': 'Receiver not found'}), 404

if __name__ == '__main__':
	app.run(debug=True)
