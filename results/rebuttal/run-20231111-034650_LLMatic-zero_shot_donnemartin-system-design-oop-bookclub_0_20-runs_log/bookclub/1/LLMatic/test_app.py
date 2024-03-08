import app
import unittest


class TestApp(unittest.TestCase):

	def setUp(self):
		app.app.testing = True
		self.app = app.app.test_client()

	def test_register(self):
		response = self.app.post('/register', data=dict(username='test', email='test@test.com', password='test'))
		self.assertEqual(response.status_code, 200)

	def test_login(self):
		self.app.post('/register', data=dict(username='test1', email='test1@test.com', password='test1'))
		response = self.app.post('/login', data=dict(username='test1', password='test1'))
		self.assertEqual(response.status_code, 200)

	def test_create_profile(self):
		self.app.post('/register', data=dict(username='test2', email='test2@test.com', password='test2'))
		self.app.post('/login', data=dict(username='test2', password='test2'))
		response = self.app.post('/create_profile', data=dict(reading_interests='fiction', books_read='book1,book2', books_to_read='book3,book4'))
		self.assertEqual(response.status_code, 200)

	def test_update_profile(self):
		self.app.post('/register', data=dict(username='test3', email='test3@test.com', password='test3'))
		self.app.post('/login', data=dict(username='test3', password='test3'))
		self.app.post('/create_profile', data=dict(reading_interests='fiction', books_read='book1,book2', books_to_read='book3,book4'))
		response = self.app.post('/update_profile', data=dict(reading_interests='non-fiction', books_read='book3,book4', books_to_read='book5,book6'))
		self.assertEqual(response.status_code, 200)

	def test_view_profile(self):
		self.app.post('/register', data=dict(username='test4', email='test4@test.com', password='test4'))
		self.app.post('/login', data=dict(username='test4', password='test4'))
		self.app.post('/create_profile', data=dict(reading_interests='fiction', books_read='book1,book2', books_to_read='book3,book4'))
		response = self.app.get('/view_profile', query_string=dict(username='test4'))
		self.assertEqual(response.status_code, 200)

	def test_follow_user(self):
		self.app.post('/register', data=dict(username='test5', email='test5@test.com', password='test5'))
		self.app.post('/login', data=dict(username='test5', password='test5'))
		self.app.post('/create_profile', data=dict(reading_interests='fiction', books_read='book1,book2', books_to_read='book3,book4'))
		response = self.app.post('/follow_user', data=dict(username_to_follow='test5'))
		self.assertEqual(response.status_code, 200)

	def test_recommend_books(self):
		self.app.post('/register', data=dict(username='test6', email='test6@test.com', password='test6'))
		self.app.post('/login', data=dict(username='test6', password='test6'))
		self.app.post('/create_profile', data=dict(reading_interests='fiction', books_read='book1,book2', books_to_read='book3,book4'))
		response = self.app.get('/recommend_books')
		self.assertEqual(response.status_code, 200)
		self.assertIn('recommended_books', response.get_json())

	def test_admin_dashboard(self):
		self.app.post('/register', data=dict(username='admin', email='admin@admin.com', password='admin'))
		self.app.post('/login', data=dict(username='admin', password='admin'))
		response = self.app.get('/admin_dashboard')
		self.assertEqual(response.status_code, 200)
		self.assertIn('user_engagement', response.get_json())
		self.assertIn('popular_books', response.get_json())

	def test_manage_users(self):
		self.app.post('/register', data=dict(username='admin', email='admin@admin.com', password='admin'))
		self.app.post('/login', data=dict(username='admin', password='admin'))
		response = self.app.post('/manage_users', data=dict(action='delete', username='test'))
		self.assertEqual(response.status_code, 200)

	def test_manage_book_clubs(self):
		self.app.post('/register', data=dict(username='admin', email='admin@admin.com', password='admin'))
		self.app.post('/login', data=dict(username='admin', password='admin'))
		response = self.app.post('/manage_book_clubs', data=dict(action='delete', book_club_id='1'))
		self.assertEqual(response.status_code, 200)

	def test_create_notification(self):
		self.app.post('/register', data=dict(username='test7', email='test7@test.com', password='test7'))
		self.app.post('/login', data=dict(username='test7', password='test7'))
		response = self.app.post('/create_notification', data=dict(message='Test notification'))
		self.assertEqual(response.status_code, 200)

	def test_view_notifications(self):
		self.app.post('/register', data=dict(username='test8', email='test8@test.com', password='test8'))
		self.app.post('/login', data=dict(username='test8', password='test8'))
		self.app.post('/create_notification', data=dict(message='Test notification'))
		response = self.app.get('/view_notifications')
		self.assertEqual(response.status_code, 200)

	def test_add_resource(self):
		self.app.post('/register', data=dict(username='test9', email='test9@test.com', password='test9'))
		self.app.post('/login', data=dict(username='test9', password='test9'))
		response = self.app.post('/add_resource', data=dict(resource='Test resource'))
		self.assertEqual(response.status_code, 200)

	def test_view_resources(self):
		self.app.post('/register', data=dict(username='test10', email='test10@test.com', password='test10'))
		self.app.post('/login', data=dict(username='test10', password='test10'))
		self.app.post('/add_resource', data=dict(resource='Test resource'))
		response = self.app.get('/view_resources')
		self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
	unittest.main()
