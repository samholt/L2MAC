import pytest
import app
import json

@pytest.fixture
def client():
	app.app.config['TESTING'] = True
	with app.app.test_client() as client:
		yield client


def test_create_account(client):
	response = client.post('/create_account', json={'user_id': 'user1', 'user_info': {'name': 'John Doe', 'email': 'john.doe@example.com'}})
	assert response.get_json()['message'] == 'Account created successfully'


def test_link_bank_account_without_account(client):
	response = client.post('/link_bank_account', json={'user_id': 'user1', 'bank_account_info': {'bank_name': 'Bank of America', 'account_number': '1234567890'}})
	assert response.status_code == 400


def test_handle_mfa_without_account(client):
	response = client.post('/handle_mfa', json={'user_id': 'user1', 'mfa_info': {'mfa_type': 'sms', 'phone_number': '+1234567890'}})
	assert response.status_code == 400


def test_link_bank_account(client):
	client.post('/create_account', json={'user_id': 'user1', 'user_info': {'name': 'John Doe', 'email': 'john.doe@example.com'}})
	response = client.post('/link_bank_account', json={'user_id': 'user1', 'bank_account_info': {'bank_name': 'Bank of America', 'account_number': '1234567890'}})
	assert response.get_json()['message'] == 'Bank account linked successfully'


def test_handle_mfa(client):
	client.post('/create_account', json={'user_id': 'user1', 'user_info': {'name': 'John Doe', 'email': 'john.doe@example.com'}})
	response = client.post('/handle_mfa', json={'user_id': 'user1', 'mfa_info': {'mfa_type': 'sms', 'phone_number': '+1234567890'}})
	assert response.get_json()['message'] == 'MFA handled successfully'


def test_import_expenses_incomes(client):
	response = client.post('/import_expenses_incomes', json={'user_id': 'user1', 'expenses': {'groceries': 100, 'rent': 500}, 'incomes': {'salary': 2000}})
	assert response.get_json()['message'] == 'Expenses and incomes imported successfully'


def test_categorize_expenses_incomes(client):
	response = client.post('/categorize_expenses_incomes', json={'user_id': 'user1', 'expense_categories': ['groceries', 'rent'], 'income_categories': ['salary']})
	assert response.get_json()['message'] == 'Expenses and incomes categorized successfully'


def test_visualize_expense_income_history(client):
	response = client.get('/visualize_expense_income_history?user_id=user1')
	assert response.get_json() == {'expenses': {'groceries': 100, 'rent': 500}, 'incomes': {'salary': 2000}}


def test_set_adjust_budget(client):
	response = client.post('/set_adjust_budget', json={'user_id': 'user1', 'budget': 1500})
	assert response.get_json()['message'] == 'Budget set/adjusted successfully'


def test_alert_budget_limit(client):
	response = client.get('/alert_budget_limit?user_id=user1')
	assert response.get_json()['message'] == 'No budget or spending data available'


def test_analyze_spending(client):
	response = client.get('/analyze_spending?user_id=user1')
	assert response.get_json()['message'] == 'No budget or spending data available'


def test_integrate_investment_account(client):
	response = client.post('/integrate_investment_account', json={'user_id': 'user1', 'account_info': {'brokerage': 'Brokerage XYZ', 'account_number': '1234567890'}})
	assert response.get_json()['message'] == 'Investment account integrated successfully'


def test_track_investment(client):
	response = client.post('/track_investment', json={'user_id': 'user1', 'investment_info': {'balance': 10000, 'performance': 0.05}})
	assert response.get_json()['message'] == 'Investment tracked successfully'


def test_overview_asset_allocation(client):
	response = client.post('/overview_asset_allocation', json={'user_id': 'user1', 'allocation_info': {'stocks': 50, 'bonds': 30, 'cash': 20}})
	assert response.get_json()['message'] == 'Asset allocation overviewed successfully'


def test_generate_report(client):
	response = client.post('/generate_report', json={'user_id': 'user1', 'report': {'expenses': 1000, 'income': 2000}})
	assert response.get_json() == {'expenses': 1000, 'income': 2000}


def test_custom_alert(client):
	response = client.post('/custom_alert', json={'user_id': 'user1', 'alert': 'You have exceeded your budget limit'})
	assert response.get_json()['alert'] == 'You have exceeded your budget limit'
