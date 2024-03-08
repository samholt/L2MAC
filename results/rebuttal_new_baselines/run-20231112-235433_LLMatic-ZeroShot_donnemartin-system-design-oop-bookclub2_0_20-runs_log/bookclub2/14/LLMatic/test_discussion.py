import pytest
from discussion import Discussion

def test_discussion_creation():
	book_club = 'Book Club 1'
	book = 'Book 1'
	discussion = Discussion(book_club, book)
	assert discussion.book_club == book_club
	assert discussion.book == book
	assert discussion.get_comments() == []

def test_add_comment():
	discussion = Discussion('Book Club 1', 'Book 1')
	comment = 'This is a comment'
	discussion.add_comment(comment)
	assert discussion.get_comments() == [comment]
