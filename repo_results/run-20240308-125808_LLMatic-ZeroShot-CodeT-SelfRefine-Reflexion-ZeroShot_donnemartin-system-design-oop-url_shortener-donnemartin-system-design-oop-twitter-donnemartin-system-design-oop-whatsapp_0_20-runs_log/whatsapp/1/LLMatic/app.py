from flask import Flask, request, render_template

app = Flask(__name__)

# Mock database
users = {}

@app.route('/')
def home():
	return render_template('index.html')

@app.route('/status/<username>')
def user_status(username):
	if username in users:
		return {'status': users[username]['status']}
	else:
		return {'error': 'User not found'}, 404

@app.route('/message', methods=['POST'])
def send_message():
	data = request.get_json()
	if data['username'] in users and users[data['username']]['status'] == 'offline':
		users[data['username']]['messages'].append(data['message'])
	return {'status': 'Message queued'}

if __name__ == '__main__':
	app.run(debug=True)
