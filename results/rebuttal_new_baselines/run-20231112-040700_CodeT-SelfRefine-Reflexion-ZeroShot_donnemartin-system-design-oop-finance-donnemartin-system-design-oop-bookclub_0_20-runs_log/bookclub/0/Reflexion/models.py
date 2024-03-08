from dataclasses import dataclass, field
from typing import List, Dict

@dataclass
class User:
	id: str
	name: str
	email: str
	clubs: List[str] = field(default_factory=list)
	books_read: List[str] = field(default_factory=list)
	wish_list: List[str] = field(default_factory=list)
	follows: List[str] = field(default_factory=list)

@dataclass
class Club:
	id: str
	name: str
	description: str
	is_private: bool
	members: List[str] = field(default_factory=list)
	books: List[str] = field(default_factory=list)
	meetings: Dict[str, str] = field(default_factory=dict)

@dataclass
class Book:
	id: str
	title: str
	author: str
	summary: str
	reviews: List[str] = field(default_factory=list)

@dataclass
class Meeting:
	id: str
	club_id: str
	book_id: str
	scheduled_time: str

@dataclass
class Review:
	id: str
	book_id: str
	user_id: str
	content: str

