class ChatController:
    def __init__(self, user):
        self.user = user
        self.active_chat = None

    def create_chat(self, participants):
        chat = Chat(chat_id=len(participants), participants=participants)
        self.active_chat = chat
        return chat

    def send_message(self, content):
        if self.active_chat:
            message = Message(message_id=len(self.active_chat.messages), sender=self.user, content=content, timestamp=None)
            self.active_chat.add_message(message)

    def delete_message(self, message_id):
        if self.active_chat:
            self.active_chat.remove_message(message_id)