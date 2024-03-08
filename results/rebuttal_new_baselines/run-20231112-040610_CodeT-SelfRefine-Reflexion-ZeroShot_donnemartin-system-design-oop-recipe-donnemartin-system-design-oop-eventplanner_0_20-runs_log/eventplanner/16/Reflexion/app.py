from flask import Flask, request, jsonify
from dataclasses import dataclass
from typing import List

app = Flask(__name__)

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
	DB['events'].append(event)
	return jsonify(event), 201

@app.route('/venue', methods=['POST'])
def create_venue():
	venue = Venue(**request.json)
	DB['venues'].append(venue)
	return jsonify(venue), 201

@app.route('/guest', methods=['POST'])
def create_guest():
	guest = Guest(**request.json)
	DB['guests'].append(guest)
	return jsonify(guest), 201

@app.route('/vendor', methods=['POST'])
def create_vendor():
	vendor = Vendor(**request.json)
	DB['vendors'].append(vendor)
	return jsonify(vendor), 201

if __name__ == '__main__':
	app.run(debug=True)
