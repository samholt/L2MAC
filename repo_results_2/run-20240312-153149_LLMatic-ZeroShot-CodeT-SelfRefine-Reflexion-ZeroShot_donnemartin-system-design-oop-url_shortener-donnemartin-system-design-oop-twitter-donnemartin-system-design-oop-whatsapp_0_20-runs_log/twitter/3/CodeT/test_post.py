import pytest
from post import Post

@pytest.fixture
def post():
	return Post('test@test.com', 'Hello, world!')

def test_to_dict(post):
	post_dict = post.to_dict()
	assert post_dict['user_email'] == 'test@test.com'
	assert post_dict['content'] == 'Hello, world!'
