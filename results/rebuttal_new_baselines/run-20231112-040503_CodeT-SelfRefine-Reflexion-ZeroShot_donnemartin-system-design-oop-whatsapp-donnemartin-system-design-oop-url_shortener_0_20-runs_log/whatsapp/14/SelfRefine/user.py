from database import db
import uuid


class User(db.Model):
	id = db.Column(db.String, primary_key=True)
	email = db.Column(db.String, unique=True, nullable=False)
	password = db.Column(db.String, nullable=False)
	profile_picture = db.Column(db.String)
	status_message = db.Column(db.String)
	privacy_settings = db.Column(db.PickleType)
	blocked_contacts = db.Column(db.PickleType)
	groups = db.Column(db.PickleType)

	def __init__(self, email, password):
		self.id = str(uuid.uuid4())
		self.email = email
		self.password = password
		self.profile_picture = ''
		self.status_message = ''
		self.privacy_settings = {}
		self.blocked_contacts = []
		self.groups = []

	def to_dict(self):
		return {
			'id': self.id,
			'email': self.email,
			'profile_picture': self.profile_picture,
			'status_message': self.status_message,
			'privacy_settings': self.privacy_settings,
			'blocked_contacts': self.blocked_contacts,
			'groups': self.groups
		}
