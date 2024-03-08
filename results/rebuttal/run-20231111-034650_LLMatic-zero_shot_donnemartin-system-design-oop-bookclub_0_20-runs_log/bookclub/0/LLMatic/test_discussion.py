import pytest
from discussion import Discussion

def test_create_discussion():
	discussion = Discussion('Test Topic', 'Test Book Club')
	assert discussion.topic == 'Test Topic'
	assert discussion.book_club == 'Test Book Club'
	assert discussion.comments == []

def test_add_comment():
	discussion = Discussion('Test Topic', 'Test Book Club')
	discussion.add_comment('Test Comment')
	assert discussion.comments == ['Test Comment']

def test_upload_image():
	discussion = Discussion('Test Topic', 'Test Book Club')
	discussion.upload_image('Test Image')
	assert discussion.comments == [{'type': 'image', 'content': 'Test Image'}]

def test_upload_link():
	discussion = Discussion('Test Topic', 'Test Book Club')
	discussion.upload_link('Test Link')
	assert discussion.comments == [{'type': 'link', 'content': 'Test Link'}]
