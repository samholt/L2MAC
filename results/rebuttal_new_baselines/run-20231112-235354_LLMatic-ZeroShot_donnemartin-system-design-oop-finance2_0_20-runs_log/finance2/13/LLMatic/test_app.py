import pytest
from app import app

@pytest.fixture
def client():
	with app.test_client() as client:
		yield client


def test_create_user(client):
	resp = client.post('/create_user', json={'username': 'test', 'password': 'test', 'email': 'test@test.com'})
	assert resp.status_code == 200
	assert resp.get_json() == {'message': 'User created successfully'}


def test_authenticate_user(client):
	client.post('/create_user', json={'username': 'test', 'password': 'test', 'email': 'test@test.com'})
	resp = client.post('/authenticate_user', json={'username': 'test', 'password': 'test', 'auth_code': '123456'})
	assert resp.status_code == 200
	assert resp.get_json() == {'message': 'User authenticated successfully'}


def test_link_bank_account(client):
	resp = client.post('/link_bank_account', json={'account_number': '1234567890'})
	assert resp.status_code == 200
	assert resp.get_json() == {'message': 'Bank account linked successfully'}


def test_add_expense(client):
	resp = client.post('/add_expense', json={'amount': 100, 'category': 'Groceries'})
	assert resp.status_code == 200
	assert resp.get_json() == {'message': 'Expense added successfully'}


def test_add_income(client):
	resp = client.post('/add_income', json={'amount': 1000, 'category': 'Salary'})
	assert resp.status_code == 200
	assert resp.get_json() == {'message': 'Income added successfully'}


def test_set_budget(client):
	resp = client.post('/set_budget', json={'new_budget': 2000})
	assert resp.status_code == 200
	assert resp.get_json() == {'message': 'Budget set successfully'}


def test_adjust_budget(client):
	resp = client.post('/adjust_budget', json={'adjustment': 500})
	assert resp.status_code == 200
	assert resp.get_json() == {'message': 'Budget adjusted successfully'}


def test_link_investment_account(client):
	resp = client.post('/link_investment_account', json={'account_name': 'Investment1', 'account': {'balance': 10000, 'assets': {'Stocks': 5000, 'Bonds': 5000}}})
	assert resp.status_code == 200
	assert resp.get_json() == {'message': 'Investment account linked successfully'}


def test_track_investment_performance(client):
	resp = client.post('/track_investment_performance', json={'account_name': 'Investment1', 'performance': {'return': 10, 'risk': 5}})
	assert resp.status_code == 200
	assert resp.get_json() == {'message': 'Investment performance tracked successfully'}


def test_generate_report(client):
	resp = client.get('/generate_report', query_string={'month': 'January'})
	assert resp.status_code == 404
	assert resp.get_json() == {'message': 'No data for this month'}
