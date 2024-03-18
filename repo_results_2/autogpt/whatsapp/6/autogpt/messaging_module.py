class Message:
    def __init__(self, sender, recipient, text):
        self.sender = sender
        self.recipient = recipient
        self.text = text
        self.read_receipt = False
        self.encrypted = False

    def mark_as_read(self):
        self.read_receipt = True

    def encrypt_message(self):
        self.text = self.text[::-1]  # Simple encryption for demonstration
        self.encrypted = True

    def decrypt_message(self):
        if self.encrypted:
            self.text = self.text[::-1]
            self.encrypted = False