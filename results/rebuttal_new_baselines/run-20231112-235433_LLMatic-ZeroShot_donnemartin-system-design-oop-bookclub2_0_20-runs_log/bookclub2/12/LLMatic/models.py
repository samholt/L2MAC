from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


class User(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(64), index=True, unique=True)
	email = db.Column(db.String(120), index=True, unique=True)
	password_hash = db.Column(db.String(128))
	created_clubs = db.relationship('BookClub', backref='creator', lazy='select')
	role = db.Column(db.String(64), default='member')


class BookClub(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(64), unique=True)
	creator_id = db.Column(db.Integer, db.ForeignKey('user.id'))
	members = db.relationship('User', secondary='bookclub_membership', backref=db.backref('clubs', lazy='dynamic'))
	privacy = db.Column(db.String(64), default='public')


class BookClubMembership(db.Model):
	__tablename__ = 'bookclub_membership'
	user_id = db.Column(db.Integer, db.ForeignKey('user.id'), primary_key=True)
	bookclub_id = db.Column(db.Integer, db.ForeignKey('book_club.id'), primary_key=True)
	role = db.Column(db.String(64), default='member')


class Meeting(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	date = db.Column(db.DateTime)
	time = db.Column(db.Time)
	location = db.Column(db.String(128))
	club_id = db.Column(db.Integer, db.ForeignKey('book_club.id'))


class Discussion(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	title = db.Column(db.String(64))
	content = db.Column(db.String(256))
	club_id = db.Column(db.Integer, db.ForeignKey('book_club.id'))
	user_id = db.Column(db.Integer, db.ForeignKey('user.id'))


class Comment(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	content = db.Column(db.String(256))
	discussion_id = db.Column(db.Integer, db.ForeignKey('discussion.id'))
	user_id = db.Column(db.Integer, db.ForeignKey('user.id'))


class Vote(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	book_id = db.Column(db.Integer)
	club_id = db.Column(db.Integer, db.ForeignKey('book_club.id'))
	user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
