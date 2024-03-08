import pytest
from reporting import Reporting

def test_generate_report():
	reporting = Reporting()
	assert reporting.generate_report('event1', {'attendance': 100, 'satisfaction': 4.5}) == {'attendance': 100, 'satisfaction': 4.5}

def test_collect_feedback():
	reporting = Reporting()
	assert reporting.collect_feedback('event1', {'rating': 4, 'comment': 'Great event!'}) == [{'rating': 4, 'comment': 'Great event!'}]
