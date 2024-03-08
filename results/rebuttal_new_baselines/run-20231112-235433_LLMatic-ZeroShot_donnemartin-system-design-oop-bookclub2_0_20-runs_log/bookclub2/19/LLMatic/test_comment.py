import pytest
from comment import Comment

def test_create_comment():
	comment = Comment('1', 'This is a comment', 'Author', 'Thread')
	assert comment.id == '1'
	assert comment.content == 'This is a comment'
	assert comment.author == 'Author'
	assert comment.thread == 'Thread'

def test_update_comment():
	comment = Comment('1', 'This is a comment', 'Author', 'Thread')
	comment.update_comment('This is an updated comment')
	assert comment.content == 'This is an updated comment'
