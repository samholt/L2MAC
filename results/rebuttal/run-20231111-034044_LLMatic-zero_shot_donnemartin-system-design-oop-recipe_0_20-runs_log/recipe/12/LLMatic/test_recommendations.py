from recommendations import Recommendations
from users import create_user


def test_generate_recommendations():
	rec = Recommendations()
	create_user('test_user', 'password')
	recommendations = rec.generate_recommendations('test_user')
	assert recommendations == ['recipe1', 'recipe2', 'recipe3']


def test_send_notifications():
	rec = Recommendations()
	create_user('test_user', 'password')
	rec.send_notifications('test_user', ['new_recipe1', 'new_recipe2'])
	notifications = rec.get_notifications('test_user')
	assert notifications == ['new_recipe1', 'new_recipe2']
