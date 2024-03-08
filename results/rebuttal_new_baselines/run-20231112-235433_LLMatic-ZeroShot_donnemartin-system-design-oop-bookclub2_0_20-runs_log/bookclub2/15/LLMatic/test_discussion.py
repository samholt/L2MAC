import pytest
from discussion import Discussion

def test_create_forum():
	d = Discussion()
	d.create_forum('forum1')
	assert 'forum1' in d.forums

def test_post_comment():
	d = Discussion()
	d.create_forum('forum1')
	d.post_comment('forum1', 'comment1')
	assert 'comment1' in d.comments['forum1']

def test_vote_for_book():
	d = Discussion()
	d.vote_for_book('book1')
	assert 'book1' in d.votes
	assert d.votes['book1'] == 1
