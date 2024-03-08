import pytest
from forum import Forum

def test_create_thread():
	forum = Forum('Book Club', 'Book')
	thread = forum.create_thread('Thread Title', 'Author')
	assert thread == {'title': 'Thread Title', 'author': 'Author', 'comments': []}

def test_add_comment():
	forum = Forum('Book Club', 'Book')
	forum.create_thread('Thread Title', 'Author')
	thread = forum.add_comment('Thread Title', 'Comment', 'Comment Author')
	assert thread == {'title': 'Thread Title', 'author': 'Author', 'comments': [{'comment': 'Comment', 'author': 'Comment Author'}]}
