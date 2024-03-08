import pytest
from profile import Profile


def test_follow():
	profile1 = Profile('user1')
	profile2 = Profile('user2')
	profile1.follow('user2')
	assert 'user2' in profile1.followers


def test_add_to_reading_list():
	profile = Profile('user')
	profile.add_to_reading_list('book')
	assert 'book' in profile.reading_list
