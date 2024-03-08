import pytest
from statistics import Statistics


def test_monitor_user_engagement():
	stats = Statistics()
	stats.monitor_user_engagement('user1', 10)
	assert stats.get_user_engagement()['user1'] == 10


def test_monitor_site_usage():
	stats = Statistics()
	stats.monitor_site_usage({'visits': 1000, 'page_views': 5000})
	assert stats.get_site_usage()['visits'] == 1000
	assert stats.get_site_usage()['page_views'] == 5000
