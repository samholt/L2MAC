from discussion import Discussion

def test_discussion():
	discussion = Discussion()
	discussion.create_discussion('1', 'Test discussion')
	assert discussion.get_discussion('1') == 'Test discussion'
	discussion.update_discussion('1', 'Updated discussion')
	assert discussion.get_discussion('1') == 'Updated discussion'
	discussion.delete_discussion('1')
	assert discussion.get_discussion('1') is None
