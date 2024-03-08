import models
import data

def test_generate_monthly_report():
	user = models.User.create_user('test_user', 'test_password', 'test_email')
	monthly_report = user.generate_monthly_report()
	assert monthly_report['income'] == 3000
	assert monthly_report['expense'] == 500

def test_generate_spending_trends():
	data_obj = data.Data()
	transaction1 = data.Transaction('1', 'income', 1000, 'salary')
	transaction2 = data.Transaction('2', 'expense', 200, 'groceries')
	data_obj.add_transaction(transaction1)
	data_obj.add_transaction(transaction2)
	spending_trends = data_obj.generate_spending_trends()
	assert spending_trends['salary'] == 1000
	assert spending_trends['groceries'] == 200

