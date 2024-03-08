import pytest
from post import create_post, get_trending_topics

# Test data
user_id = 1
content = 'This is a test post'

# Create a post
create_post(user_id, content)

# Test the get_trending_topics function
def test_get_trending_topics():
	trending_posts = get_trending_topics()
	assert trending_posts is not None
	assert len(trending_posts) > 0
	# Check that the posts are sorted by the sum of likes and retweets
	for i in range(len(trending_posts) - 1):
		assert trending_posts[i].likes + trending_posts[i].retweets >= trending_posts[i + 1].likes + trending_posts[i + 1].retweets
