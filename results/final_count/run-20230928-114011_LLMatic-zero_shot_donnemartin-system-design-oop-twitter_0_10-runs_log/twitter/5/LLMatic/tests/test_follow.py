import pytest
from follow import Follow
from post import Post


def test_follow():
	follow = Follow('user1', 'user2')
	follow.follow('user3')
	assert follow.followed == 'user3'


def test_unfollow():
	follow = Follow('user1', 'user2')
	follow.unfollow('user2')
	assert follow.followed == None


def test_display_timeline():
	follow = Follow('user1', 'user2')
	follow.followed_posts.append(Post('user2', 'Hello, world!', ['image1.jpg']))
	assert len(follow.display_timeline()) == 1
