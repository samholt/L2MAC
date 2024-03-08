import pytest
from recommendation import Recommendation
from database import Database
from book import Book
from user import User

def test_recommendation():
	db = Database()
	rec = Recommendation(db)
	user = User(db)
	user.create_user('1', {'books': ['1', '2']})
	book1 = Book('1', 'Book1', 'Author1', 'Description1')
	book1.votes = 5
	book2 = Book('2', 'Book2', 'Author2', 'Description2')
	book2.votes = 4
	book3 = Book('3', 'Book3', 'Author3', 'Description3')
	book3.votes = 3
	db.insert(db.books, '1', book1)
	db.insert(db.books, '2', book2)
	db.insert(db.books, '3', book3)
	recommendations = rec.recommend('1')
	assert len(recommendations) == 1
	assert recommendations[0].id == '3'
