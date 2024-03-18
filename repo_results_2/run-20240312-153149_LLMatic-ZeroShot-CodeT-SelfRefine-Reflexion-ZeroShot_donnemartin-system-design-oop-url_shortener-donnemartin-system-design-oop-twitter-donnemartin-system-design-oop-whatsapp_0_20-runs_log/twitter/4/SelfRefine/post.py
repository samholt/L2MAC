from dataclasses import dataclass
from datetime import datetime
import uuid
from app import db

@dataclass
class Post(db.Model):
	id: str = db.Column(db.String, primary_key=True)
	user_email: str = db.Column(db.String)
	content: str = db.Column(db.String)
	image_url: str = db.Column(db.String)
	created_at: datetime = db.Column(db.DateTime)

	def to_dict(self):
		return {
			'id': self.id,
			'user_email': self.user_email,
			'content': self.content,
			'image_url': self.image_url,
			'created_at': self.created_at.isoformat()
		}
