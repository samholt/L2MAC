import pytest
from community import Community

def test_show_recent_activity():
	community = Community()
	community.activity_log = [{'user': 'Alice', 'activity': 'Posted a new recipe'}, {'user': 'Bob', 'activity': 'Liked a recipe'}]
	assert community.show_recent_activity('Alice') == [{'user': 'Alice', 'activity': 'Posted a new recipe'}]

def test_share_on_social_media():
	community = Community()
	assert community.share_on_social_media('Pasta', 'Facebook') == 'Sharing Pasta on Facebook'
	assert community.share_on_social_media('Pasta', 'LinkedIn') == 'Invalid platform'
