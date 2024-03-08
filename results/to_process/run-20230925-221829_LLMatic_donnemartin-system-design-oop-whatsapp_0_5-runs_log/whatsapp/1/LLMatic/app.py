from flask import Flask, request, jsonify
from user import User
from contact import Contact
from message import Message
from group import Group

app = Flask(__name__)

@app.route('/register', methods=['POST'])
def register():
	data = request.get_json()
	user = User(data['username'], data['password'])
	return jsonify({'message': 'User registered successfully'}), 201

@app.route('/message', methods=['POST'])
def message():
	data = request.get_json()
	message = Message(data['sender'], data['receiver'], data['content'])
	return jsonify({'message': 'Message sent successfully'}), 201

@app.route('/post_status', methods=['POST'])
def post_status():
	data = request.get_json()
	user = User(data['username'], data['password'])
	user.post_status(data['image'], int(data['visibility']))
	return jsonify({'message': 'Status posted successfully'}), 201

if __name__ == '__main__':
	app.run(debug=True)
