import unittest
from controllers.alert_controller import AlertController
from controllers.user_controller import UserController
from models.alert import Alert


class TestAlertController(unittest.TestCase):
	def test_create_alert(self):
		user = UserController.create_user('John Doe', 'john@example.com', 'password')
		alert = AlertController.create_alert(user, 'Budget limit nearing')
		self.assertIsInstance(alert, Alert)

	def test_get_user_alerts(self):
		user = UserController.create_user('John Doe', 'john@example.com', 'password')
		AlertController.create_alert(user, 'Budget limit nearing')
		alerts = AlertController.get_alerts(user)
		self.assertIsInstance(alerts, list)
		self.assertEqual(len(alerts), 1)
