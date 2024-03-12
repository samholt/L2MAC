from flask import Flask, request

app = Flask(__name__)

# Mock database
users = {}

@app.route('/')
def home():
	return 'Hello, World!'

@app.route('/webapp', methods=['GET'])
def webapp():
	return 'Welcome to the web application!'

@app.route('/status/<username>', methods=['GET'])
def status(username):
	if username in users:
		return {'status': users[username]['status']}
	else:
		return {'error': 'User not found'}, 404

@app.route('/message/<username>', methods=['POST'])
def message(username):
	if username in users:
		message = request.json.get('message')
		if users[username]['status'] == 'offline':
			users[username]['messages'].append(message)
		return {'status': 'Message sent'}
	else:
		return {'error': 'User not found'}, 404

if __name__ == '__main__':
	app.run(debug=True)
