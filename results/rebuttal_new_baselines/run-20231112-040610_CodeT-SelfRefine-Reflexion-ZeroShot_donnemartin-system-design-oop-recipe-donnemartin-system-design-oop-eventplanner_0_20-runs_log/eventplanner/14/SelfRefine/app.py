from flask import Flask, request, jsonify
from dataclasses import dataclass
from typing import List

app = Flask(__name__)

# Mock database
DB = {'events': {}, 'venues': {}, 'guests': {}, 'vendors': {}}

@dataclass
class Event:
	id: str
	type: str
	date: str
	time: str
	theme: str
	color_scheme: str

@dataclass
class Venue:
	id: str
	location: str
	capacity: int
	type: str

@dataclass
class Guest:
	id: str
	name: str
	email: str

@dataclass
class Vendor:
	id: str
	name: str
	type: str
	reviews: List[str]

@app.route('/event', methods=['POST'])
def create_event():
	event = Event(**request.json)
	if event.id in DB['events']:
		return jsonify({'error': 'Event already exists'}), 400
	DB['events'][event.id] = event
	return jsonify(event), 201

@app.route('/event/<event_id>', methods=['PUT'])
def update_event(event_id):
	if event_id not in DB['events']:
		return jsonify({'error': 'Event not found'}), 404
	event = Event(**request.json)
	DB['events'][event_id] = event
	return jsonify(event), 200

@app.route('/venue', methods=['POST'])
def create_venue():
	venue = Venue(**request.json)
	if venue.id in DB['venues']:
		return jsonify({'error': 'Venue already exists'}), 400
	DB['venues'][venue.id] = venue
	return jsonify(venue), 201

@app.route('/guest', methods=['POST'])
def create_guest():
	guest = Guest(**request.json)
	if guest.id in DB['guests']:
		return jsonify({'error': 'Guest already exists'}), 400
	DB['guests'][guest.id] = guest
	return jsonify(guest), 201

@app.route('/vendor', methods=['POST'])
def create_vendor():
	vendor = Vendor(**request.json)
	if vendor.id in DB['vendors']:
		return jsonify({'error': 'Vendor already exists'}), 400
	DB['vendors'][vendor.id] = vendor
	return jsonify(vendor), 201

if __name__ == '__main__':
	app.run(debug=True)
