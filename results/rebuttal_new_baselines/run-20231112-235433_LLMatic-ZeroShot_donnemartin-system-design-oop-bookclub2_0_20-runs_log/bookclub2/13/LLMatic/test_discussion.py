import pytest
from discussion import Discussion

def test_discussion_creation():
	topic = 'Test Topic'
	discussion = Discussion(topic)
	assert discussion.topic == topic
	assert discussion.comments == []
	assert discussion.votes == 0

def test_add_comment():
	topic = 'Test Topic'
	discussion = Discussion(topic)
	comment = 'Test Comment'
	discussion.add_comment(comment)
	assert discussion.comments == [comment]

def test_upvote():
	topic = 'Test Topic'
	discussion = Discussion(topic)
	discussion.upvote()
	assert discussion.votes == 1

def test_downvote():
	topic = 'Test Topic'
	discussion = Discussion(topic)
	discussion.downvote()
	assert discussion.votes == -1
