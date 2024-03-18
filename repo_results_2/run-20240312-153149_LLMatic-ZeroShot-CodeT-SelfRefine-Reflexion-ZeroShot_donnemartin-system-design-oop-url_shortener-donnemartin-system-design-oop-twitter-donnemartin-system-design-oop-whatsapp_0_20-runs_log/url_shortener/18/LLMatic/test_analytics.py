import analytics


def test_update_and_get_analytics():
	url = 'http://test.com'
	location = 'USA'
	analytics.update_url_analytics(url, location)
	result = analytics.get_url_analytics(url)
	assert result['url'] == url
	assert result['clicks'] == 1
	assert result['locations'] == [location]
	assert len(result['click_times']) == 1
