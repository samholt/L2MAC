from flask import Flask, request, render_template

app = Flask(__name__)

# Mock database
users = {}
offline_messages = {}

@app.route('/')
def home():
	return render_template('index.html')

@app.route('/signup', methods=['POST'])
def signup():
	email = request.form.get('email')
	password = request.form.get('password')
	if email not in users:
		users[email] = {'password': password, 'blocked_contacts': [], 'groups': {}, 'messages': [], 'statuses': [], 'online': False}
		return 'User created successfully', 201
	else:
		return 'User already exists', 400

@app.route('/update_status', methods=['POST'])
def update_status():
	user_email = request.form.get('user_email')
	status = request.form.get('status')
	if user_email in users:
		users[user_email]['online'] = status == 'online'
		if status == 'online' and user_email in offline_messages:
			users[user_email]['messages'].extend(offline_messages[user_email])
			offline_messages.pop(user_email)
		return 'Status updated successfully', 200
	else:
		return 'User not found', 404

@app.route('/post_message', methods=['POST'])
def post_message():
	user_email = request.form.get('user_email')
	recipient_email = request.form.get('recipient_email')
	message = request.form.get('message')
	if user_email in users and recipient_email in users:
		if users[recipient_email]['online']:
			users[recipient_email]['messages'].append(message)
		else:
			if recipient_email not in offline_messages:
				offline_messages[recipient_email] = []
			offline_messages[recipient_email].append(message)
		return 'Message sent successfully', 200
	else:
		return 'User not found', 404

if __name__ == '__main__':
	app.run(debug=True)
