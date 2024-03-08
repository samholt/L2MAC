from flask import Flask, request, send_from_directory
from database import MockDatabase
import uuid
import random
import string
import os

app = Flask(__name__, static_folder='static')
db = MockDatabase()

# existing routes...

@app.route('/send_message', methods=['POST'])
def send_message():
	data = request.get_json()
	message_id = str(uuid.uuid4())
	db.insert_message(message_id, data['sender_id'], data['recipient_id'], data['content'])
	return {'message_id': message_id}, 200

@app.route('/receive_messages', methods=['GET'])
def receive_messages():
	user_id = request.args.get('user_id')
	messages = db.get_offline_messages(user_id)
	db.clear_offline_messages(user_id)
	return {'messages': messages}, 200

if __name__ == '__main__':
	app.run(debug=True)
