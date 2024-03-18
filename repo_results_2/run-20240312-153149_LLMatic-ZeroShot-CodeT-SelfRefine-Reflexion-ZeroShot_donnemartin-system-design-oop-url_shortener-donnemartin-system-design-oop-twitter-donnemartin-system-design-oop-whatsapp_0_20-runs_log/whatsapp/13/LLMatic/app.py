from flask import Flask, request, g, render_template
import mock_db
import time

app = Flask(__name__)

@app.before_request
def before_request():
	if 'db' not in g:
		g.db = mock_db.MockDB()

@app.route('/', methods=['GET'])
def index():
	return render_template('index.html')

@app.route('/send_message', methods=['POST'])
def send_message():
	data = request.get_json()
	if g.db.online:
		g.db.add(data['message_id'], {'text': data['text']})
		return {'status': 'message sent'}, 200
	else:
		g.db.queue_message(data)
		return {'status': 'message queued'}, 200

@app.route('/set_online', methods=['POST'])
def set_online():
	data = request.get_json()
	g.db.set_online(data['online'])
	if g.db.online:
		for message in g.db.message_queue:
			g.db.add(message['message_id'], {'text': message['text']})
		g.db.message_queue = []
	return {'status': 'online status updated'}, 200

if __name__ == '__main__':
	app.run(debug=True)
