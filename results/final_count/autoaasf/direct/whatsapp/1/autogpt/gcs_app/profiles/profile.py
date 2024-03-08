class UserProfile:
    def __init__(self, user_id: int, username: str, email: str, first_name: str, last_name: str, bio: str = ''):
        self.user_id = user_id
        self.username = username
        self.email = email
        self.first_name = first_name
        self.last_name = last_name
        self.bio = bio

    def update_bio(self, new_bio: str):
        self.bio = new_bio

    def get_full_name(self) -> str:
        return f'{self.first_name} {self.last_name}'