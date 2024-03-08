import reporting

def test_generate_report():
	reporting.report_db = {'1': {'feedback': ['Great event!']}}
	assert reporting.generate_report('1') == {'feedback': ['Great event!']}
	assert reporting.generate_report('2') == 'No report found'

def test_collect_feedback():
	reporting.report_db = {}
	reporting.collect_feedback('1', 'Great event!')
	assert reporting.report_db == {'1': {'feedback': ['Great event!']}}
	reporting.collect_feedback('1', 'Awesome!')
	assert reporting.report_db == {'1': {'feedback': ['Great event!', 'Awesome!']}}
