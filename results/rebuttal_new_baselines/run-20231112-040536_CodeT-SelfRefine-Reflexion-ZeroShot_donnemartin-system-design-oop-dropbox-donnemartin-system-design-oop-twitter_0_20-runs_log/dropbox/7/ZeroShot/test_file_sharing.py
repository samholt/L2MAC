import pytest
import file_sharing

def test_share_file():
	data = {'file_name': 'NewTest', 'shared_with': ['test@test.com']}
	response = file_sharing.share_file(data)
	assert response == {'message': 'File shared successfully'}
