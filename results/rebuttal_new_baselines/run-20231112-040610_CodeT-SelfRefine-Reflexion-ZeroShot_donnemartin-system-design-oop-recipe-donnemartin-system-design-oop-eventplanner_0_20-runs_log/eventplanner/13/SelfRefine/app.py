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
	services: List[str]

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

@app.route('/venue', methods=['POST'])
def create_venue():
	data = request.get_json()
	venue = Venue(**data)
	DB['venues'].append(venue)
	return jsonify({'message': 'Venue created'}), 201

@app.route('/venue/<int:venue_id>', methods=['PUT'])
def update_venue(venue_id):
	data = request.get_json()
	for venue in DB['venues']:
		if venue.id == venue_id:
			venue.name = data.get('name', venue.name)
			venue.location = data.get('location', venue.location)
			venue.capacity = data.get('capacity', venue.capacity)
			venue.type = data.get('type', venue.type)
			return jsonify({'message': 'Venue updated'}), 200
	return jsonify({'message': 'Venue not found'}), 404

@app.route('/guest', methods=['POST'])
def create_guest():
	data = request.get_json()
	guest = Guest(**data)
	DB['guests'].append(guest)
	return jsonify({'message': 'Guest created'}), 201

@app.route('/guest/<int:guest_id>', methods=['PUT'])
def update_guest(guest_id):
	data = request.get_json()
	for guest in DB['guests']:
		if guest.id == guest_id:
			guest.name = data.get('name', guest.name)
			guest.email = data.get('email', guest.email)
			return jsonify({'message': 'Guest updated'}), 200
	return jsonify({'message': 'Guest not found'}), 404

@app.route('/vendor', methods=['POST'])
def create_vendor():
	data = request.get_json()
	vendor = Vendor(**data)
	DB['vendors'].append(vendor)
	return jsonify({'message': 'Vendor created'}), 201

@app.route('/vendor/<int:vendor_id>', methods=['PUT'])
def update_vendor(vendor_id):
	data = request.get_json()
	for vendor in DB['vendors']:
		if vendor.id == vendor_id:
			vendor.name = data.get('name', vendor.name)
			vendor.services = data.get('services', vendor.services)
			return jsonify({'message': 'Vendor updated'}), 200
	return jsonify({'message': 'Vendor not found'}), 404

if __name__ == '__main__':
	app.run(debug=True)
