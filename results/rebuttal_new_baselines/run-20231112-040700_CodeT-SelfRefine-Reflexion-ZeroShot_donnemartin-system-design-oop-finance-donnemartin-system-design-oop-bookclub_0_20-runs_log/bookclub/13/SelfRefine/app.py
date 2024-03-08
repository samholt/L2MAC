from flask import Flask, request, jsonify
from dataclasses import dataclass
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
db = SQLAlchemy(app)


class User(db.Model):
	id = db.Column(db.String, primary_key=True)
	name = db.Column(db.String(50))
	email = db.Column(db.String(120))


class Club(db.Model):
	id = db.Column(db.String, primary_key=True)
	name = db.Column(db.String(50))
	description = db.Column(db.String(200))
	is_private = db.Column(db.Boolean)


class Book(db.Model):
	id = db.Column(db.String, primary_key=True)
	title = db.Column(db.String(50))
	author = db.Column(db.String(50))
	summary = db.Column(db.String(200))


class Meeting(db.Model):
	id = db.Column(db.String, primary_key=True)
	club_id = db.Column(db.String(50))
	book_id = db.Column(db.String(50))
	date = db.Column(db.String(50))
	reminder = db.Column(db.Boolean)


class Discussion(db.Model):
	id = db.Column(db.String, primary_key=True)
	club_id = db.Column(db.String(50))
	book_id = db.Column(db.String(50))
	user_id = db.Column(db.String(50))
	message = db.Column(db.String(200))


class Resource(db.Model):
	id = db.Column(db.String, primary_key=True)
	title = db.Column(db.String(50))
	link = db.Column(db.String(200))
	contributor = db.Column(db.String(50))


class UserClub(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	user_id = db.Column(db.String, db.ForeignKey('user.id'))
	club_id = db.Column(db.String, db.ForeignKey('club.id'))


class UserBook(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	user_id = db.Column(db.String, db.ForeignKey('user.id'))
	book_id = db.Column(db.String, db.ForeignKey('book.id'))


@app.route('/users', methods=['POST'])
def create_user():
	data = request.get_json()
	user = User(**data)
	db.session.add(user)
	db.session.commit()
	return jsonify(user), 201

@app.route('/clubs', methods=['POST'])
def create_club():
	data = request.get_json()
	club = Club(**data)
	db.session.add(club)
	db.session.commit()
	return jsonify(club), 201

@app.route('/books', methods=['POST'])
def create_book():
	data = request.get_json()
	book = Book(**data)
	db.session.add(book)
	db.session.commit()
	return jsonify(book), 201

@app.route('/meetings', methods=['POST'])
def create_meeting():
	data = request.get_json()
	meeting = Meeting(**data)
	db.session.add(meeting)
	db.session.commit()
	return jsonify(meeting), 201

@app.route('/discussions', methods=['POST'])
def create_discussion():
	data = request.get_json()
	discussion = Discussion(**data)
	db.session.add(discussion)
	db.session.commit()
	return jsonify(discussion), 201

@app.route('/resources', methods=['POST'])
def create_resource():
	data = request.get_json()
	resource = Resource(**data)
	db.session.add(resource)
	db.session.commit()
	return jsonify(resource), 201

if __name__ == '__main__':
	app.run(debug=True)
