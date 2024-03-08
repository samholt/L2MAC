import pytest
from models import db, User, Post, Comment, Like, Retweet, Follow, Message, Notification, Trend


def test_user_model():
	assert 'id' in User.__table__.columns
	assert 'email' in User.__table__.columns
	assert 'username' in User.__table__.columns
	assert 'password' in User.__table__.columns
	assert 'profile_picture' in User.__table__.columns
	assert 'bio' in User.__table__.columns
	assert 'website_link' in User.__table__.columns
	assert 'location' in User.__table__.columns
	assert 'is_private' in User.__table__.columns


def test_post_model():
	assert 'id' in Post.__table__.columns
	assert 'user_id' in Post.__table__.columns
	assert 'content' in Post.__table__.columns
	assert 'image_url' in Post.__table__.columns
	assert 'created_at' in Post.__table__.columns


def test_comment_model():
	assert 'id' in Comment.__table__.columns
	assert 'post_id' in Comment.__table__.columns
	assert 'user_id' in Comment.__table__.columns
	assert 'content' in Comment.__table__.columns
	assert 'created_at' in Comment.__table__.columns


def test_like_model():
	assert 'id' in Like.__table__.columns
	assert 'post_id' in Like.__table__.columns
	assert 'user_id' in Like.__table__.columns


def test_retweet_model():
	assert 'id' in Retweet.__table__.columns
	assert 'post_id' in Retweet.__table__.columns
	assert 'user_id' in Retweet.__table__.columns


def test_follow_model():
	assert 'id' in Follow.__table__.columns
	assert 'follower_id' in Follow.__table__.columns
	assert 'followed_id' in Follow.__table__.columns


def test_message_model():
	assert 'id' in Message.__table__.columns
	assert 'sender_id' in Message.__table__.columns
	assert 'receiver_id' in Message.__table__.columns
	assert 'content' in Message.__table__.columns
	assert 'created_at' in Message.__table__.columns


def test_notification_model():
	assert 'id' in Notification.__table__.columns
	assert 'user_id' in Notification.__table__.columns
	assert 'content' in Notification.__table__.columns
	assert 'created_at' in Notification.__table__.columns


def test_trend_model():
	assert 'id' in Trend.__table__.columns
	assert 'hashtag' in Trend.__table__.columns
	assert 'count' in Trend.__table__.columns

