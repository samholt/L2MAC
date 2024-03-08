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
	if not all(key in data for key in ['id', 'type', 'date', 'time', 'theme', 'color_scheme']):
		return jsonify({'message': 'Missing data'}), 400
	event = Event(**data)
	DB['events'].append(event)
	return jsonify({'message': 'Event created'}), 201

@app.route('/venue', methods=['POST'])
def create_venue():
	data = request.get_json()
	if not all(key in data for key in ['id', 'location', 'capacity', 'type']):
		return jsonify({'message': 'Missing data'}), 400
	venue = Venue(**data)
	DB['venues'].append(venue)
	return jsonify({'message': 'Venue created'}), 201

@app.route('/guest', methods=['POST'])
def create_guest():
	data = request.get_json()
	if not all(key in data for key in ['id', 'name', 'email']):
		return jsonify({'message': 'Missing data'}), 400
	guest = Guest(**data)
	DB['guests'].append(guest)
	return jsonify({'message': 'Guest added'}), 201

@app.route('/vendor', methods=['POST'])
def create_vendor():
	data = request.get_json()
	if not all(key in data for key in ['id', 'name', 'type', 'reviews']):
		return jsonify({'message': 'Missing data'}), 400
	vendor = Vendor(**data)
	DB['vendors'].append(vendor)
	return jsonify({'message': 'Vendor added'}), 201

if __name__ == '__main__':
	app.run(debug=True)
