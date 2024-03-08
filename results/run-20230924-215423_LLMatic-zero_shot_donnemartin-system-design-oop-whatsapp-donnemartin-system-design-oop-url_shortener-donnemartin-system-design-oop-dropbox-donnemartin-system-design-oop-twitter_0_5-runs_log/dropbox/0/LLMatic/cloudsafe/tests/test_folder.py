from cloudsafe.models.folder import Folder

def test_folder_model():
	folder = Folder(id='1', name='test', parent_folder='root')
	assert folder.id == '1'
	assert folder.name == 'test'
	assert folder.parent_folder == 'root'
