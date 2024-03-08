import unittest
import json
from app import create_app, db
from app.models import User, Group


class GroupsTestCase(unittest.TestCase):
	def setUp(self):
		self.app = create_app('testing')
		self.app_context = self.app.app_context()
		self.app_context.push()
		db.create_all()
		self.client = self.app.test_client(use_cookies=True)

	def tearDown(self):
		db.session.remove()
		db.drop_all()
		self.app_context.pop()

	def test_create_group(self):
		response = self.client.post('/groups/create', data=json.dumps({'name': 'Test Group', 'user_id': 1}), content_type='application/json')
		self.assertEqual(response.status_code, 201)
		self.assertIn('Group created successfully', response.get_data(as_text=True))

	def test_edit_group(self):
		response = self.client.put('/groups/edit/1', data=json.dumps({'name': 'Edited Group', 'picture': 'new_picture.jpg'}), content_type='application/json')
		self.assertEqual(response.status_code, 200)
		self.assertIn('Group updated successfully', response.get_data(as_text=True))

	def test_manage_group(self):
		response = self.client.post('/groups/manage/1', data=json.dumps({'user_id': 2}), content_type='application/json')
		self.assertEqual(response.status_code, 200)
		self.assertIn('User added to group', response.get_data(as_text=True))

		response = self.client.delete('/groups/manage/1', data=json.dumps({'user_id': 2}), content_type='application/json')
		self.assertEqual(response.status_code, 200)
		self.assertIn('User removed from group', response.get_data(as_text=True))

		response = self.client.put('/groups/manage/1', data=json.dumps({'user_id': 2, 'admin_id': 1}), content_type='application/json')
		self.assertEqual(response.status_code, 200)
		self.assertIn('User added as admin', response.get_data(as_text=True))

		response = self.client.put('/groups/manage/1', data=json.dumps({'user_id': 2}), content_type='application/json')
		self.assertEqual(response.status_code, 200)
		self.assertIn('User removed from admin', response.get_data(as_text=True))
