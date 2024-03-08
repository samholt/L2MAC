import pytest
from forum import Forum


def test_create_thread():
	forum = Forum('Book Club')
	thread = forum.create_thread('Discussion on Harry Potter', 'John')
	assert thread['title'] == 'Discussion on Harry Potter'
	assert thread['author'] == 'John'
	assert thread['comments'] == []


def test_add_comment():
	forum = Forum('Book Club')
	forum.create_thread('Discussion on Harry Potter', 'John')
	thread = forum.add_comment('Discussion on Harry Potter', 'I love this book!', 'Jane')
	assert thread['comments'][0]['comment'] == 'I love this book!'
	assert thread['comments'][0]['author'] == 'Jane'
