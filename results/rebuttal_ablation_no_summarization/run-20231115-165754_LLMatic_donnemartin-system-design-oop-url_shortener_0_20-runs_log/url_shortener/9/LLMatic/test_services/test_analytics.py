from services.analytics import Analytics


def test_record_and_retrieve_click_data():
	analytics = Analytics()
	short_url = 'abc123'
	location = 'USA'
	analytics.record_click(short_url, location)
	click_data = analytics.get_click_data(short_url)
	assert click_data['clicks'] == 1
	assert click_data['click_details'][0]['location'] == location

