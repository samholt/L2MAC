from flask import Flask, request, jsonify
from dataclasses import dataclass
import sqlite3

app = Flask(__name__)

@dataclass
class Event:
	id: int
	type: str
	date: str
	time: str
	theme: str
	color_scheme: str

@app.before_first_request
def setup_db():
	with sqlite3.connect('events.db') as conn:
		c = conn.cursor()
		c.execute('''CREATE TABLE IF NOT EXISTS events
			(id INTEGER PRIMARY KEY, type text, date text, time text, theme text, color_scheme text)''')
		conn.commit()

@app.route('/event', methods=['POST'])
def create_event():
	data = request.get_json()
	with sqlite3.connect('events.db') as conn:
		c = conn.cursor()
		c.execute("INSERT INTO events (type, date, time, theme, color_scheme) VALUES (?, ?, ?, ?, ?)", (data['type'], data['date'], data['time'], data['theme'], data['color_scheme']))
		conn.commit()
		id = c.lastrowid
	return jsonify({'id': id}), 201

@app.route('/event/<int:id>', methods=['GET'])
def get_event(id):
	with sqlite3.connect('events.db') as conn:
		c = conn.cursor()
		c.execute('SELECT * FROM events WHERE id=?', (id,))
		event = c.fetchone()
		if not event:
			return jsonify({'error': 'Event not found'}), 404
		return jsonify(dict(zip([column[0] for column in c.description], event))), 200

if __name__ == '__main__':
	app.run(debug=True)
