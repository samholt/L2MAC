from flask_socketio import SocketIO, send, join_room, leave_room

# Initialize SocketIO
socketio = SocketIO()

# Mock database
messages = {}
groups = {}

@socketio.on('message')
def handle_message(data):
	# Handle incoming messages
	# Send message to recipient
	recipient = data['recipient']
	message = data['message']
	if recipient not in messages:
		messages[recipient] = []
	messages[recipient].append({'message': message, 'read': False})
	# Emit the message to the recipient
	send(message, room=recipient)

	# Update the read receipt
	data['read'] = True

@socketio.on('group')
def handle_group(data):
	# Handle group actions
	# Join or leave a group
	if data['action'] == 'join':
		join_room(data['group'])
	elif data['action'] == 'leave':
		leave_room(data['group'])
	# Emit a notification to the participants when a group is updated
	if data['group'] not in groups:
		groups[data['group']] = []
	groups[data['group']].append(data['notification'])
	send(data['notification'], room=data['group'])

@socketio.on('status')
def handle_status(data):
	# Handle status updates
	# Update user status
	# This is a mock implementation, in a real application this would interact with a database
	user_status = {}
	user_status[data['user']] = data['status']
	# Broadcast the new status to all clients
	send(user_status)
