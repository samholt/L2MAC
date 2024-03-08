import cli


def test_cli():
	cli_instance = cli.CLI()
	assert cli_instance.user.create_user('test', 'test') == 'User created successfully'
	assert cli_instance.user.login('test', 'test') == 'Login successful'
	cli_instance.transaction.add_transaction('test', {'amount': 100, 'category': 'groceries'})
	assert cli_instance.transaction.transactions['test'][0]['amount'] == 100
	cli_instance.bank_account.link_account('test', 1000)
	assert cli_instance.bank_account.get_account('test')['balance'] == 1000
	cli_instance.budget.set_monthly_budget('test', 500)
	assert cli_instance.budget.get_budget_info('test')['monthly_budget'] == 500
	cli_instance.investment.add_investment('test', 1000)
	assert cli_instance.investment.investments['test'] == 1000
	cli_instance.recommendations.add_recommendation('test', 'Save more')
	assert cli_instance.recommendations.get_recommendations('test')[0] == 'Save more'
	cli_instance.notifications.send_notification('test', 'Test notification')
	assert cli_instance.notifications.get_notifications('test')[0] == 'Test notification'

