class Status:
    def __init__(self, user_id, content):
        self.user_id = user_id
        self.content = content


class StatusManager:
    def __init__(self):
        pass

    def create_status(self, user_id, content):
        # TODO: Implement status creation logic
        pass

    def delete_status(self, status_id):
        # TODO: Implement status deletion logic
        pass

    def view_status(self, viewer_id, status_owner_id):
        # TODO: Implement status viewing logic
        pass
