from cloudsafe.models.file import File

def test_file_model():
	file = File(id='1', name='test', size=100, type='txt', parent_folder='root', version_history=[])
	assert file.id == '1'
	assert file.name == 'test'
	assert file.size == 100
	assert file.type == 'txt'
	assert file.parent_folder == 'root'
	assert file.version_history == []
