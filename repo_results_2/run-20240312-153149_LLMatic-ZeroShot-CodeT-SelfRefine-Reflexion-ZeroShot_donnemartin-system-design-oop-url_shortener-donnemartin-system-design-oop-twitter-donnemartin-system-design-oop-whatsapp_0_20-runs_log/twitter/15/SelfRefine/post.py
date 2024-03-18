from dataclasses import dataclass
from database import db
import uuid

@dataclass
class Post(db.Model):
	id: str = db.Column(db.String(36), unique=True, nullable=False, primary_key=True, default=str(uuid.uuid4()))
	user_email: str = db.Column(db.String(120), db.ForeignKey('user.email'), nullable=False)
	content: str = db.Column(db.String(500), nullable=False)
	image: str = db.Column(db.String(120), nullable=True)

	def to_dict(self):
		return {'id': self.id, 'user_email': self.user_email, 'content': self.content, 'image': self.image}
