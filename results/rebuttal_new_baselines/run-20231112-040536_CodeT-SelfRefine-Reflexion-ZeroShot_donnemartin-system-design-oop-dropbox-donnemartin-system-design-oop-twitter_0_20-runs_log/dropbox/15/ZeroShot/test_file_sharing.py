import file_sharing

def test_share():
	data = {'file_name': 'new_test.txt', 'expiry_date': '2022-12-31', 'password': 'test'}
	response = file_sharing.share(data)
	assert response['status'] == 'success'
