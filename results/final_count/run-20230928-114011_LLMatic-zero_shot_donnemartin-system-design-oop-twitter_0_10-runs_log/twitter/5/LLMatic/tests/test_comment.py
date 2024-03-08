import pytest
from comment import Comment


def test_comment_creation():
	comment = Comment('author', 'content', 'parent_post')
	assert comment.author == 'author'
	assert comment.content == 'content'
	assert comment.parent_post == 'parent_post'
	assert comment.likes == 0


def test_like():
	comment = Comment('author', 'content', 'parent_post')
	comment.like()
	assert comment.likes == 1


def test_delete():
	comment = Comment('author', 'content', 'parent_post')
	comment.delete()
	assert comment.content == ''
	assert comment.likes == 0
