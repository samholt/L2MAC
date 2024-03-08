import unittest
from flask import url_for
from app import create_app


class TestWebBlueprint(unittest.TestCase):

	def setUp(self):
		self.app = create_app('testing')
		self.client = self.app.test_client()

	def test_home_route(self):
		response = self.client.get(url_for('web.home'))
		self.assertEqual(response.status_code, 200)

	def test_chat_route(self):
		response = self.client.get(url_for('web.chat'))
		self.assertEqual(response.status_code, 302)
