from flask import Flask, request, jsonify
from dataclasses import dataclass

app = Flask(__name__)

# Mock database
DB = {
	'events': [],
	'venues': [],
	'guests': [],
	'vendors': [],
	'users': [],
	'notifications': [],
	'reports': [],
	'admins': []
}

@dataclass
class Event:
	id: int
	type: str
	date: str
	time: str
	theme: str
	color_scheme: str

@dataclass
class Venue:
	id: int
	location: str
	capacity: int
	type: str

@dataclass
class Guest:
	id: int
	name: str
	email: str
	rsvp: bool

@dataclass
class Vendor:
	id: int
	name: str
	type: str
	reviews: list

@dataclass
class User:
	id: int
	name: str
	email: str
	password: str
	events: list

@dataclass
class Notification:
	id: int
	user_id: int
	message: str

@dataclass
class Report:
	id: int
	event_id: int
	attendance: int
	budget_adherence: float

@dataclass
class Admin:
	id: int
	name: str
	email: str
	password: str

@app.route('/events', methods=['POST'])
def create_event():
	event = Event(**request.json)
	DB['events'].append(event)
	return jsonify(event), 201

@app.route('/events/<int:event_id>', methods=['PUT'])
def update_event(event_id):
	event = next((e for e in DB['events'] if e.id == event_id), None)
	if event is None:
		return jsonify({'error': 'Event not found'}), 404
	for key, value in request.json.items():
		setattr(event, key, value)
	return jsonify(event), 200

@app.route('/events/<int:event_id>', methods=['DELETE'])
def delete_event(event_id):
	event = next((e for e in DB['events'] if e.id == event_id), None)
	if event is None:
		return jsonify({'error': 'Event not found'}), 404
	DB['events'].remove(event)
	return '', 204

if __name__ == '__main__':
	app.run(debug=True)
