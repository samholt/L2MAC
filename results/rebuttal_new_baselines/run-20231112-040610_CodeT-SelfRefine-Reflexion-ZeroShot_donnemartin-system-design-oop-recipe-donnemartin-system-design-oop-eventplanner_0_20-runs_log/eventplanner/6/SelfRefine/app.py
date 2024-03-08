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
	if not all(key in data for key in ['type', 'date', 'time', 'theme', 'color_scheme']):
		return jsonify({'error': 'Missing required field'}), 400
	id = len(DB) + 1
	event = Event(id, **data)
	DB[id] = event
	return jsonify({'id': id}), 201

@app.route('/event/<int:id>', methods=['GET'])
def get_event(id):
	event = DB.get(id)
	if not event:
		return jsonify({'error': 'Event not found'}), 404
	return jsonify(event.__dict__), 200

@app.route('/event/<int:id>', methods=['PUT'])
def update_event(id):
	data = request.get_json()
	event = DB.get(id)
	if not event:
		return jsonify({'error': 'Event not found'}), 404
	for key, value in data.items():
		if hasattr(event, key):
			setattr(event, key, value)
	return jsonify(event.__dict__), 200

@app.route('/event/<int:id>', methods=['DELETE'])
def delete_event(id):
	if id in DB:
		del DB[id]
		return jsonify({'message': 'Event deleted'}), 200
	return jsonify({'error': 'Event not found'}), 404

@app.route('/events', methods=['GET'])
def get_events():
	return jsonify([event.__dict__ for event in DB.values()]), 200

if __name__ == '__main__':
	app.run(debug=True)
