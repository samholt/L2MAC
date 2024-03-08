window.onload = function() {
	fetch('/user/' + localStorage.getItem('email'))
	.then(response => response.json())
	.then(data => {
		document.getElementById('email').textContent = 'Email: ' + data.email;
		document.getElementById('blocked_contacts').textContent = 'Blocked Contacts: ' + data.blocked_contacts.join(', ');
		document.getElementById('groups').textContent = 'Groups: ' + data.groups.map(group => group.group_name).join(', ');
		document.getElementById('messages').textContent = 'Messages: ' + data.messages.map(message => message.content).join(', ');
		document.getElementById('statuses').textContent = 'Statuses: ' + data.statuses.map(status => status.id).join(', ');
		document.getElementById('status_visibility').textContent = 'Status Visibility: ' + data.status_visibility;
	})
	.catch((error) => {
		console.error('Error:', error);
	});
}
