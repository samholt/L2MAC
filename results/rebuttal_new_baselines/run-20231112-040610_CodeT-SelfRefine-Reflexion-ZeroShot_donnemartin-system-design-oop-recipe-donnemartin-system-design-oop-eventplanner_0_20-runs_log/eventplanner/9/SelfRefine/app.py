from flask import Flask, request, jsonify
from dataclasses import dataclass

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
	if not all(key in data for key in ['id', 'type', 'date', 'time', 'theme', 'color_scheme']):
		return jsonify({'message': 'Missing required field'}), 400
	event = Event(**data)
	DB[event.id] = event
	return jsonify(data), 201

@app.route('/event/<int:event_id>', methods=['PUT'])
def update_event(event_id):
	data = request.get_json()
	if not all(key in data for key in ['id', 'type', 'date', 'time', 'theme', 'color_scheme']):
		return jsonify({'message': 'Missing required field'}), 400
	if event_id not in DB:
		return jsonify({'message': 'Event not found'}), 404
	event = Event(**data)
	DB[event.id] = event
	return jsonify(data), 200

@app.route('/event/<int:event_id>', methods=['DELETE'])
def delete_event(event_id):
	if event_id not in DB:
		return jsonify({'message': 'Event not found'}), 404
	del DB[event_id]
	return jsonify({'message': 'Event deleted'}), 200

if __name__ == '__main__':
	app.run(debug=True)
