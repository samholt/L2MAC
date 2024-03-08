from app import db


class User(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(80), unique=True, nullable=False)
	password = db.Column(db.String(120), nullable=False)


class File(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
	filename = db.Column(db.String(120), nullable=False)
	content = db.Column(db.LargeBinary, nullable=False)


class SharedFile(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	file_id = db.Column(db.Integer, db.ForeignKey('file.id'), nullable=False)
	user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
