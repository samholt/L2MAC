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

@app.route('/event', methods=['POST'])
def create_event():
	data = request.get_json()
	event = Event(**data)
	DB[event.id] = event
	return jsonify(data), 201

@app.route('/event/<int:event_id>', methods=['GET'])
def get_event(event_id):
	event = DB.get(event_id)
	if event is None:
		return '', 404
	return jsonify(event), 200

@app.route('/event/<int:event_id>', methods=['PUT'])
def update_event(event_id):
	data = request.get_json()
	event = DB.get(event_id)
	if event is None:
		return '', 404
	event.type = data.get('type', event.type)
	event.date = data.get('date', event.date)
	event.time = data.get('time', event.time)
	event.theme = data.get('theme', event.theme)
	event.color_scheme = data.get('color_scheme', event.color_scheme)
	DB[event_id] = event
	return jsonify(event), 200

if __name__ == '__main__':
	app.run(debug=True)
