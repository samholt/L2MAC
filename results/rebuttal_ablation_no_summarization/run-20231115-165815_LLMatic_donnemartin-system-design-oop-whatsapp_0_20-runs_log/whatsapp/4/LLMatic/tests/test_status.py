from models.status import Status

def test_status_model():
	status = Status('1', 'user1', 'image1', 'public', '1h')
	assert status.id == '1'
	assert status.user == 'user1'
	assert status.image == 'image1'
	assert status.visibility == 'public'
	assert status.time_limit == '1h'
