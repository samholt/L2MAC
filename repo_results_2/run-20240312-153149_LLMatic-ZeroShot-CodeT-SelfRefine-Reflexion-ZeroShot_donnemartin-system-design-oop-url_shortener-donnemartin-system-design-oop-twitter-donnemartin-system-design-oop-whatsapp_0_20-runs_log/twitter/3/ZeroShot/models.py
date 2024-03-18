from app import db


class User(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(80), unique=True, nullable=False)
	email = db.Column(db.String(120), unique=True, nullable=False)
	password = db.Column(db.String(120), nullable=False)
	bio = db.Column(db.String(280))
	website = db.Column(db.String(120))
	location = db.Column(db.String(120))
	is_private = db.Column(db.Boolean, default=False)


def __repr__(self):
	return '<User %r>' % self.username
