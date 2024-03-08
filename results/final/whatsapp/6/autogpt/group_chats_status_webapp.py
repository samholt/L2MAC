from user_auth import UserManager, User
from user_profiles_contacts_messaging import UserProfile


class GroupChat:
    """A class representing a group chat."""

    def __init__(self, name):
        """Initialize a new group chat with the given name."""
        self.name = name
        self.members = set()
        self.messages = []

    def add_member(self, member):
        """Add a member to the group chat."""
        self.members.add(member)

    def remove_member(self, member):
        """Remove a member from the group chat."""
        self.members.discard(member)

    def send_message(self, sender, message):
        """Send a message to the group chat from the sender."""
        if sender not in self.members:
            return False
        self.messages.append((sender, message))
        return True


class Status:
    """A class representing a user's status."""

    def __init__(self, user, content):
        """Initialize a new status with the given user and content."""
        self.user = user
        self.content = content


class WebApp:
    """A class representing the Global Chat Service (GCS) web application."""

    def __init__(self):
        """Initialize a new GCS web application."""
        self.user_manager = UserManager()
        self.user_profiles = {}
        self.group_chats = {}
        self.statuses = {}

    def register_user(self, username, password):
        """Register a new user with the given username and password."""
        if self.user_manager.register_user(username, password):
            self.user_profiles[username] = UserProfile(self.user_manager.users[username])
            return True
        return False

    def authenticate_user(self, username, password):
        """Authenticate a user with the given username and password."""
        return self.user_manager.authenticate_user(username, password)

    def create_group_chat(self, name):
        """Create a new group chat with the given name."""
        if name in self.group_chats:
            return False
        self.group_chats[name] = GroupChat(name)
        return True

    def post_status(self, username, content):
        """Post a new status for the user with the given username and content."""
        if username not in self.user_profiles:
            return False
        self.statuses[username] = Status(self.user_profiles[username].user, content)
        return True