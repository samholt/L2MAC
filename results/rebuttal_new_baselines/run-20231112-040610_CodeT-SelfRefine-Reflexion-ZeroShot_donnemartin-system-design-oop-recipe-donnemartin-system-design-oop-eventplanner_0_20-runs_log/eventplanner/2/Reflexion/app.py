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
	service: str

@app.route('/event', methods=['POST'])
def create_event():
	event = Event(**request.json)
	DB['event'] = event
	return jsonify(event), 201

@app.route('/event', methods=['GET'])
def get_event():
	event = DB.get('event')
	if event is None:
		return 'No event found', 404
	return jsonify(event), 200

if __name__ == '__main__':
	app.run(debug=True)
