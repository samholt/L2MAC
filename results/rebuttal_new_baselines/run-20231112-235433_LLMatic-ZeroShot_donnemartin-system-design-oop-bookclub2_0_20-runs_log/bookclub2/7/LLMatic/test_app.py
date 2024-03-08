import unittest
from flask import Flask
import app

class TestApp(unittest.TestCase):
	def setUp(self):
		self.app = app.app.test_client()
		self.app.testing = True 

	def test_home_status_code(self):
		result = self.app.get('/')
		self.assertEqual(result.status_code, 200)

if __name__ == '__main__':
	unittest.main()
