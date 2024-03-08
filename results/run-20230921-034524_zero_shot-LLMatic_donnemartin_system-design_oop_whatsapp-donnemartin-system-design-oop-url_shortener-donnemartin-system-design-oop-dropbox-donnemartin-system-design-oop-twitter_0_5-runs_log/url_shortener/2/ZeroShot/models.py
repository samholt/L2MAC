from flask_sqlalchemy import SQLAlchemy
from datetime import datetime, timedelta

db = SQLAlchemy()

class URL(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	original_url = db.Column(db.String(500), nullable=False)
	short_url = db.Column(db.String(5), unique=True, nullable=False)
	clicks = db.Column(db.Integer, default=0)
	created_at = db.Column(db.DateTime, default=datetime.utcnow)
	expires_at = db.Column(db.DateTime, default=datetime.utcnow + timedelta(days=30))

	def is_expired(self):
		return datetime.utcnow() > self.expires_at
