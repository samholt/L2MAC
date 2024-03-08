from flask import Flask, request, jsonify
from dataclasses import dataclass
from typing import Dict
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
db = SQLAlchemy(app)

@dataclass
class User(db.Model):
	id: db.Column(db.String, primary_key=True)
	name: db.Column(db.String)
	email: db.Column(db.String)

@dataclass
class Club(db.Model):
	id: db.Column(db.String, primary_key=True)
	name: db.Column(db.String)
	description: db.Column(db.String)
	is_private: db.Column(db.Boolean)

@dataclass
class Book(db.Model):
	id: db.Column(db.String, primary_key=True)
	title: db.Column(db.String)
	author: db.Column(db.String)
	description: db.Column(db.String)

@dataclass
class Meeting(db.Model):
	id: db.Column(db.String, primary_key=True)
	club_id: db.Column(db.String, db.ForeignKey('club.id'))
	book_id: db.Column(db.String, db.ForeignKey('book.id'))
	date: db.Column(db.String)
	time: db.Column(db.String)

@dataclass
class Discussion(db.Model):
	id: db.Column(db.String, primary_key=True)
	club_id: db.Column(db.String, db.ForeignKey('club.id'))
	book_id: db.Column(db.String, db.ForeignKey('book.id'))
	user_id: db.Column(db.String, db.ForeignKey('user.id'))
	message: db.Column(db.String)

@dataclass
class Resource(db.Model):
	id: db.Column(db.String, primary_key=True)
	title: db.Column(db.String)
	description: db.Column(db.String)
	link: db.Column(db.String)

@app.route('/user', methods=['POST'])
def create_user():
	data = request.get_json()
	user = User(**data)
	db.session.add(user)
	db.session.commit()
	return jsonify(user), 201

@app.route('/club', methods=['POST'])
def create_club():
	data = request.get_json()
	club = Club(**data)
	db.session.add(club)
	db.session.commit()
	return jsonify(club), 201

@app.route('/book', methods=['POST'])
def create_book():
	data = request.get_json()
	book = Book(**data)
	db.session.add(book)
	db.session.commit()
	return jsonify(book), 201

@app.route('/meeting', methods=['POST'])
def create_meeting():
	data = request.get_json()
	meeting = Meeting(**data)
	db.session.add(meeting)
	db.session.commit()
	return jsonify(meeting), 201

@app.route('/discussion', methods=['POST'])
def create_discussion():
	data = request.get_json()
	discussion = Discussion(**data)
	db.session.add(discussion)
	db.session.commit()
	return jsonify(discussion), 201

@app.route('/resource', methods=['POST'])
def create_resource():
	data = request.get_json()
	resource = Resource(**data)
	db.session.add(resource)
	db.session.commit()
	return jsonify(resource), 201

if __name__ == '__main__':
	app.run(debug=True)
