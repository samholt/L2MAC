import sys
sys.path.append('.')

import pytest
from models import User, Post, Comment, Like, Retweet, Follow, Message, Notification, Trend

def test_models():
	assert User
	assert Post
	assert Comment
	assert Like
	assert Retweet
	assert Follow
	assert Message
	assert Notification
	assert Trend

