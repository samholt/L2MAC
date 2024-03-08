from flask import Flask, request, jsonify
from dataclasses import dataclass
from typing import List

app = Flask(__name__)

# Mock database
DB = {'events': [], 'venues': [], 'guests': [], 'vendors': []}

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
	if not all(key in data for key in ('id', 'type', 'date', 'time', 'theme', 'color_scheme')):
		return jsonify({'message': 'Missing fields'}), 400
	event = Event(**data)
	DB['events'].append(event)
	return jsonify({'message': 'Event created'}), 201

@app.route('/event/<int:id>', methods=['GET'])
def get_event(id):
	for event in DB['events']:
		if event.id == id:
			return jsonify(event), 200
	return jsonify({'message': 'Event not found'}), 404

@app.route('/event/<int:id>', methods=['PUT'])
def update_event(id):
	data = request.get_json()
	for event in DB['events']:
		if event.id == id:
			for key, value in data.items():
				setattr(event, key, value)
			return jsonify({'message': 'Event updated'}), 200
	return jsonify({'message': 'Event not found'}), 404

@app.route('/event/<int:id>', methods=['DELETE'])
def delete_event(id):
	for event in DB['events']:
		if event.id == id:
			DB['events'].remove(event)
			return jsonify({'message': 'Event deleted'}), 200
	return jsonify({'message': 'Event not found'}), 404

# Similar endpoints would be created for 'venues', 'guests', and 'vendors'

if __name__ == '__main__':
	app.run(debug=True)
