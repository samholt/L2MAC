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
	name: str
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
	event = next((e for e in DB['events'] if e.id == event_id), None)
	if event is None:
		return jsonify({'error': 'Event not found'}), 404
	event.type = request.json.get('type', event.type)
	event.date = request.json.get('date', event.date)
	event.time = request.json.get('time', event.time)
	event.theme = request.json.get('theme', event.theme)
	event.color_scheme = request.json.get('color_scheme', event.color_scheme)
	return jsonify(event), 200

@app.route('/venue', methods=['POST'])
def create_venue():
	venue = Venue(**request.json)
	DB['venues'].append(venue)
	return jsonify(venue), 201

@app.route('/venue/<int:venue_id>', methods=['PUT'])
def update_venue(venue_id):
	venue = next((v for v in DB['venues'] if v.id == venue_id), None)
	if venue is None:
		return jsonify({'error': 'Venue not found'}), 404
	venue.name = request.json.get('name', venue.name)
	venue.location = request.json.get('location', venue.location)
	venue.capacity = request.json.get('capacity', venue.capacity)
	venue.type = request.json.get('type', venue.type)
	return jsonify(venue), 200

@app.route('/guest', methods=['POST'])
def create_guest():
	guest = Guest(**request.json)
	DB['guests'].append(guest)
	return jsonify(guest), 201

@app.route('/guest/<int:guest_id>', methods=['PUT'])
def update_guest(guest_id):
	guest = next((g for g in DB['guests'] if g.id == guest_id), None)
	if guest is None:
		return jsonify({'error': 'Guest not found'}), 404
	guest.name = request.json.get('name', guest.name)
	guest.email = request.json.get('email', guest.email)
	return jsonify(guest), 200

@app.route('/vendor', methods=['POST'])
def create_vendor():
	vendor = Vendor(**request.json)
	DB['vendors'].append(vendor)
	return jsonify(vendor), 201

@app.route('/vendor/<int:vendor_id>', methods=['PUT'])
def update_vendor(vendor_id):
	vendor = next((v for v in DB['vendors'] if v.id == vendor_id), None)
	if vendor is None:
		return jsonify({'error': 'Vendor not found'}), 404
	vendor.name = request.json.get('name', vendor.name)
	vendor.type = request.json.get('type', vendor.type)
	vendor.reviews = request.json.get('reviews', vendor.reviews)
	return jsonify(vendor), 200

if __name__ == '__main__':
	app.run(debug=True)
