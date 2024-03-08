import file_sharing

def test_generate_shareable_link():
	# Test with a file that exists in the database
	assert file_sharing.generate_shareable_link('file1') == 'http://localhost:5000/download/file1'
	# Test with a file that does not exist in the database
	assert file_sharing.generate_shareable_link('file4') == 'File not found.'
