from flask import Flask, request
from dataclasses import dataclass
from typing import Dict

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

@app.route('/event', methods=['POST'])
def create_event():
	data = request.get_json()
	event = Event(**data)
	DB[event.id] = event
	return {'message': 'Event created successfully'}, 201

@app.route('/event/<int:event_id>', methods=['PUT'])
def update_event(event_id):
	data = request.get_json()
	event = Event(**data)
	DB[event.id] = event
	return {'message': 'Event updated successfully'}, 200

if __name__ == '__main__':
	app.run(debug=True)
