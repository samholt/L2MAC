import pytest
import requests
import os

base_url = 'http://localhost:5000'

# Mock user and folder data
user_data = {'name': 'Test User', 'email': 'test@example.com', 'password': 'password'}
folder_data = {'name': 'Test Folder', 'user_id': 1}
file_data = {'name': 'test_file.txt', 'user_id': 1}

# Test creating a folder
response = requests.post(f'{base_url}/create-folder', json=folder_data)
assert response.status_code == 201
assert response.json()['message'] == 'Folder created successfully'

# Test renaming a folder
rename_data = {'id': 1, 'new_name': 'Renamed Folder'}
response = requests.post(f'{base_url}/rename', json=rename_data)
assert response.status_code == 200
assert response.json()['message'] == 'Renamed successfully'

# Test moving a folder
move_data = {'id': 1, 'new_path': '/new/path'}
response = requests.post(f'{base_url}/move', json=move_data)
assert response.status_code == 200
assert response.json()['message'] == 'Moved successfully'

# Test deleting a folder
delete_data = {'id': 1}
response = requests.post(f'{base_url}/delete', json=delete_data)
assert response.status_code == 200
assert response.json()['message'] == 'Deleted successfully'
