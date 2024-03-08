import pytest
from discussion import Discussion

def test_create_forum():
	d = Discussion()
	d.create_forum('Test Forum')
	assert 'Test Forum' in d.forums

def test_post_comment():
	d = Discussion()
	d.create_forum('Test Forum')
	d.post_comment('Test Forum', 'This is a test comment')
	assert d.forums['Test Forum']['comments'][0]['comment'] == 'This is a test comment'

def test_post_reply():
	d = Discussion()
	d.create_forum('Test Forum')
	d.post_comment('Test Forum', 'This is a test comment')
	d.post_reply('Test Forum', 0, 'This is a test reply')
	assert d.forums['Test Forum']['comments'][0]['replies'][0] == 'This is a test reply'

def test_upload_link():
	d = Discussion()
	d.create_forum('Test Forum')
	d.upload_link('Test Forum', 'https://example.com')
	assert d.forums['Test Forum']['link'] == 'https://example.com'

def test_upload_image():
	d = Discussion()
	d.create_forum('Test Forum')
	d.upload_image('Test Forum', 'image.jpg')
	assert d.forums['Test Forum']['image'] == 'image.jpg'
