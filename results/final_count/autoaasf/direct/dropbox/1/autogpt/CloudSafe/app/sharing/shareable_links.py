import uuid
import time


class ShareableLink:
    def __init__(self, file_id, expiry_date=None, password=None):
        self.id = uuid.uuid4()
        self.file_id = file_id
        self.expiry_date = expiry_date
        self.password = password

    def is_expired(self):
        if self.expiry_date:
            return time.time() > self.expiry_date
        else:
            return False

    def is_password_protected(self):
        return self.password is not None


def create_shareable_link(file_id, expiry_date=None, password=None):
    link = ShareableLink(file_id, expiry_date, password)
    # TODO: Save the shareable link to the database
    return link