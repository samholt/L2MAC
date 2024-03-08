from dataclasses import dataclass
from typing import List

@dataclass
class User:
	id: int
	username: str
	followers: List[int]
	following: List[int]

@dataclass
class Tweet:
	id: int
	user_id: int
	content: str
	replies: List[int]
	is_private: bool

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
