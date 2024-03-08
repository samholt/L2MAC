from flask import Flask, request, jsonify
from dataclasses import dataclass

app = Flask(__name__)

# Mock database
DB = {
	'events': {},
	'venues': {},
	'guests': {},
	'vendors': {}
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

@app.route('/event', methods=['POST'])
def create_event():
	event = Event(**request.json)
	DB['events'][event.id] = event
	return jsonify(event), 201

@app.route('/event/<int:id>', methods=['GET'])
def get_event(id):
	event = DB['events'].get(id)
	if event is None:
		return '', 404
	return jsonify(event), 200

@app.route('/event/<int:id>', methods=['PUT'])
def update_event(id):
	event = Event(**request.json)
	DB['events'][id] = event
	return jsonify(event), 200

@app.route('/event/<int:id>', methods=['DELETE'])
def delete_event(id):
	if id in DB['events']:
		del DB['events'][id]
		return '', 204
	return '', 404

if __name__ == '__main__':
	app.run(debug=True)
