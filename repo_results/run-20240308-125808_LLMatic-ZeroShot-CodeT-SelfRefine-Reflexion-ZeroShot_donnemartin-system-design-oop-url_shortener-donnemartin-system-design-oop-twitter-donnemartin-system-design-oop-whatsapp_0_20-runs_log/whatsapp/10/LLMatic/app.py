from flask import Flask, jsonify, request, render_template

app = Flask(__name__)

users = {}
messages = {}
statuses = {}
queued_messages = {}

@app.route('/', methods=['GET'])
def home():
	return render_template('index.html')

@app.route('/status', methods=['POST'])
def update_status():
	data = request.get_json()
	user_id = data['user_id']
	status = data['status']
	statuses[user_id] = status
	return jsonify({'status': 'success'}), 200

@app.route('/message', methods=['POST'])
def send_message():
	data = request.get_json()
	receiver_id = data['receiver_id']
	message = data['message']
	if statuses.get(receiver_id) == 'offline':
		if receiver_id not in queued_messages:
			queued_messages[receiver_id] = []
		queued_messages[receiver_id].append(message)
		return jsonify({'status': 'queued'}), 200
	else:
		messages[receiver_id] = message
		return jsonify({'status': 'sent'}), 200

if __name__ == '__main__':
	app.run(debug=True)
