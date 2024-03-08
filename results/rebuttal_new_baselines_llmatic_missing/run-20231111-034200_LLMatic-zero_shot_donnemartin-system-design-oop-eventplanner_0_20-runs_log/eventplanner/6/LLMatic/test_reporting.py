import pytest
import reporting
from database import Database


def test_generate_report():
	report = reporting.Report()
	db = Database()
	event_id = 'event1'
	report_data = report.generate_report(event_id)
	db.add_report(event_id, report_data)
	assert db.reports[event_id] == report_data


def test_collect_feedback():
	report = reporting.Report()
	db = Database()
	event_id = 'event1'
	feedback = {'user1': 'Great event!', 'user2': 'Had a lot of fun'}
	collected_feedback = report.collect_feedback(event_id, feedback)
	db.add_report(event_id, collected_feedback)
	assert db.reports[event_id] == collected_feedback
