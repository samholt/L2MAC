from dataclasses import dataclass

@dataclass
class User:
	id: int
	email: str
	username: str
	password: str
	profile_picture: str
	bio: str
	website_link: str
	location: str
	is_private: bool

@dataclass
class Post:
	id: int
	user_id: int
	content: str
	image: str

@dataclass
class Comment:
	id: int
	post_id: int
	user_id: int
	content: str

@dataclass
class Message:
	id: int
	sender_id: int
	receiver_id: int
	content: str

@dataclass
class Notification:
	id: int
	user_id: int
	content: str
