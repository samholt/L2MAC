import pytest
import random
import string
from auth_service import AuthService
from user_service import UserService
from contact_service import ContactService
from group_service import GroupService
from message_service import MessageService
from group_chat_service import GroupChatService
from status_service import StatusService
from web_app_service import WebAppService
from offline_service import OfflineService
from user_status_service import UserStatusService

@pytest.fixture
def auth_service():
	return AuthService()

@pytest.fixture
def user_service():
	return UserService()

@pytest.fixture
def contact_service():
	return ContactService()

@pytest.fixture
def group_service():
	return GroupService()

@pytest.fixture
def message_service():
	return MessageService()

@pytest.fixture
def group_chat_service():
	return GroupChatService()

@pytest.fixture
def status_service():
	return StatusService()

@pytest.fixture
def web_app_service():
	return WebAppService()

@pytest.fixture
def offline_service():
	return OfflineService()

@pytest.fixture
def user_status_service():
	return UserStatusService()

@pytest.fixture
def user_emails(auth_service):
	return list(auth_service.users.keys())

@pytest.fixture
def user_id():
	return random.randint(1, 100)

@pytest.fixture
def contacts_list():
	return [random.randint(1, 100) for _ in range(10)]

@pytest.fixture
def group_id(group_service, user_id):
	return group_service.create_group(user_id, 'Test Group')

@pytest.fixture
def user_ids():
	return [random.randint(1, 100) for _ in range(10)]

# Tests go here
