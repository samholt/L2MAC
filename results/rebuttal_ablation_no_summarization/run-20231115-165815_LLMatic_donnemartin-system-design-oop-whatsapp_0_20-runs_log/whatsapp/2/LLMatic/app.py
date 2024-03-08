from flask import Flask, request, jsonify
from user import Auth
from message import Message
from group import Group
from status import Status

app = Flask(__name__)

auth = Auth()
status = Status()

@app.route('/signup', methods=['POST'])
def signup():
	data = request.get_json()
	return jsonify(auth.sign_up(data['email'], data['password'])), 200

@app.route('/login', methods=['POST'])
def login():
	data = request.get_json()
	return jsonify(auth.log_in(data['email'], data['password'])), 200

@app.route('/recover', methods=['POST'])
def recover():
	data = request.get_json()
	return jsonify(auth.recover_password(data['email'])), 200

@app.route('/message', methods=['POST'])
def send_message():
	data = request.get_json()
	message = Message(data['sender'], data['receiver'], data['content'])
	return jsonify(message.send_message()), 200

@app.route('/group', methods=['POST'])
def create_group():
	data = request.get_json()
	group = Group(data['name'], data['admin'], data.get('picture'))
	return jsonify({'message': 'Group created successfully'}), 200

@app.route('/status', methods=['POST'])
def post_status():
	data = request.get_json()
	status_id = status.post_status(data['user_id'], data['image'], data['visibility'])
	return jsonify({'status_id': status_id}), 200

if __name__ == '__main__':
	app.run(debug=True)
