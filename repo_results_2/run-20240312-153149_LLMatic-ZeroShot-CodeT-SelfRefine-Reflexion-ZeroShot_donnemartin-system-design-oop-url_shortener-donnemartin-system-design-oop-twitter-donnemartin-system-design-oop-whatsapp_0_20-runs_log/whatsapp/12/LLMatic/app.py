from flask import Flask, request, render_template
import mock_db
from user import User
from contact import Contact
from group import Group
from message import Message
from status import Status

app = Flask(__name__)
db = mock_db.MockDB()

@app.route('/', methods=['GET'])
def home():
	return render_template('chat.html')

@app.route('/user/<email>/online_status', methods=['GET'])
def check_online_status(email):
	user = db.retrieve(email)
	if user:
		return {'online_status': user.last_online}
	else:
		return {'error': 'User not found'}, 404

@app.route('/user/<email>/send_queued_messages', methods=['POST'])
def send_queued_messages(email):
	user = db.retrieve(email)
	if user:
		user.send_queued_messages()
		return {'status': 'success'}, 200
	else:
		return {'error': 'User not found'}, 404

# Existing routes...

if __name__ == '__main__':
	app.run(debug=True)
