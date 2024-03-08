import pytest
import discussion


def test_create_forum_missing_data():
	discussion_obj = discussion.Discussion()
	with pytest.raises(ValueError):
		discussion_obj.create_forum('')


def test_add_comment_missing_data():
	discussion_obj = discussion.Discussion()
	with pytest.raises(ValueError):
		discussion_obj.add_comment('', '', '')


def test_vote_for_next_book_missing_data():
	discussion_obj = discussion.Discussion()
	with pytest.raises(ValueError):
		discussion_obj.vote_for_next_book('', '', '')
