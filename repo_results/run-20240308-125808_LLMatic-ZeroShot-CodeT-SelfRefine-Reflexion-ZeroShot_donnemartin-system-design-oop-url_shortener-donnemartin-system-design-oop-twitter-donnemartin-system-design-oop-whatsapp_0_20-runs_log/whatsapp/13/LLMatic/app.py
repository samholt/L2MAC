from flask import Flask, jsonify, request, render_template
import uuid
import time

app = Flask(__name__)

users = {}

@app.route('/')
def hello_world():
	return render_template('index.html')

@app.route('/signup', methods=['POST'])
def signup():
	data = request.get_json()
	user_id = str(uuid.uuid4())
	users[user_id] = data
	users[user_id]['blocked_contacts'] = []
	users[user_id]['groups'] = {}
	users[user_id]['messages'] = []
	users[user_id]['statuses'] = []
	users[user_id]['online'] = False
	return jsonify({'user_id': user_id}), 201

@app.route('/post_status', methods=['POST'])
def post_status():
	data = request.get_json()
	user_id = data.get('user_id')
	status = data.get('status')
	if user_id in users:
		status_id = str(uuid.uuid4())
		users[user_id]['statuses'].append({'status_id': status_id, 'status': status, 'timestamp': time.time()})
		return jsonify({'status_id': status_id}), 201
	else:
		return jsonify({'message': 'User not found'}), 404

@app.route('/view_status', methods=['POST'])
def view_status():
	data = request.get_json()
	user_id = data.get('user_id')
	status_id = data.get('status_id')
	if user_id in users:
		for status in users[user_id]['statuses']:
			if status['status_id'] == status_id and time.time() - status['timestamp'] <= 86400:
				return jsonify({'status': status['status']}), 200
	return jsonify({'message': 'Status not found or expired'}), 404

@app.route('/update_status', methods=['POST'])
def update_status():
	data = request.get_json()
	user_id = data.get('user_id')
	status = data.get('status')
	if user_id in users:
		users[user_id]['online'] = status
		return jsonify({'message': 'Status updated'}), 200
	else:
		return jsonify({'message': 'User not found'}), 404

if __name__ == '__main__':
	app.run(debug=True)
