from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class URL(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	long_url = db.Column(db.String(500), nullable=False)
	short_url = db.Column(db.String(50), unique=True, nullable=False)
	created_at = db.Column(db.DateTime, default=datetime.utcnow)
	expires_at = db.Column(db.DateTime)
	click_count = db.Column(db.Integer, default=0)
