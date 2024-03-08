from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


class Url(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	original_url = db.Column(db.String(500), nullable=False)
	short_url = db.Column(db.String(80), unique=True, nullable=False)
	custom_url = db.Column(db.String(80), unique=True)
	clicks = db.Column(db.Integer, default=0)
	expires_on = db.Column(db.DateTime)
