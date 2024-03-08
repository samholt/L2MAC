import unittest
from models.alert import Alert


class TestAlert(unittest.TestCase):
	def setUp(self):
		self.user = 'test_user'
		self.message = 'test_message'
		self.alert = Alert.create_alert(self.user, self.message)

	def test_create_alert(self):
		self.assertEqual(self.alert.user, self.user)
		self.assertEqual(self.alert.message, self.message)

	def test_get_user_alerts(self):
		alerts = Alert.get_user_alerts(self.user)
		self.assertIn(self.alert, alerts)

if __name__ == '__main__':
	unittest.main()

