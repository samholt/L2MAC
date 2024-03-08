from discussion import Discussion

def test_discussion():
	# Create a new discussion
	discussion = Discussion('Book Club 1', 'Discussion 1')
	assert discussion.book_club == 'Book Club 1'
	assert discussion.topic == 'Discussion 1'
	assert discussion.comments == []
	assert discussion.votes == {}

	# Add a comment
	discussion.add_comment('User 1', 'This is a comment.')
	assert discussion.comments == [{'user': 'User 1', 'comment': 'This is a comment.'}]

	# Vote for the next book
	discussion.vote_for_next_book('User 1', 'Book 1')
	assert discussion.votes == {'Book 1': ['User 1']}
