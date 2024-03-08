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
	event = Event(**data)
	DB[event.id] = event
	return jsonify(data), 201

@app.route('/event/<int:event_id>', methods=['PUT'])
def update_event(event_id):
	data = request.get_json()
	event = DB.get(event_id)
	if event:
		for key, value in data.items():
			setattr(event, key, value)
		return jsonify(data), 200
	else:
		return {'message': 'Event not found'}, 404

if __name__ == '__main__':
	app.run(debug=True)
