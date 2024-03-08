from comment import Comment

def test_comment():
	comment = Comment()
	comment.post_comment('1', 'Test comment')
	assert comment.get_comment('1') == 'Test comment'
	comment.update_comment('1', 'Updated comment')
	assert comment.get_comment('1') == 'Updated comment'
	comment.delete_comment('1')
	assert comment.get_comment('1') is None
