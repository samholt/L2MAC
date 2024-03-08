from models import User, Club, Book

users = {}
clubs = {}
books = {}

# User operations
def create_user(user: User):
	users[user.id] = user

def get_user(user_id: int):
	return users.get(user_id)

def update_user(user: User):
	users[user.id] = user

def delete_user(user_id: int):
	del users[user_id]

# Club operations
def create_club(club: Club):
	clubs[club.id] = club

def get_club(club_id: int):
	return clubs.get(club_id)

def update_club(club: Club):
	clubs[club.id] = club

def delete_club(club_id: int):
	del clubs[club_id]

# Book operations
def create_book(book: Book):
	books[book.id] = book

def get_book(book_id: int):
	return books.get(book_id)

def update_book(book: Book):
	books[book.id] = book

def delete_book(book_id: int):
	del books[book_id]

