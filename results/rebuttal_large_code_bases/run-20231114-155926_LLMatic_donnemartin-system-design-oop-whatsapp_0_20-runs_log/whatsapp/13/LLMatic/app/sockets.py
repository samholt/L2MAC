from flask_socketio import emit, join_room, leave_room
from app.app import socketio, app

@socketio.on('message')
def handle_message(data):
	emit('message', data, broadcast=True)

@socketio.on('join')
def on_join(data):
	username = data['username']
	room = data['room']
	join_room(room)
	emit('message', {'username': username, 'message': username + ' has entered the room.'}, room=room)

@socketio.on('leave')
def on_leave(data):
	username = data['username']
	room = data['room']
	leave_room(room)
	emit('message', {'username': username, 'message': username + ' has left the room.'}, room=room)

@socketio.on('status')
def handle_status(data):
	emit('status', data, broadcast=True)

if __name__ == '__main__':
	socketio.run(app, debug=True)
