import pytest
import app
from user import User
from transaction import Transaction
from bank_account import BankAccount
from budget import Budget
from investment import Investment, Alert
from report import Report
from recommendation import Recommendation
from notification import Notification

@pytest.fixture
def client():
	app.app.config['TESTING'] = True
	with app.app.test_client() as client:
		yield client


def test_create_user(client):
	response = client.post('/user', json={'username': 'test', 'password': 'test', 'email': 'test@test.com'})
	assert response.status_code == 201
	assert response.get_json() == {'message': 'User created'}

	response = client.post('/user', json={'username': 'test', 'password': 'test', 'email': 'test@test.com'})
	assert response.status_code == 400
	assert response.get_json() == {'message': 'User already exists'}


def test_get_user(client):
	app.user_manager.create_user('test', 'test', 'test@test.com')
	response = client.get('/user/test')
	assert response.status_code == 200
	assert response.get_json() == {'username': 'test', 'email': 'test@test.com'}


def test_add_transaction(client):
	response = client.post('/transaction', json={'id': '1', 'amount': '100', 'date': '2022-01-01', 'type': 'debit'})
	assert response.status_code == 201
	assert response.get_json() == {'message': 'Transaction added'}


def test_get_transaction(client):
	app.transaction_manager.add_transaction('1', '100', '2022-01-01', 'debit')
	response = client.get('/transaction/1')
	assert response.status_code == 200
	assert response.get_json() == {'id': '1', 'amount': 100.0, 'date': '2022-01-01', 'type': 'debit'}


def test_link_account(client):
	response = client.post('/bank_account', json={'account_number': '1234567890'})
	assert response.status_code == 201
	assert response.get_json() == {'message': 'Bank account linked'}


def test_get_bank_account(client):
	app.bank_account_manager.link_account('1234567890')
	response = client.get('/bank_account/1234567890')
	assert response.status_code == 200
	assert response.get_json() == {'account_number': '1234567890', 'balance': 0}


def test_add_budget(client):
	response = client.post('/budget', json={'category': 'Food', 'limit': '500'})
	assert response.status_code == 201
	assert response.get_json() == {'message': 'Budget added'}


def test_get_budget(client):
	app.budget_manager.add_budget(Budget('Food', 500))
	response = client.get('/budget/Food')
	assert response.status_code == 200
	assert response.get_json() == {'category': 'Food', 'limit': 500, 'total_spent': 0, 'remaining_budget': 500}


def test_add_investment(client):
	response = client.post('/investment', json={'name': 'Stock', 'quantity': '10', 'purchase_price': '100', 'current_price': '150'})
	assert response.status_code == 201
	assert response.get_json() == {'message': 'Investment added'}


def test_get_investment(client):
	app.investment_manager.add_investment('Stock', 10, 100, 150)
	response = client.get('/investment/Stock')
	assert response.status_code == 200
	assert response.get_json() == {'name': 'Stock', 'quantity': 10, 'purchase_price': 100, 'current_price': 150, 'performance': 500.0}


def test_create_report(client):
	app.user_manager.create_user('test', 'test', 'test@test.com')
	response = client.post('/report', json={'username': 'test', 'month': 'January', 'income': '1000', 'expenses': '500', 'savings': '500', 'investments': ['Stock']})
	assert response.status_code == 201
	assert response.get_json() == {'message': 'Report created'}


def test_get_report(client):
	user = app.user_manager.create_user('test', 'test', 'test@test.com')
	app.report_manager.create_report(user, 'January', 1000, 500, 500, ['Stock'])
	response = client.get('/report/test/January')
	assert response.status_code == 200
	assert response.get_json() == {'user': 'test', 'month': 'January', 'income': 1000, 'expenses': 500, 'savings': 500, 'investments': ['Stock']}


def test_create_recommendation(client):
	app.user_manager.create_user('test', 'test', 'test@test.com')
	response = client.post('/recommendation', json={'username': 'test'})
	assert response.status_code == 201
	assert response.get_json() == {'message': 'Recommendation created'}


def test_get_recommendation(client):
	user = app.user_manager.create_user('test', 'test', 'test@test.com')
	app.recommendation_manager.create_recommendation(user)
	response = client.get('/recommendation/test')
	assert response.status_code == 200
	assert response.get_json() == {'username': 'test', 'tips': ['Save more money'], 'financial_products': ['Investment product']}


def test_create_notification(client):
	app.user_manager.create_user('test', 'test', 'test@test.com')
	response = client.post('/notification', json={'username': 'test', 'message': 'Test notification'})
	assert response.status_code == 201
	assert 'Notification created' in response.get_json()['message']

