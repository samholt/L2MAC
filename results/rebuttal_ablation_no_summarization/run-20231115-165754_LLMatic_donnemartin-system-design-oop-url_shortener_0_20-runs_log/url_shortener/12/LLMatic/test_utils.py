import utils

# Mock database
utils.click_db = {}

# Test the record_click function
def test_record_click():
	clicks = utils.record_click('test_url', '127.0.0.1', utils.click_db)
	assert 'test_url' in clicks
	assert len(clicks['test_url']) == 1
