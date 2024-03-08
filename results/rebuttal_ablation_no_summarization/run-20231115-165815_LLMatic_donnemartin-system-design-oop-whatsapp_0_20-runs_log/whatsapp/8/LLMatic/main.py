from auth import User
from profile import Profile
from contacts import Contact
from messaging import Messaging
from groups import GroupChat
from status import Status
from webapp import WebApp
from connectivity import Connectivity


class GlobalChatService:
	def __init__(self):
		self.auth = User('test@example.com', 'password')
		self.profile = Profile()
		self.contacts = Contact('Test')
		self.messaging = Messaging()
		self.groups = GroupChat('Test Group', 'test.jpg', ['User1', 'User2'])
		self.status = Status()
		self.webapp = WebApp()
		self.connectivity = Connectivity()

	def start_service(self):
		self.webapp.start()

	def stop_service(self):
		self.webapp.stop()


if __name__ == '__main__':
	# Create instance of GlobalChatService
	global_chat_service = GlobalChatService()

	# Start the service
	global_chat_service.start_service()
