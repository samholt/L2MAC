from dataclasses import dataclass, field
from typing import Optional, List
from datetime import datetime

# Mock database
DATABASE = {}

@dataclass
class User:
	id: int
	username: str
	email: str
	password: str
	profile_picture: Optional[str] = None
	status_message: Optional[str] = None
	privacy_settings: Optional[str] = None
	last_seen: Optional[str] = None
	blocked_contacts: List[int] = field(default_factory=list)
	online: bool = False


@dataclass
class Group:
	id: int
	name: str
	admin: Optional[int]
	members: List[int]

	def set_admin(self, user_id: int):
		self.admin = user_id

	def check_permission(self, user_id: int) -> bool:
		return self.admin == user_id


@dataclass
class Status:
	id: int
	user_id: int
	image: str
	visibility: str
	timestamp: datetime

	def __post_init__(self):
		self.timestamp = datetime.now()

	@classmethod
	def post(cls, user_id: int, image: str, visibility: str):
		status_id = len(DATABASE) + 1
		status = cls(status_id, user_id, image, visibility, datetime.now())
		DATABASE[status_id] = status
		# Broadcasting the status to the visible users is not implemented as it requires a more complex system
		return status

	def set_visibility(self, visibility: str):
		self.visibility = visibility
		DATABASE[self.id] = self
		return self

@dataclass
class Message:
	id: int
	sender_id: int
	receiver_id: int
	content: str
	timestamp: datetime
	queued: bool = True

	def __post_init__(self):
		self.timestamp = datetime.now()

	@classmethod
	def send(cls, sender_id: int, receiver_id: int, content: str):
		message_id = len(DATABASE) + 1
		receiver = DATABASE.get(receiver_id)
		if receiver and receiver.last_seen is None:
			message = cls(message_id, sender_id, receiver_id, content, datetime.now(), True)
		else:
			message = cls(message_id, sender_id, receiver_id, content, datetime.now(), False)
		DATABASE[message_id] = message
		return message

	def receive(self):
		if self.queued:
			self.queued = False
			DATABASE[self.id] = self
			# Broadcasting the message to the receiver user is not implemented as it requires a more complex system
		return self
