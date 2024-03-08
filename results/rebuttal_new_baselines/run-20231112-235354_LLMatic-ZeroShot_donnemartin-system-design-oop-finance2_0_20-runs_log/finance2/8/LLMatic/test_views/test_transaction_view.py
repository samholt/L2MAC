import pytest
from flask import Flask, json
from views.transaction_view import create_transaction, get_user_transactions, categorize_transactions

app = Flask(__name__)

@app.route('/create_transaction', methods=['POST'])
def create_transaction_view():
	return create_transaction()

@app.route('/get_user_transactions', methods=['GET'])
def get_user_transactions_view():
	return get_user_transactions()

@app.route('/categorize_transactions', methods=['POST'])
def categorize_transactions_view():
	return categorize_transactions()


def test_create_transaction():
	with app.test_client() as client:
		response = client.post('/create_transaction', data=json.dumps({'user': 'Test User', 'amount': 100, 'category': 'Groceries'}), content_type='application/json')
		data = json.loads(response.get_data(as_text=True))
		assert response.status_code == 201
		assert data['message'] == 'Transaction created successfully'
		assert data['transaction']['user'] == 'Test User'
		assert data['transaction']['amount'] == 100
		assert data['transaction']['category'] == 'Groceries'


def test_get_user_transactions():
	with app.test_client() as client:
		client.post('/create_transaction', data=json.dumps({'user': 'Test User', 'amount': 100, 'category': 'Groceries'}), content_type='application/json')
		response = client.get('/get_user_transactions', query_string={'user': 'Test User'})
		data = json.loads(response.get_data(as_text=True))
		assert response.status_code == 200
		assert len(data['transactions']) == 1
		assert data['transactions'][0]['user'] == 'Test User'
		assert data['transactions'][0]['amount'] == 100
		assert data['transactions'][0]['category'] == 'Groceries'


def test_categorize_transactions():
	with app.test_client() as client:
		client.post('/create_transaction', data=json.dumps({'user': 'Test User', 'amount': 100, 'category': 'Groceries'}), content_type='application/json')
		response = client.post('/categorize_transactions', data=json.dumps({'transactions': [{'user': 'Test User', 'amount': 100, 'category': 'Groceries'}]}), content_type='application/json')
		data = json.loads(response.get_data(as_text=True))
		assert response.status_code == 200
		assert len(data['transactions']) == 1
		assert data['transactions'][0]['user'] == 'Test User'
		assert data['transactions'][0]['amount'] == 100
		assert data['transactions'][0]['category'] == 'Groceries'

