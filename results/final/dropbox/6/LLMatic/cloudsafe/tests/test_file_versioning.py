import requests
import os
import pytest

# Mock user
user = {'id': 1, 'name': 'Test User', 'email': 'test@example.com', 'password': 'password'}

# Mock files
file1 = {'id': 1, 'name': 'file1.txt', 'size': 100, 'type': 'text/plain', 'path': 'uploads/file1.txt', 'user_id': user['id']}
file2 = {'id': 2, 'name': 'file2.txt', 'size': 200, 'type': 'text/plain', 'path': 'uploads/file2.txt', 'user_id': user['id']}

# Mock versions
version1 = {'id': 1, 'name': 'file1.txt', 'size': 100, 'type': 'text/plain', 'path': 'uploads/file1.txt', 'user_id': user['id']}
version2 = {'id': 2, 'name': 'file1.txt', 'size': 200, 'type': 'text/plain', 'path': 'uploads/file1.txt', 'user_id': user['id']}

file1['versions'] = [version1, version2]

# Mock database
files_db = {1: file1, 2: file2}

# Test file versioning
@pytest.mark.parametrize('file_id, version, expected_status_code', [
    (1, 1, 200),
    (1, 2, 200),
    (1, 3, 404),
    (2, 1, 404),
    (3, 1, 404)
])
def test_file_versioning(file_id, version, expected_status_code):
    response = requests.get(f'http://localhost:5000/download?id={file_id}&version={version}')
    assert response.status_code == expected_status_code

    if response.status_code == 200:
        assert response.headers['Content-Type'] == files_db[file_id]['versions'][version - 1]['type']
        assert int(response.headers['Content-Length']) == files_db[file_id]['versions'][version - 1]['size']
        assert response.content == open(files_db[file_id]['versions'][version - 1]['path'], 'rb').read()

