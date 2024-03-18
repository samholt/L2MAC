class GroupChat:
    def __init__(self, name, picture=None):
        self.name = name
        self.picture = picture
        self.participants = []
        self.admins = []

    def add_participant(self, participant):
        self.participants.append(participant)

    def remove_participant(self, participant):
        self.participants.remove(participant)

    def assign_admin(self, participant):
        if participant in self.participants:
            self.admins.append(participant)

    def remove_admin(self, participant):
        if participant in self.admins:
            self.admins.remove(participant)