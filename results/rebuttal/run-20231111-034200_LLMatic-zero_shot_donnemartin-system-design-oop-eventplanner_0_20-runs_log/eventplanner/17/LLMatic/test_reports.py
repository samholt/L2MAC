from reports import Reports

def test_generate_event_report():
	reports = Reports()
	report = reports.generate_event_report('event1')
	assert report == {'attendees': 100, 'budget_used': 5000, 'vendor_performance': 90}

def test_collect_feedback():
	reports = Reports()
	feedback = reports.collect_feedback('event1', 'Great event!')
	assert feedback == ['Great event!']
