import pytest
import app
from app import User, Club, Book, Meeting, Discussion, Resource

@pytest.fixture
def client():
    app.app.config['TESTING'] = True
    with app.app.test_client() as client:
        yield client

def test_create_user(client):
    rv = client.post('/users', json={'id': 1, 'name': 'John Doe', 'email': 'john@example.com', 'read_list': [], 'clubs': []})
    assert rv.status_code == 201
    assert rv.get_json() == {'id': 1}

def test_create_club(client):
    rv = client.post('/clubs', json={'id': 1, 'name': 'Book Club', 'description': 'A club for book lovers', 'is_private': False, 'members': [], 'books': []})
    assert rv.status_code == 201
    assert rv.get_json() == {'id': 1}

def test_create_book(client):
    rv = client.post('/books', json={'id': 1, 'title': 'Book Title', 'author': 'Book Author'})
    assert rv.status_code == 201
    assert rv.get_json() == {'id': 1}

def test_create_meeting(client):
    rv = client.post('/meetings', json={'id': 1, 'club_id': 1, 'book_id': 1, 'date': '2022-01-01'})
    assert rv.status_code == 201
    assert rv.get_json() == {'id': 1}

def test_create_discussion(client):
    rv = client.post('/discussions', json={'id': 1, 'club_id': 1, 'book_id': 1, 'user_id': 1, 'comment': 'This is a comment'})
    assert rv.status_code == 201
    assert rv.get_json() == {'id': 1}

def test_create_resource(client):
    rv = client.post('/resources', json={'id': 1, 'title': 'Resource Title', 'link': 'http://example.com'})
    assert rv.status_code == 201
    assert rv.get_json() == {'id': 1}
