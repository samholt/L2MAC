import dataclasses

@dataclasses.dataclass
class Post:
    user: User
    content: str
    interactions: dict

    def create_post(self, user, content):
        self.user = user
        self.content = content
        self.interactions = {}

    def interact_with_post(self, user, interaction):
        self.interactions[user] = interaction

    def filter_content(self, filter_criteria):
        return self.content.contains(filter_criteria)

    def search_content(self, search_criteria):
        return self.content.contains(search_criteria)