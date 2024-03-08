from dataclasses import dataclass

@dataclass
class User:
	id: int
	name: str
	email: str
	books_read: list
	clubs_joined: list
	interests: list

@dataclass
class Club:
	id: int
	name: str
	description: str
	members: list
	books: list
	meetings: list
	is_private: bool

@dataclass
class Book:
	id: int
	title: str
	author: str
	summary: str
	votes: int

