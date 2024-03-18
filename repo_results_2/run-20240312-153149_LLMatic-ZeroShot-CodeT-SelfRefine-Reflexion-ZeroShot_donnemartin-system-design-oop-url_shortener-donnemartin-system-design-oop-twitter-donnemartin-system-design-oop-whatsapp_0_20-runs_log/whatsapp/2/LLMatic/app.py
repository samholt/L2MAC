from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

users = {}

groups = {}

statuses = {}

@app.route('/')
def home():
	return render_template('chat.html')

@app.route('/user/<username>', methods=['POST'])
def user(username):
	if request.method == 'POST':
		if username not in users:
			users[username] = {'online': False, 'queue': []}
		users[username]['online'] = request.json.get('online', False)
		return jsonify(users[username])

@app.route('/message/<username>', methods=['POST'])
def message(username):
	if request.method == 'POST':
		if username in users and not users[username]['online']:
			users[username]['queue'].append(request.json.get('message'))
		return jsonify({'status': 'message queued'})

if __name__ == '__main__':
	app.run(debug=True)
