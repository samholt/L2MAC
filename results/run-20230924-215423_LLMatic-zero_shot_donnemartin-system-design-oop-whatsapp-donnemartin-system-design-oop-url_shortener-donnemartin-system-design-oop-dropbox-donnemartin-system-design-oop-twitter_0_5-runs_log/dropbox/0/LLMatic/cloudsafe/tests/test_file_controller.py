from cloudsafe.controllers.file_controller import upload, download, organize, version


def test_upload():
	assert upload() == 'File uploaded'


def test_download():
	assert download() == 'File downloaded'


def test_organize():
	assert organize() == 'File organized'


def test_version():
	assert version() == 'File versioned'
