from recommendation_engine import RecommendationEngine
from mock_db import MockDB
from user import User
from book import Book


def test_recommend_books_based_on_history():
	user = User('Test User', 'test@example.com', 'password', books_to_read=[Book('Test Book', 'Test Author')])
	db = MockDB()
	db.add(db.users, user.email, user)
	engine = RecommendationEngine(db)
	assert engine.recommend_books_based_on_history(user) == user.books_to_read[0]


def test_highlight_popular_books():
	book1 = Book('Test Book 1', 'Test Author', reviews=['Great book!', 'Loved it!'])
	book2 = Book('Test Book 2', 'Test Author', reviews=['Great book!'])
	db = MockDB()
	db.add(db.books, book1.title, book1)
	db.add(db.books, book2.title, book2)
	engine = RecommendationEngine(db)
	assert engine.highlight_popular_books() == book1
