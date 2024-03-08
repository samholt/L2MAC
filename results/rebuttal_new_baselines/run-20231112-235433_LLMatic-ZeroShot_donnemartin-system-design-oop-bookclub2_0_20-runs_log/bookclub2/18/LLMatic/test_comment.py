import pytest
from comment import Comment

def test_comment_upvote_downvote():
	comment = Comment('This is a comment', 'Author', 'Thread')
	assert comment.upvotes == 0
	assert comment.downvotes == 0
	comment.upvote()
	assert comment.upvotes == 1
	comment.downvote()
	assert comment.downvotes == 1
