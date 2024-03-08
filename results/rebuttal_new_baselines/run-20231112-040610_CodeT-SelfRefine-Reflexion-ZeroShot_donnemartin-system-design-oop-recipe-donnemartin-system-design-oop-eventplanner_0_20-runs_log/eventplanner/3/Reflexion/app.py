from flask import Flask, request, jsonify
from dataclasses import dataclass

app = Flask(__name__)

# Mock database
DATABASE = {}

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
	DATABASE[event.id] = event
	return jsonify(data), 201

@app.route('/event/<int:event_id>', methods=['GET'])
def get_event(event_id):
	event = DATABASE.get(event_id)
	if event is None:
		return jsonify({'message': 'Event not found'}), 404
	return jsonify(event.__dict__), 200

@app.route('/event/<int:event_id>', methods=['PUT'])
def update_event(event_id):
	data = request.get_json()
	event = DATABASE.get(event_id)
	if event is None:
		return jsonify({'message': 'Event not found'}), 404
	event.__dict__.update(data)
	return jsonify(event.__dict__), 200

@app.route('/event/<int:event_id>', methods=['DELETE'])
def delete_event(event_id):
	event = DATABASE.get(event_id)
	if event is None:
		return jsonify({'message': 'Event not found'}), 404
	del DATABASE[event_id]
	return jsonify({'message': 'Event deleted'}), 200

if __name__ == '__main__':
	app.run(debug=True)
