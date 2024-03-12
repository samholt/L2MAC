import os
import unittest


class TestApp(unittest.TestCase):
	def test_app_exists(self):
		self.assertTrue(os.path.exists('app.py'))

	def test_config_exists(self):
		self.assertTrue(os.path.exists('config.py'))

	def test_models_exists(self):
		self.assertTrue(os.path.exists('models.py'))

	def test_routes_exists(self):
		self.assertTrue(os.path.exists('routes.py'))

	def test_utils_exists(self):
		self.assertTrue(os.path.exists('utils.py'))

	def test_requirements_exists(self):
		self.assertTrue(os.path.exists('requirements.txt'))
