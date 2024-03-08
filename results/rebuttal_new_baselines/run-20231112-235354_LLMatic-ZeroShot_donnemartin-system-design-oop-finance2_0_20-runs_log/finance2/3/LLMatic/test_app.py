import unittest
import app

class TestApp(unittest.TestCase):

	def setUp(self):
		self.app = app.app.test_client()

	def test_create_user(self):
		response = self.app.post('/create_user', json={'name': 'John Doe', 'email': 'john@example.com', 'password': 'password'})
		self.assertEqual(response.status_code, 201)

	def test_authenticate_user(self):
		response = self.app.post('/authenticate_user', json={'email': 'john@example.com', 'password': 'password'})
		self.assertEqual(response.status_code, 200)

	def test_link_bank_account(self):
		response = self.app.post('/link_bank_account', json={'user': 'John Doe', 'bank_account': '1234567890'})
		self.assertEqual(response.status_code, 200)

	def test_create_transaction(self):
		response = self.app.post('/create_transaction', json={'user': 'John Doe', 'amount': 100, 'category': 'Groceries', 'date': '2022-01-01'})
		self.assertEqual(response.status_code, 201)

	def test_get_transactions(self):
		response = self.app.get('/get_transactions', json={'user': 'John Doe'})
		self.assertEqual(response.status_code, 200)

	def test_set_budget(self):
		response = self.app.post('/set_budget', json={'user': 'John Doe', 'amount': 500, 'category': 'Groceries'})
		self.assertEqual(response.status_code, 201)

	def test_adjust_budget(self):
		response = self.app.post('/adjust_budget', json={'user': 'John Doe', 'amount': 100})
		self.assertEqual(response.status_code, 201)

	def test_get_budgets(self):
		response = self.app.get('/get_budgets', json={'user': 'John Doe'})
		self.assertEqual(response.status_code, 200)

	def test_link_investment_account(self):
		response = self.app.post('/link_investment_account', json={'user': 'John Doe', 'account': '1234567890'})
		self.assertEqual(response.status_code, 201)

	def test_track_investment_performance(self):
		response = self.app.get('/track_investment_performance', json={'user': 'John Doe'})
		self.assertEqual(response.status_code, 200)

	def test_get_investments(self):
		response = self.app.get('/get_investments', json={'user': 'John Doe'})
		self.assertEqual(response.status_code, 200)

	def test_create_alert(self):
		response = self.app.post('/create_alert', json={'user': 'John Doe', 'alert_type': 'Low Balance', 'message': 'Your balance is low.'})
		self.assertEqual(response.status_code, 201)

	def test_get_alerts(self):
		response = self.app.get('/get_alerts', json={'user': 'John Doe'})
		self.assertEqual(response.status_code, 200)

	def test_customize_alert(self):
		response = self.app.post('/customize_alert', json={'user': 'John Doe', 'alert_type': 'Low Balance', 'message': 'Your balance is very low.'})
		self.assertEqual(response.status_code, 201)


if __name__ == '__main__':
	unittest.main()
