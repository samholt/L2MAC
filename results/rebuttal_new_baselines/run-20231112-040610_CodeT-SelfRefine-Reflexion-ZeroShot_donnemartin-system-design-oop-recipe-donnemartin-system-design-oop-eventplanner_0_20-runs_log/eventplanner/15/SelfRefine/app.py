from flask import Flask, request, jsonify
from dataclasses import dataclass
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
db = SQLAlchemy(app)

# Database model
class Event(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	type = db.Column(db.String(50))
	date = db.Column(db.String(10))
	time = db.Column(db.String(5))
	theme = db.Column(db.String(50))
	color_scheme = db.Column(db.String(50))

	def to_dict(self):
		return {c.name: getattr(self, c.name) for c in self.__table__.columns}

@app.route('/event', methods=['POST'])
def create_event():
	data = request.get_json()
	if not all(key in data for key in ['id', 'type', 'date', 'time', 'theme', 'color_scheme']):
		return jsonify({'message': 'Missing fields'}), 400
	event = Event(**data)
	db.session.add(event)
	db.session.commit()
	return jsonify(data), 201

@app.route('/event/<int:event_id>', methods=['PUT'])
def update_event(event_id):
	data = request.get_json()
	event = Event.query.get(event_id)
	if event is None:
		return jsonify({'message': 'Event not found'}), 404
	event.__dict__.update(data)
	db.session.commit()
	return jsonify(event.to_dict()), 200

if __name__ == '__main__':
	app.run(debug=True)
