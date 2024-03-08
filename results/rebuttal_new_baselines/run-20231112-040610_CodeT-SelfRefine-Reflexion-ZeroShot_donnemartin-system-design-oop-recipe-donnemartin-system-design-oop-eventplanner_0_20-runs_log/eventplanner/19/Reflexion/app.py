from flask import Flask, request
from dataclasses import dataclass

app = Flask(__name__)

# Mock database
DB = {
	'events': [],
	'venues': [],
	'guests': [],
	'vendors': []
}

@dataclass
class Event:
	id: int
	type: str
	date: str
	time: str

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
	service: str

@app.route('/events', methods=['POST'])
def create_event():
	event = Event(**request.json)
	DB['events'].append(event)
	return {'id': event.id}, 201

@app.route('/venues', methods=['POST'])
def create_venue():
	venue = Venue(**request.json)
	DB['venues'].append(venue)
	return {'id': venue.id}, 201

@app.route('/guests', methods=['POST'])
def create_guest():
	guest = Guest(**request.json)
	DB['guests'].append(guest)
	return {'id': guest.id}, 201

@app.route('/vendors', methods=['POST'])
def create_vendor():
	vendor = Vendor(**request.json)
	DB['vendors'].append(vendor)
	return {'id': vendor.id}, 201

if __name__ == '__main__':
	app.run(debug=True)
