import pytest
from main import GlobalChatService

def test_global_chat_service():
	# Create instance of GlobalChatService
	global_chat_service = GlobalChatService()

	# Start the service
	global_chat_service.start_service()

	# Check if service is running
	assert global_chat_service.webapp.is_running == True

	# Stop the service
	global_chat_service.stop_service()

	# Check if service is stopped
	assert global_chat_service.webapp.is_running == False
