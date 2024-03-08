import pytest
from vote import Vote

def test_vote():
	vote = Vote(1, 1, 1)
	assert vote.get_data() == {'id': 1, 'book_id': 1, 'user_id': 1}
	vote.cast(2, 2)
	assert vote.get_data() == {'id': 1, 'book_id': 2, 'user_id': 2}
	vote.update_data(3, 3)
	assert vote.get_data() == {'id': 1, 'book_id': 3, 'user_id': 3}
	vote.delete()
	assert vote.get_data() == {'id': None, 'book_id': None, 'user_id': None}
