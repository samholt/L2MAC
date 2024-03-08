import unittest
from cloudsafe.main import app

class TestMain(unittest.TestCase):
	def setUp(self):
		self.app = app.test_client()

	def test_register(self):
		response = self.app.post('/register', json={'name': 'Test User', 'email': 'test@example.com', 'password': 'password', 'profile_picture': 'profile.jpg'})
		self.assertEqual(response.status_code, 201)

	def test_login(self):
		response = self.app.post('/login', json={'email': 'test@example.com', 'password': 'password'})
		self.assertEqual(response.status_code, 200)

	def test_profile(self):
		response = self.app.put('/profile', json={'name': 'Test User', 'email': 'test@example.com', 'new_password': 'new_password', 'profile_picture': 'new_profile.jpg'})
		self.assertEqual(response.status_code, 200)

	def test_storage(self):
		response = self.app.get('/storage')
		self.assertEqual(response.status_code, 200)

	def test_upload(self):
		response = self.app.post('/upload', json={'file': 'file.txt'})
		self.assertEqual(response.status_code, 201)

	def test_download(self):
		response = self.app.get('/download', json={'file_id': 1})
		self.assertEqual(response.status_code, 200)

	def test_rename(self):
		response = self.app.put('/rename', json={'file_id': 1, 'new_name': 'new_file.txt'})
		self.assertEqual(response.status_code, 200)

	def test_move(self):
		response = self.app.put('/move', json={'file_id': 1, 'new_location': '/new_folder'})
		self.assertEqual(response.status_code, 200)

	def test_delete(self):
		response = self.app.delete('/delete', json={'file_id': 1})
		self.assertEqual(response.status_code, 200)

	def test_create(self):
		response = self.app.post('/create', json={'name': 'New Folder'})
		self.assertEqual(response.status_code, 201)

	def test_rename_folder(self):
		response = self.app.put('/rename', json={'folder_id': 1, 'new_name': 'Renamed Folder'})
		self.assertEqual(response.status_code, 200)

	def test_move_folder(self):
		response = self.app.put('/move', json={'folder_id': 1, 'new_location': '/new_folder'})
		self.assertEqual(response.status_code, 200)

	def test_delete_folder(self):
		response = self.app.delete('/delete', json={'folder_id': 1})
		self.assertEqual(response.status_code, 200)

	def test_generate_link(self):
		response = self.app.post('/generate', json={'file_id': 1})
		self.assertEqual(response.status_code, 201)

	def test_set_expiry_date(self):
		response = self.app.put('/expiry', json={'link_id': 1, 'expiry_date': '2022-12-31'})
		self.assertEqual(response.status_code, 200)

	def test_set_password(self):
		response = self.app.put('/password', json={'link_id': 1, 'password': 'password'})
		self.assertEqual(response.status_code, 200)

	def test_invite_user(self):
		response = self.app.post('/invite', json={'folder_id': 1, 'user_id': 2})
		self.assertEqual(response.status_code, 201)

	def test_set_permissions(self):
		response = self.app.put('/permissions', json={'folder_id': 1, 'user_id': 2, 'permissions': 'read'})
		self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
	unittest.main()
