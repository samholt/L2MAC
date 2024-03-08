import pytest
from models.user import User
from models.book import Book
from recommendation_engine import RecommendationEngine


def test_recommendation_engine():
	users = [User(i, f'User {i}', f'user{i}@example.com', 'password', books=list(range(i))) for i in range(10)]
	books = [Book(i, f'Book {i}', 'Author') for i in range(20)]

	engine = RecommendationEngine(users, books)

	for user in users:
		recommendations = engine.recommend_books(user)
		assert all(book.id not in user.books for book in recommendations), 'Recommended a book that the user has already read.'
		assert len(recommendations) <= 5, 'Recommended more than 5 books.'
