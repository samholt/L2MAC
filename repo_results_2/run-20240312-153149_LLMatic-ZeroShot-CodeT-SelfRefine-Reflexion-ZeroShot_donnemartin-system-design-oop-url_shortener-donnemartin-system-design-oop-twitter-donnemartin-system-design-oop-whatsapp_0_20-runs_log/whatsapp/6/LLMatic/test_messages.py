import json
import app

def test_send_message():
	app.app.testing = True
	client = app.app.test_client()

	# Create users for testing
	client.post('/signup', data=json.dumps({'email': 'test@example.com', 'password': 'password'}), content_type='application/json')
	client.post('/signup', data=json.dumps({'email': 'test2@example.com', 'password': 'password'}), content_type='application/json')

	# Log in users for testing
	client.post('/login', data=json.dumps({'email': 'test@example.com', 'password': 'password'}), content_type='application/json')
	client.post('/login', data=json.dumps({'email': 'test2@example.com', 'password': 'password'}), content_type='application/json')

	# Test send_message with missing parameters
	response = client.post('/send_message', data=json.dumps({}), content_type='application/json')
	assert response.status_code == 400

	# Test send_message with invalid sender or receiver
	response = client.post('/send_message', data=json.dumps({'sender': 'test@example.com', 'receiver': 'nonexistent@example.com', 'message': 'Hello'}), content_type='application/json')
	assert response.status_code == 404

	# Test successful send_message with receiver online
	response = client.post('/send_message', data=json.dumps({'sender': 'test@example.com', 'receiver': 'test2@example.com', 'message': 'Hello'}), content_type='application/json')
	assert response.status_code == 200
	assert app.DATABASE['messages']['test@example.com-test2@example.com'] == {'message': 'Hello', 'status': 'sent'}

	# Test successful send_message with receiver offline
	app.DATABASE['users']['test2@example.com']['online'] = False
	response = client.post('/send_message', data=json.dumps({'sender': 'test@example.com', 'receiver': 'test2@example.com', 'message': 'Hello'}), content_type='application/json')
	assert response.status_code == 200
	assert app.DATABASE['messages']['test@example.com-test2@example.com'] == {'message': 'Hello', 'status': 'queued'}
