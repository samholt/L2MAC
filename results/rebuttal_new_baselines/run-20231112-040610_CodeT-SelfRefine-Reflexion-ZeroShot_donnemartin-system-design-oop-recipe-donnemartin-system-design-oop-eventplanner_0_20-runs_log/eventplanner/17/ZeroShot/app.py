from flask import Flask, request, jsonify
from dataclasses import dataclass
from typing import List

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

@dataclass
class Vendor:
	id: int
	name: str
	type: str
	reviews: List[str]

@app.route('/event', methods=['POST'])
def create_event():
	data = request.get_json()
	event = Event(**data)
	DB['events'].append(event)
	return jsonify({'message': 'Event created'}), 201

@app.route('/event/<int:event_id>', methods=['PUT'])
def update_event(event_id):
	data = request.get_json()
	for event in DB['events']:
		if event.id == event_id:
			event.type = data.get('type', event.type)
			event.date = data.get('date', event.date)
			event.time = data.get('time', event.time)
			event.theme = data.get('theme', event.theme)
			event.color_scheme = data.get('color_scheme', event.color_scheme)
			return jsonify({'message': 'Event updated'}), 200
	return jsonify({'message': 'Event not found'}), 404

if __name__ == '__main__':
	app.run(debug=True)
