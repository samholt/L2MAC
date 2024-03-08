class Message:
    def __init__(self, sender, recipient, text):
        self.sender = sender
        self.recipient = recipient
        self.text = text

    def send(self):
        # In a real system, this would send the message to the recipient
        pass