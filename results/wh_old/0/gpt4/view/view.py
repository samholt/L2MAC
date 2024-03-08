from controller.user_controller import UserController
from controller.chat_controller import ChatController
from controller.notification_controller import NotificationController
from controller.encryption_controller import EncryptionController

class View:
    def __init__(self):
        self.user_controller = UserController()
        self.chat_controller = ChatController()
        self.notification_controller = NotificationController()
        self.encryption_controller = EncryptionController()
    
    def start(self):
        pass
