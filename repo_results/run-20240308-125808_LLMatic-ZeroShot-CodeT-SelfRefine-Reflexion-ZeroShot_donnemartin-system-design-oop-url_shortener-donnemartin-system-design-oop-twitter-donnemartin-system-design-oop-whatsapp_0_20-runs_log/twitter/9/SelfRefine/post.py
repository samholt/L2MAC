from dataclasses import dataclass
from database import db
import uuid

@dataclass
class Post(db.Model):
	user_email: str = db.Column(db.String)
	content: str = db.Column(db.String)
	image: str = db.Column(db.String)
	id: str = db.Column(db.String, primary_key=True, default=str(uuid.uuid4()))

	def to_dict(self):
		return {
			'user_email': self.user_email,
			'content': self.content,
			'image': self.image,
			'id': self.id
		}
