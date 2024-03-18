import pytest
from posting_content_management import Post


def test_search():
	post = Post('user1', 'This is a test post')
	assert post.search('test') == True
	assert post.search('not in post') == False


def test_filter():
	post = Post('user1', 'This is a #test post')
	assert post.filter('#test') == True
	assert post.filter('#notInPost') == False
