from datetime import datetime
from uuid import uuid4
from app import db

class Post(db.Model):
	id = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid4()))
	user_email = db.Column(db.String(120), nullable=False)
	content = db.Column(db.Text, nullable=False)
	image_url = db.Column(db.String(500), nullable=True)
	created_at = db.Column(db.DateTime, default=datetime.now)

	def to_dict(self):
		return {key: value for key, value in self.__dict__.items()}
