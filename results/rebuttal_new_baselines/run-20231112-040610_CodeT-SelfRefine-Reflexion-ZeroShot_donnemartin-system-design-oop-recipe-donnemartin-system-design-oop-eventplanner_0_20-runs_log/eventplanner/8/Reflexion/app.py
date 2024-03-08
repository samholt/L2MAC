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

@app.route('/events', methods=['POST'])
def create_event():
	event_data = request.get_json()
	event = Event(**event_data)
	DATABASE[event.id] = event
	return jsonify(event_data), 201

@app.route('/events/<int:event_id>', methods=['PUT'])
def update_event(event_id):
	event_data = request.get_json()
	if event_id not in DATABASE:
		return jsonify({'message': 'Event not found'}), 404
	DATABASE[event_id] = Event(**event_data)
	return jsonify(event_data), 200

@app.route('/events/<int:event_id>', methods=['GET'])
def get_event(event_id):
	if event_id not in DATABASE:
		return jsonify({'message': 'Event not found'}), 404
	event = DATABASE[event_id]
	return jsonify(event.__dict__), 200

@app.route('/events', methods=['GET'])
def get_all_events():
	return jsonify([event.__dict__ for event in DATABASE.values()]), 200

@app.route('/events/<int:event_id>', methods=['DELETE'])
def delete_event(event_id):
	if event_id not in DATABASE:
		return jsonify({'message': 'Event not found'}), 404
	del DATABASE[event_id]
	return jsonify({'message': 'Event deleted'}), 200

if __name__ == '__main__':
	app.run(debug=True)
