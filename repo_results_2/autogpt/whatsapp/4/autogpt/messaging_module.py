class Message:
    def __init__(self, sender, recipient, text):
        self.sender = sender
        self.recipient = recipient
        self.text = text
        self.read = False

    def mark_as_read(self):
        self.read = True


class MessagingModule:
    def __init__(self):
        self.messages = []

    def send_message(self, sender, recipient, text):
        message = Message(sender, recipient, text)
        self.messages.append(message)
        return message

    def receive_message(self, message):
        message.mark_as_read()