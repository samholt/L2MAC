document.getElementById('update-status').addEventListener('click', function() {
	var status = document.getElementById('status').value;
	fetch('/api/update_status', {
		method: 'POST',
		headers: {
			'Content-Type': 'application/json'
		},
		body: JSON.stringify({ status: status })
	})
	.then(response => response.json())
	.then(data => console.log(data));
});

document.getElementById('add-contact').addEventListener('click', function() {
	var contactEmail = document.getElementById('contact-email').value;
	fetch('/api/add_contact', {
		method: 'POST',
		headers: {
			'Content-Type': 'application/json'
		},
		body: JSON.stringify({ contact_email: contactEmail })
	})
	.then(response => response.json())
	.then(data => console.log(data));
});

document.getElementById('send-message').addEventListener('click', function() {
	var recipientEmail = document.getElementById('recipient-email').value;
	var message = document.getElementById('message').value;
	fetch('/api/send_message', {
		method: 'POST',
		headers: {
			'Content-Type': 'application/json'
		},
		body: JSON.stringify({ recipient_email: recipientEmail, message: message })
	})
	.then(response => response.json())
	.then(data => console.log(data));
});

document.getElementById('create-group').addEventListener('click', function() {
	var groupName = document.getElementById('group-name').value;
	fetch('/api/create_group', {
		method: 'POST',
		headers: {
			'Content-Type': 'application/json'
		},
		body: JSON.stringify({ group_name: groupName })
	})
	.then(response => response.json())
	.then(data => console.log(data));
});

document.getElementById('update-status-visibility').addEventListener('click', function() {
	var statusVisibility = document.getElementById('status-visibility').value;
	fetch('/api/update_status_visibility', {
		method: 'POST',
		headers: {
			'Content-Type': 'application/json'
		},
		body: JSON.stringify({ status_visibility: statusVisibility })
	})
	.then(response => response.json())
	.then(data => console.log(data));
});
