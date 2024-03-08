from reporting import Reporting

def test_generate_report():
	reporting = Reporting()
	reporting.generate_report(1, {'success': True})
	assert reporting.get_report(1) == {'success': True}

def test_collect_feedback():
	reporting = Reporting()
	reporting.collect_feedback(1, {'feedback': 'Great event!'})
	assert reporting.get_feedback(1) == {'feedback': 'Great event!'}
