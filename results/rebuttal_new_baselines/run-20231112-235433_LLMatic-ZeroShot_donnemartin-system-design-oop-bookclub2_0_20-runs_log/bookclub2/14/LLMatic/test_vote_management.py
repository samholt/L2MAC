import app

def test_vote_creation():
	# Create a vote
	vote = app.Vote('Club 1', 'Book 1', [])
	app.DATABASE['votes'][vote.book] = vote
	assert app.DATABASE['votes'][vote.book] == vote

	# Test invalid book club
	vote = app.Vote('Invalid Club', 'Book 1', [])
	app.DATABASE['votes'][vote.book] = vote
	assert app.DATABASE['votes'][vote.book] == vote

	# Test invalid book
	vote = app.Vote('Club 1', 'Invalid Book', [])
	app.DATABASE['votes'][vote.book] = vote
	assert app.DATABASE['votes'][vote.book] == vote

def test_vote_counting():
	# Add votes
	vote = app.DATABASE['votes']['Book 1']
	vote.votes.append('User 1')
	vote.votes.append('User 2')
	assert len(vote.votes) == 2

	# Test invalid book
	vote = app.DATABASE['votes'].get('Invalid Book')
	if vote is not None:
		assert len(vote.votes) == 0
	else:
		assert vote is None
