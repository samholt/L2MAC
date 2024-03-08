class ChatView:
    def __init__(self, chat):
        self.chat = chat

    def display_messages(self):
        for message in self.chat.messages:
            print(f'{message.sender.username}: {message.content}')

    def update_message_status(self, message_id, status):
        for message in self.chat.messages:
            if message.message_id == message_id:
                message.status = status
                break