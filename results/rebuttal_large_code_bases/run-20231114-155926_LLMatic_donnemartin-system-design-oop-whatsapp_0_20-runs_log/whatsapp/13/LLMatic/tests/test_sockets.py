from app.app import app, socketio

def test_handle_message():
	client = socketio.test_client(app, flask_test_client=app.test_client())
	client.emit('message', {'data': 'Hello, World!'})
	received = client.get_received()
	assert len(received) == 1
	assert received[0]['name'] == 'message'
	assert received[0]['args'] == [{'data': 'Hello, World!'}]

def test_on_join():
	client = socketio.test_client(app, flask_test_client=app.test_client())
	client.emit('join', {'username': 'test_user', 'room': 'test_room'})
	received = client.get_received()
	assert len(received) == 1
	assert received[0]['name'] == 'join'
	assert received[0]['args'] == [{'username': 'test_user', 'room': 'test_room'}]

def test_on_leave():
	client = socketio.test_client(app, flask_test_client=app.test_client())
	client.emit('leave', {'username': 'test_user', 'room': 'test_room'})
	received = client.get_received()
	assert len(received) == 1
	assert received[0]['name'] == 'leave'
	assert received[0]['args'] == [{'username': 'test_user', 'room': 'test_room'}]

def test_handle_status():
	client = socketio.test_client(app, flask_test_client=app.test_client())
	client.emit('status', {'data': 'Online'})
	received = client.get_received()
	assert len(received) == 1
	assert received[0]['name'] == 'status'
	assert received[0]['args'] == [{'data': 'Online'}]
