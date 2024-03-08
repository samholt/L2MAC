from database import db
import uuid


class Chat(db.Model):
	id = db.Column(db.String, primary_key=True)
	name = db.Column(db.String, nullable=False)
	messages = db.Column(db.PickleType)

	def __init__(self, name):
		self.id = str(uuid.uuid4())
		self.name = name
		self.messages = []

	def to_dict(self):
		return {
			'id': self.id,
			'name': self.name,
			'messages': self.messages
		}
