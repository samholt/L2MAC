from flask import Flask, request, jsonify
from dataclasses import dataclass
import sqlite3

app = Flask(__name__)

# Database connection
conn = sqlite3.connect('events.db')
c = conn.cursor()

c.execute('''CREATE TABLE IF NOT EXISTS events
              (id INTEGER PRIMARY KEY, type TEXT, date TEXT, time TEXT, theme TEXT, color_scheme TEXT)''')

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
	try:
		data = request.get_json()
		c.execute("INSERT INTO events (type, date, time, theme, color_scheme) VALUES (?, ?, ?, ?, ?)", (data['type'], data['date'], data['time'], data['theme'], data['color_scheme']))
		conn.commit()
		id = c.lastrowid
		return jsonify({'id': id}), 201
	except Exception as e:
		return jsonify({'error': str(e)}), 500

@app.route('/event/<int:id>', methods=['GET'])
def get_event(id):
	try:
		c.execute("SELECT * FROM events WHERE id=?", (id,))
		event = c.fetchone()
		if not event:
			return jsonify({'error': 'Event not found'}), 404
		return jsonify(dict(zip([column[0] for column in c.description], event))), 200
	except Exception as e:
		return jsonify({'error': str(e)}), 500

@app.route('/event/<int:id>', methods=['PUT'])
def update_event(id):
	try:
		data = request.get_json()
		fields = ', '.join(f'{k} = ?' for k in data.keys())
		values = list(data.values())
		values.append(id)
		c.execute(f"UPDATE events SET {fields} WHERE id=?", values)
		conn.commit()
		c.execute("SELECT * FROM events WHERE id=?", (id,))
		event = c.fetchone()
		return jsonify(dict(zip([column[0] for column in c.description], event))), 200
	except Exception as e:
		return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
	app.run(debug=True)
