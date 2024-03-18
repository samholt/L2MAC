class GroupChat:
    def __init__(self, name, admin):
        self.name = name
        self.admin = admin
        self.participants = [admin]
        self.picture = None

    def add_participant(self, participant):
        self.participants.append(participant)

    def remove_participant(self, participant):
        self.participants.remove(participant)

    def set_picture(self, picture):
        self.picture = picture