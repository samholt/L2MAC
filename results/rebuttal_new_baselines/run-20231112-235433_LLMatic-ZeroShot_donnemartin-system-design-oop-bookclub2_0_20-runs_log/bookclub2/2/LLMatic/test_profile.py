import pytest
from profile import Profile

def test_profile():
	profile = Profile('profile1', 'user1')
	assert profile.get_profile_info() == {'profile_id': 'profile1', 'user_id': 'user1', 'reading_list': [], 'recommendations': []}

	profile.add_book_to_reading_list('book1')
	assert profile.get_profile_info() == {'profile_id': 'profile1', 'user_id': 'user1', 'reading_list': ['book1'], 'recommendations': []}

	profile.remove_book_from_reading_list('book1')
	assert profile.get_profile_info() == {'profile_id': 'profile1', 'user_id': 'user1', 'reading_list': [], 'recommendations': []}

	profile.add_recommendation('book2')
	assert profile.get_profile_info() == {'profile_id': 'profile1', 'user_id': 'user1', 'reading_list': [], 'recommendations': ['book2']}

	profile.remove_recommendation('book2')
	assert profile.get_profile_info() == {'profile_id': 'profile1', 'user_id': 'user1', 'reading_list': [], 'recommendations': []}
