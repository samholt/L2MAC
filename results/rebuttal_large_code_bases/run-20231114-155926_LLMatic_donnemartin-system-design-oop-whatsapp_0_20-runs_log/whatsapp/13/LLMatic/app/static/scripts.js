document.addEventListener('DOMContentLoaded', function() {
	var socket = io.connect(location.protocol + '//' + document.domain + ':' + location.port);

	socket.on('connect', function() {
		// Join the default group
		socket.emit('join', {group: 'default'});
	});

	socket.on('message', function(data) {
		// Append the new message to the chat box
		var chatBox = document.querySelector('.chat-box');
		var message = document.createElement('div');
		message.className = 'message';
		message.innerHTML = '<span class="username">' + data.username + '</span>: <span class="text">' + data.text + '</span>';
		chatBox.appendChild(message);
	});

	// Send a new message
	document.querySelector('#send-message').addEventListener('click', function() {
		var text = document.querySelector('#message-text').value;
		socket.emit('message', {text: text});
		document.querySelector('#message-text').value = '';
	});
});
