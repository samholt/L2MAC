class Message:
    def __init__(self, sender, receiver, text, image=None):
        self.sender = sender
        self.receiver = receiver
        self.text = text
        self.image = image
        self.read_receipt = False

    def mark_as_read(self):
        self.read_receipt = True

    def encrypt_message(self):
        # Implementation of end-to-end encryption not included
        pass

    def add_emoji(self, emoji):
        self.text += emoji

    def add_gif(self, gif):
        self.text += gif

    def add_sticker(self, sticker):
        self.text += sticker