import pytest
import json
from unittest.mock import patch
from app import app, db, sockets
from app.models import User, Message, Group, Status


@pytest.fixture
def client():
	app.config['TESTING'] = True

	with app.test_client() as client:
		yield client


@pytest.fixture
def runner():
	app.config['TESTING'] = True

	with app.app_context():
		yield app.test_cli_runner()


def test_socket_connection(client, runner):
	@sockets.socketio.on('connect')
	def on_connect():
		assert True

	@sockets.socketio.on('disconnect')
	def on_disconnect():
		assert True

	@patch('app.sockets.socketio.emit')
	def test_socket_message(client, runner, mock_emit):
		@sockets.socketio.on('message')
		def on_message(data):
			assert 'message' in data
			assert 'username' in data
			assert 'timestamp' in data
			assert 'read' in data
			assert data['read'] == True

		# Test sending and receiving of messages
		message = 'Hello, World!'
		recipient = 'test_user'
		sockets.socketio.emit('message', {'message': message, 'recipient': recipient})
		mock_emit.assert_called_with('message', {'message': message, 'recipient': recipient})

		# Test updating of read receipts
		sockets.socketio.emit('message', {'message': message, 'recipient': recipient, 'read': True})
		mock_emit.assert_called_with('message', {'message': message, 'recipient': recipient, 'read': True})

	@patch('app.sockets.socketio.emit')
	def test_socket_status(client, runner, mock_emit):
		@sockets.socketio.on('status')
		def on_status(data):
			assert 'status' in data
			assert 'username' in data
			assert 'timestamp' in data

		# Test posting of statuses
		status = 'Online'
		user = 'test_user'
		sockets.socketio.emit('status', {'status': status, 'user': user})
		mock_emit.assert_called_with('status', {'status': status, 'user': user})

		# Test emitting of notifications
		sockets.socketio.emit('status', {'status': status, 'user': user})
		mock_emit.assert_called_with('status', {'status': status, 'user': user})

	@patch('app.sockets.socketio.emit')
	def test_socket_group(client, runner, mock_emit):
		@sockets.socketio.on('group')
		def on_group(data):
			assert 'group' in data
			assert 'username' in data
			assert 'timestamp' in data
			assert 'action' in data
			assert 'notification' in data

		# Test joining and leaving of groups
		group = 'test_group'
		sockets.socketio.emit('group', {'group': group, 'action': 'join', 'notification': 'User joined the group'})
		mock_emit.assert_called_with('group', {'group': group, 'action': 'join', 'notification': 'User joined the group'})

		sockets.socketio.emit('group', {'group': group, 'action': 'leave', 'notification': 'User left the group'})
		mock_emit.assert_called_with('group', {'group': group, 'action': 'leave', 'notification': 'User left the group'})

