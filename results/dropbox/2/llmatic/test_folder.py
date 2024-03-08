from folder import Folder
from file import File

def test_folder():
	folder = Folder('test_folder')
	file = File('test_file', 100, 'content')
	folder.add_file(file)
	assert file in folder.files
	folder.remove_file(file)
	assert file not in folder.files
