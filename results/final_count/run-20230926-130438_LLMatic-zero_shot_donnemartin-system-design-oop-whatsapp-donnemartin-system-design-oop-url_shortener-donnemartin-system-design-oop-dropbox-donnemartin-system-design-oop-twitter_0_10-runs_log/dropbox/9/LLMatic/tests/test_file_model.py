import datetime
from models.file import File
from models.user import User

def test_file_model():
	user = User('1', 'Test User', 'test@example.com', 'password', 'profile_pic.jpg', 0)
	file = File('1', 'Test File', 100, datetime.datetime.now(), user, [])
	assert file.id == '1'
	assert file.content == 'Test File'
	assert file.size == 100
	assert isinstance(file.upload_date, datetime.datetime)
	assert file.owner == user
	assert file.versions == []
