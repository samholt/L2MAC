class Invitation:
    def __init__(self, sender, recipient_email, file_id, permissions):
        self.sender = sender
        self.recipient_email = recipient_email
        self.file_id = file_id
        self.permissions = permissions


def send_invitation(sender, recipient_email, file_id, permissions):
    invitation = Invitation(sender, recipient_email, file_id, permissions)
    # TODO: Send the invitation via email
    return invitation