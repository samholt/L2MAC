import pytest
from forum import Forum


def test_create_thread():
	forum = Forum('1', 'BookClub1')
	thread = forum.create_thread('Thread1', 'Author1')
	assert thread == {'title': 'Thread1', 'author': 'Author1', 'comments': []}


def test_add_comment():
	forum = Forum('1', 'BookClub1')
	forum.create_thread('Thread1', 'Author1')
	thread = forum.add_comment('Thread1', 'Comment1', 'Author2')
	assert thread == {'title': 'Thread1', 'author': 'Author1', 'comments': [{'comment': 'Comment1', 'author': 'Author2'}]}
