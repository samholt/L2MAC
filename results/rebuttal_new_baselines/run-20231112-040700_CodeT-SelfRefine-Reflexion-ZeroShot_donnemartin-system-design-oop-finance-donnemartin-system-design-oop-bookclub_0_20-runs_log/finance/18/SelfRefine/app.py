from flask import Flask, request, jsonify
from dataclasses import dataclass
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
db = SQLAlchemy(app)

# Database models
class User(db.Model):
	id = db.Column(db.String, primary_key=True)
	username = db.Column(db.String, unique=True, nullable=False)
	password = db.Column(db.String, nullable=False)

class Transaction(db.Model):
	id = db.Column(db.String, primary_key=True)
	user_id = db.Column(db.String, db.ForeignKey('user.id'), nullable=False)
	amount = db.Column(db.Float, nullable=False)
	category = db.Column(db.String, nullable=False)

@app.route('/create_user', methods=['POST'])
def create_user():
	try:
		data = request.get_json()
		user = User(**data)
		db.session.add(user)
		db.session.commit()
		return jsonify(user), 201
	except Exception as e:
		return jsonify({'error': str(e)}), 400

@app.route('/add_transaction', methods=['POST'])
def add_transaction():
	try:
		data = request.get_json()
		transaction = Transaction(**data)
		db.session.add(transaction)
		db.session.commit()
		return jsonify(transaction), 201
	except Exception as e:
		return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
	app.run(debug=True)
