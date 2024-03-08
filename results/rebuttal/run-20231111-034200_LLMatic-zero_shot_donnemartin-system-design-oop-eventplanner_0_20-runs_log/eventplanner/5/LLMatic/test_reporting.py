import pytest
from reporting import Reporting


def test_collect_feedback():
	reporting = Reporting()
	reporting.collect_feedback('event1', 'user1', 5)
	assert reporting.feedback == {'event1': {'user1': 5}}


def test_generate_report():
	reporting = Reporting()
	reporting.collect_feedback('event1', 'user1', 5)
	reporting.collect_feedback('event1', 'user2', 4)
	report = reporting.generate_report('event1')
	assert report == {'average_rating': 4.5, 'feedback_count': 2}
