import database

def test_database_schema():
	assert set(database.user_schema) == set(['email', 'username', 'password', 'profile_picture', 'bio', 'website_link', 'location', 'is_private']), 'User schema is incorrect'
	assert set(database.post_schema) == set(['user_id', 'content', 'image', 'timestamp']), 'Post schema is incorrect'
	assert set(database.comment_schema) == set(['user_id', 'post_id', 'content', 'timestamp']), 'Comment schema is incorrect'
	assert set(database.like_schema) == set(['user_id', 'post_id', 'timestamp']), 'Like schema is incorrect'
	assert set(database.follow_schema) == set(['follower_id', 'followee_id', 'timestamp']), 'Follow schema is incorrect'
	assert set(database.message_schema) == set(['sender_id', 'receiver_id', 'content', 'timestamp']), 'Message schema is incorrect'
	assert set(database.notification_schema) == set(['user_id', 'content', 'timestamp']), 'Notification schema is incorrect'
	assert set(database.trend_schema) == set(['hashtag', 'mentions']), 'Trend schema is incorrect'
