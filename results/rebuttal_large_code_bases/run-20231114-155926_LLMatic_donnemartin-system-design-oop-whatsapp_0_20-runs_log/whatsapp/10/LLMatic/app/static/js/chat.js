document.addEventListener('DOMContentLoaded', function() {
	// chat page scripts
	var socket = new WebSocket('ws://' + window.location.host + '/ws/chat');

	socket.onmessage = function(event) {
		var data = JSON.parse(event.data);
		if (data['type'] === 'message') {
			// append the new message to the chat
			var chat = document.getElementById('chat');
			var message = document.createElement('p');
			message.textContent = data['content'];
			chat.appendChild(message);
			// update the read receipt
			data['read_receipt'] = true;
			socket.send(JSON.stringify(data));
		}
	};

	document.getElementById('send').addEventListener('click', function() {
		var content = document.getElementById('message').value;
		socket.send(JSON.stringify({
			'type': 'message',
			'content': content,
			'read_receipt': false
		}));
		document.getElementById('message').value = '';
	});
});
