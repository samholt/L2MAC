class Message:
    def __init__(self, sender, recipient, text, image=None):
        self.sender = sender
        self.recipient = recipient
        self.text = text
        self.image = image
        self.read = False

    def mark_as_read(self):
        self.read = True

    def encrypt(self):
        # This is a simplified version. In a real-world application, a more secure encryption method would be used.
        self.text = ''.join(chr(ord(c) + 1) for c in self.text)

    def decrypt(self):
        self.text = ''.join(chr(ord(c) - 1) for c in self.text)

class Messaging:
    def __init__(self):
        self.messages = []

    def send_message(self, sender, recipient, text, image=None):
        message = Message(sender, recipient, text, image)
        message.encrypt()
        self.messages.append(message)

    def receive_message(self, message):
        message.decrypt()
        message.mark_as_read()