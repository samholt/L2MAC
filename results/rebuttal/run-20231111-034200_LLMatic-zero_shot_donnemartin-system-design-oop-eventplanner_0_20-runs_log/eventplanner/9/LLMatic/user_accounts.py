from flask import Flask, request
from database import Database
from datetime import datetime

app = Flask(__name__)
db = Database()

@app.route('/create_profile', methods=['POST'])
def create_profile():
	data = request.get_json()
	return {'id': db.insert('profiles', data)}, 201

@app.route('/customize_profile/<int:id>', methods=['PUT'])
def customize_profile(id):
	data = request.get_json()
	if db.update('profiles', id, data):
		return {}, 204
	else:
		return {'error': 'Profile not found'}, 404

@app.route('/get_profile/<int:id>', methods=['GET'])
def get_profile(id):
	profile = db.get('profiles', id)
	if profile:
		return profile, 200
	else:
		return {'error': 'Profile not found'}, 404

@app.route('/create_event', methods=['POST'])
def create_event():
	data = request.get_json()
	data['date'] = datetime.strptime(data['date'], '%Y-%m-%dT%H:%M:%S')
	return {'id': db.insert('events', data)}, 201

@app.route('/get_events/<int:id>', methods=['GET'])
def get_events(id):
	events = db.get_all('events')
	user_events = [event for event in events if event['user_id'] == id]
	return {'past_events': [event for event in user_events if event['date'] < datetime.now()],
		'upcoming_events': [event for event in user_events if event['date'] >= datetime.now()]}, 200

if __name__ == '__main__':
	app.run(debug=True)
