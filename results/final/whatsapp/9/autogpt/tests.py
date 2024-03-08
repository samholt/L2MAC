import unittest
from user_auth import UserManager
from user_profiles import ProfileManager
from contact_management import ContactManager
from messaging import MessageManager
from group_chats import GroupChatManager
from status_story import StatusStoryManager
from connectivity_offline import OfflineStorage, Connectivity


class TestGCS(unittest.TestCase):
    def setUp(self):
        self.user_manager = UserManager()
        self.profile_manager = ProfileManager()
        self.contact_manager = ContactManager()
        self.message_manager = MessageManager()
        self.group_chat_manager = GroupChatManager()
        self.status_story_manager = StatusStoryManager()
        self.offline_storage = OfflineStorage()
        self.connectivity = Connectivity(self.offline_storage)

    def test_user_registration_authentication(self):
        pass

    def test_user_profiles(self):
        pass

    def test_contact_management(self):
        pass

    def test_messaging(self):
        pass

    def test_group_chats(self):
        pass

    def test_status_story(self):
        pass

    def test_connectivity_offline(self):
        pass


if __name__ == '__main__':
    unittest.main()