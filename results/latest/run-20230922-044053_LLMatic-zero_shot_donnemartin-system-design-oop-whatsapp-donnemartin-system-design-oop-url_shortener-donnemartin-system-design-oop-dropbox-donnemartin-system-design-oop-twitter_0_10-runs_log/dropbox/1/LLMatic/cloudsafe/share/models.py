from datetime import datetime
from typing import List


class Share:
    def __init__(self, file: str, shared_with: List[str], permissions: str, expiry_date: datetime, password_protected: bool, password: str):
        self.file = file
        self.shared_with = shared_with
        self.permissions = permissions
        self.expiry_date = expiry_date
        self.password_protected = password_protected
        self.password = password

    def generate_shareable_link(self):
        # Implement logic to generate shareable link
        pass

    def manage_shared_folder(self):
        # Implement logic to manage shared folder
        pass
