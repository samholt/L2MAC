import pytest
from post import Post

@pytest.fixture
def post():
	return Post('test@example.com', 'Hello, world!')


def test_to_dict(post):
	post_dict = post.to_dict()
	assert post_dict['user_email'] == 'test@example.com'
	assert post_dict['content'] == 'Hello, world!'
	assert post_dict['likes'] == 0
	assert post_dict['retweets'] == 0
	assert post_dict['replies'] == 0
