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

@app.route('/event', methods=['POST'])
def create_event():
	event_data = request.get_json()
	event = Event(**event_data)
	DB[event.id] = event
	return jsonify(event_data), 201

@app.route('/event/<int:event_id>', methods=['GET'])
def get_event(event_id):
	event = DB.get(event_id)
	if event is None:
		return jsonify({'error': 'Event not found'}), 404
	return jsonify(event.__dict__), 200

if __name__ == '__main__':
	app.run(debug=True)
