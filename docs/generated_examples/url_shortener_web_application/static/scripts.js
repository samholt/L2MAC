document.getElementById('shortenForm')?.addEventListener('submit', function(e) {
	e.preventDefault();
	const url = e.target.url.value;
	fetch('/shorten', {
		method: 'POST',
		headers: {
			'Content-Type': 'application/x-www-form-urlencoded',
		},
		body: `url=${encodeURIComponent(url)}`
	}).then(response => response.json()).then(data => {
		if(data.error) {
			document.getElementById('result').textContent = data.error;
		} else {
			document.getElementById('result').innerHTML = `Shortened URL: <a href="/${data.short_url}">${data.short_url}</a>`;
		}
	}).catch(error => console.error('Error:', error));
});

document.getElementById('registerForm')?.addEventListener('submit', function(e) {
	e.preventDefault();
	const username = e.target.username.value;
	const password = e.target.password.value;
	fetch('/register', {
		method: 'POST',
		headers: {
			'Content-Type': 'application/x-www-form-urlencoded',
		},
		body: `username=${encodeURIComponent(username)}&password=${encodeURIComponent(password)}`
	}).then(response => response.json()).then(data => {
		if(data.error) {
			document.getElementById('result').textContent = data.error;
		} else {
			document.getElementById('result').textContent = 'Registration successful. Please login.';
			setTimeout(() => window.location.href = '/login', 2000);
		}
	}).catch(error => console.error('Error:', error));
});

document.getElementById('loginForm')?.addEventListener('submit', function(e) {
	e.preventDefault();
	const username = e.target.username.value;
	const password = e.target.password.value;
	fetch('/login', {
		method: 'POST',
		headers: {
			'Content-Type': 'application/x-www-form-urlencoded',
		},
		body: `username=${encodeURIComponent(username)}&password=${encodeURIComponent(password)}`
	}).then(response => response.json()).then(data => {
		if(data.error) {
			document.getElementById('result').textContent = data.error;
		} else {
			document.getElementById('result').textContent = 'Login successful.';
			setTimeout(() => window.location.href = '/', 2000);
		}
	}).catch(error => console.error('Error:', error));
});
