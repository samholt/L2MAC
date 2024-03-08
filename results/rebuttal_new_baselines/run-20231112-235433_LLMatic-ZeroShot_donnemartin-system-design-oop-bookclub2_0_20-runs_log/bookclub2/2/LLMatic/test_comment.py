import pytest
from comment import Comment

def test_comment():
	comment = Comment(1, 'This is a comment', 'User1')
	assert comment.get_comment_info() == {'id': 1, 'content': 'This is a comment', 'user': 'User1'}

	comment.edit_comment('This is an edited comment')
	assert comment.get_comment_info() == {'id': 1, 'content': 'This is an edited comment', 'user': 'User1'}

	comment.create_comment(2, 'This is a new comment', 'User2')
	assert comment.get_comment_info() == {'id': 2, 'content': 'This is a new comment', 'user': 'User2'}
