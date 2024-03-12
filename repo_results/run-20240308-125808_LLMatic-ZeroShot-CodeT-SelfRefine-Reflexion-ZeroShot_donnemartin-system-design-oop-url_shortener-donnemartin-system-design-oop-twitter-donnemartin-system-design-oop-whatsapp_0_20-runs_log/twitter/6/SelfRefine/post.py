from dataclasses import dataclass
from db import db
import uuid

@dataclass
class Post(db.Model):
	id: str = db.Column(db.String, primary_key=True, default=str(uuid.uuid4()))
	user_email: str = db.Column(db.String)
	content: str = db.Column(db.String)
	image: str = db.Column(db.String)

	def to_dict(self):
		return self.__dict__
