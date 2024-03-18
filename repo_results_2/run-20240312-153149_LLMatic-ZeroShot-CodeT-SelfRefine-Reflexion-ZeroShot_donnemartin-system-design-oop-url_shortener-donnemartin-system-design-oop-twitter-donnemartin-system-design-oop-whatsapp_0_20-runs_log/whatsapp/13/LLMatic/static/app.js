$(document).ready(function() {
	$('#send-message-form').on('submit', function(e) {
		e.preventDefault();
		var message = $('#message-input').val();
		$.ajax({
			url: '/send_message',
			type: 'POST',
			contentType: 'application/json',
			data: JSON.stringify({ 'message_id': Date.now().toString(), 'text': message }),
			success: function(response) {
				$('#message-container').append('<p>' + message + '</p>');
				$('#message-input').val('');
				if (response.status === 'message queued') {
					$('#status').text('Offline. Message queued.');
				} else {
					$('#status').text('Online.');
				}
			},
			error: function(error) {
				console.log(error);
			}
		});
	});
});
