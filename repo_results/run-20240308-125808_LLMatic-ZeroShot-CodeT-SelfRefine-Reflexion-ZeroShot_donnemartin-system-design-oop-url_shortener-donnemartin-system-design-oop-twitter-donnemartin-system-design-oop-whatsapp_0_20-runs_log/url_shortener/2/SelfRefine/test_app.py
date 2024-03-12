import pytest
import requests
from datetime import datetime, timedelta
from app import app, conn, c, User, URL

@pytest.fixture
def client():
	app.config['TESTING'] = True
	with app.test_client() as client:
		yield client

@pytest.fixture(autouse=True)
def setup():
	c.execute('DELETE FROM users')
	c.execute('DELETE FROM urls')
	conn.commit()

@pytest.mark.parametrize('username, password', [('user1', 'pass1'), ('user2', 'pass2')])
def test_register(client, username, password):
	response = client.post('/register', json={'username': username, 'password': password})
	assert response.status_code == 200
	assert response.get_json() == {'message': 'User registered successfully'}
	c.execute('SELECT * FROM users WHERE username=?', (username,))
	assert c.fetchone() == (username, password)

@pytest.mark.parametrize('username, password', [('user1', 'pass1'), ('user2', 'pass2')])
def test_login(client, username, password):
	c.execute('INSERT INTO users VALUES (?,?)', (username, password))
	conn.commit()
	response = client.post('/login', json={'username': username, 'password': password})
	assert response.status_code == 200
	assert response.get_json() == {'message': 'Logged in successfully'}

@pytest.mark.parametrize('original_url, short_url, username, expiration_date', [('http://google.com', 'goog', 'user1', (datetime.now() + timedelta(days=1)).strftime('%Y-%m-%d %H:%M:%S'))])
def test_shorten(client, original_url, short_url, username, expiration_date):
	c.execute('INSERT INTO users VALUES (?,?)', (username, 'pass1'))
	conn.commit()
	response = client.post('/shorten', json={'original_url': original_url, 'short_url': short_url, 'username': username, 'expiration_date': expiration_date})
	assert response.status_code == 200
	assert response.get_json() == {'message': 'URL shortened successfully'}
	c.execute('SELECT * FROM urls WHERE short_url=?', (short_url,))
	url = c.fetchone()
	assert url == (original_url, short_url, username, '[]', expiration_date)

@pytest.mark.parametrize('original_url, short_url, username, expiration_date', [('http://google.com', 'goog', 'user1', (datetime.now() + timedelta(days=1)).strftime('%Y-%m-%d %H:%M:%S'))])
def test_redirect_to_original(client, original_url, short_url, username, expiration_date):
	c.execute('INSERT INTO users VALUES (?,?)', (username, 'pass1'))
	c.execute('INSERT INTO urls VALUES (?,?,?,?,?)', (original_url, short_url, username, '[]', expiration_date))
	conn.commit()
	response = client.get('/' + short_url)
	assert response.status_code == 302
	assert response.location == original_url
	c.execute('SELECT * FROM urls WHERE short_url=?', (short_url,))
	url = c.fetchone()
	assert len(eval(url[3])) == 1

@pytest.mark.parametrize('username, password', [('user1', 'pass1'), ('user2', 'pass2')])
def test_analytics(client, username, password):
	c.execute('INSERT INTO users VALUES (?,?)', (username, password))
	conn.commit()
	response = client.get('/analytics', json={'username': username})
	assert response.status_code == 200
	assert response.get_json() == {}
