from dataclasses import dataclass

@dataclass
class User:
	id: int
	username: str
	following: list

@dataclass
class Tweet:
	id: int
	user_id: int
	content: str
	replies: list
	privacy: str

@dataclass
class DirectMessage:
	id: int
	sender_id: int
	receiver_id: int
	content: str

@dataclass
class Mention:
	id: int
	user_id: int
	tweet_id: int
