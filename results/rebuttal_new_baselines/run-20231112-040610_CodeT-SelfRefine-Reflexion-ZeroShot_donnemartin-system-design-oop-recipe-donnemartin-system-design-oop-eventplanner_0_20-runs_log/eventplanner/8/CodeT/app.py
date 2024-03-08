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
	event = Event(id, data['type'], data['date'], data['time'], data['theme'], data['color_scheme'])
	DB[id] = event
	return jsonify({'id': id}), 201

@app.route('/event/<int:id>', methods=['PUT'])
def update_event(id):
	data = request.get_json()
	event = DB.get(id)
	if not event:
		return jsonify({'error': 'Event not found'}), 404
	event.type = data.get('type', event.type)
	event.date = data.get('date', event.date)
	event.time = data.get('time', event.time)
	event.theme = data.get('theme', event.theme)
	event.color_scheme = data.get('color_scheme', event.color_scheme)
	return jsonify({'success': True}), 200

if __name__ == '__main__':
	app.run(debug=True)
