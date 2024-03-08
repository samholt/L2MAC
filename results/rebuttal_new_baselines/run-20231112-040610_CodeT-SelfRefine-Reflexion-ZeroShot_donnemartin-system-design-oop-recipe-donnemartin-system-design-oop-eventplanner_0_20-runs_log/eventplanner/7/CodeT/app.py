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
		setattr(event, key, value)
	return jsonify(event.__dict__), 200

if __name__ == '__main__':
	app.run(debug=True)
