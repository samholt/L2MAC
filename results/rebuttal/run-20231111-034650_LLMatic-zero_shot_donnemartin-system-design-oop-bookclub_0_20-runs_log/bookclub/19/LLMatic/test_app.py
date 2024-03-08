import pytest
import app


def test_user_creation():
	user = app.User('test_user', 'test_password')
	user.create()
	assert user in app.DATABASE['users'].values()


def test_profile_update():
	user = app.User('test_user', 'test_password')
	user.create()
	user.update_profile({'location': 'test_location'})
	assert user.profile['location'] == 'test_location'


def test_follow_user():
	user1 = app.User('test_user1', 'test_password')
	user2 = app.User('test_user2', 'test_password')
	user1.create()
	user2.create()
	user1.follow_user('test_user2')
	assert 'test_user2' in user1.profile['following']


def test_generate_recommendations():
	user1 = app.User('test_user1', 'test_password')
	user2 = app.User('test_user2', 'test_password')
	user1.create()
	user2.create()
	user1.update_profile({'books': ['book1', 'book2']})
	user2.update_profile({'books': ['book2', 'book3']})
	recommendations = user1.generate_recommendations()
	assert 'book3' in recommendations
	assert 'book2' not in recommendations


def test_get_recommendations():
	user1 = app.User('test_user1', 'test_password')
	user1.create()
	user1.update_profile({'books': ['book1', 'book2']})
	user1.generate_recommendations()
	recommendations = app.User.get_recommendations('test_user1')
	assert recommendations == app.DATABASE['recommendations']['test_user1']


def test_admin_creation():
	admin = app.Admin('test_admin', 'test_password')
	admin.create()
	assert admin in app.DATABASE['users'].values()


def test_manage_user_account():
	admin = app.Admin('test_admin', 'test_password')
	admin.create()
	admin.manage_user_account('test_user', 'activate')
	assert app.DATABASE['admin_actions']['test_user'] == 'activate'


def test_manage_book_club():
	admin = app.Admin('test_admin', 'test_password')
	admin.create()
	admin.manage_book_club('test_book_club', 'create')
	assert app.DATABASE['admin_actions']['test_book_club'] == 'create'


def test_remove_inappropriate_content():
	admin = app.Admin('test_admin', 'test_password')
	admin.create()
	app.DATABASE['resources']['test_content'] = 'Inappropriate content'
	admin.remove_inappropriate_content('test_content')
	assert 'test_content' not in app.DATABASE['resources']


def test_view_analytics():
	admin = app.Admin('test_admin', 'test_password')
	admin.create()
	analytics = admin.view_analytics()
	assert analytics == {'users': len(app.DATABASE['users']), 'book_clubs': len(app.DATABASE['book_clubs'])}


def test_send_notification():
	admin = app.Admin('test_admin', 'test_password')
	admin.create()
	admin.send_notification('test_user', 'test_notification')
	assert app.DATABASE['notifications']['test_user'] == 'test_notification'


def test_send_email_alert():
	admin = app.Admin('test_admin', 'test_password')
	admin.create()
	admin.send_email_alert('test_email', 'test_alert')
	assert app.DATABASE['notifications']['test_email'] == 'test_alert'


def test_share_resource():
	app.DATABASE['resources']['test_resource'] = 'test_content'
	assert 'test_content' == app.DATABASE['resources']['test_resource']


def test_view_resource():
	app.DATABASE['resources']['test_resource'] = 'test_content'
	resource = app.DATABASE['resources'].get('test_resource')
	assert resource == 'test_content'


if __name__ == '__main__':
	pytest.main()
