import notification


def test_create_notification():
	user = 'test_user'
	type = 'like'
	post = 'test_post'
	new_notification = notification.Notification.create_notification(user, type, post)
	assert new_notification.user == user
	assert new_notification.type == type
	assert new_notification.post == post
	assert new_notification in notification.notifications_db.values()
