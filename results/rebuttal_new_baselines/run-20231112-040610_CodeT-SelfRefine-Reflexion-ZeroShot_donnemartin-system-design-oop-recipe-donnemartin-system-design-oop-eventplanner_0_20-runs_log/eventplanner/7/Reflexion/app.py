from flask import Flask, request
from dataclasses import dataclass

app = Flask(__name__)

# Mock database
DB = {}

@dataclass
class Event:
	id: int
	type: str
	date: str
	time: str
	theme: str
	color_scheme: str

@app.route('/event', methods=['POST'])
def create_event():
	event = Event(**request.json)
	DB[event.id] = event
	return {'message': 'Event created', 'event': event.__dict__}, 201

@app.route('/event/<int:event_id>', methods=['GET'])
def get_event(event_id):
	event = DB.get(event_id)
	if event:
		return {'event': event.__dict__}
	else:
		return {'message': 'Event not found'}, 404

@app.route('/event/<int:event_id>', methods=['DELETE'])
def delete_event(event_id):
	if event_id in DB:
		del DB[event_id]
		return {'message': 'Event deleted'}
	else:
		return {'message': 'Event not found'}, 404

@app.route('/events', methods=['GET'])
def get_events():
	return {'events': [event.__dict__ for event in DB.values()]}
