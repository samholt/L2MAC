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
	event = Event(**request.json)
	DB['events'].append(event)
	return jsonify(event), 201

@app.route('/event/<int:event_id>', methods=['PUT'])
def update_event(event_id):
	for event in DB['events']:
		if event.id == event_id:
			event.type = request.json.get('type', event.type)
			event.date = request.json.get('date', event.date)
			event.time = request.json.get('time', event.time)
			event.theme = request.json.get('theme', event.theme)
			event.color_scheme = request.json.get('color_scheme', event.color_scheme)
			return jsonify(event), 200
	return jsonify({'error': 'Event not found'}), 404

if __name__ == '__main__':
	app.run(debug=True)
