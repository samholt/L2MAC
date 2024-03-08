import unittest
from gcs_app.group_chats.group_chat import GroupChat
from gcs_app.messaging.messaging import Message


class TestGroupChats(unittest.TestCase):
    def setUp(self):
        self.group_chat = GroupChat(1, 'Test Group')

    def test_add_member(self):
        self.group_chat.add_member(1)
        self.assertIn(1, self.group_chat.members)

    def test_remove_member(self):
        self.group_chat.add_member(1)
        self.group_chat.remove_member(1)
        self.assertNotIn(1, self.group_chat.members)

    def test_add_message(self):
        message = Message(1, 2, 'Hello')
        self.group_chat.add_message(message)
        self.assertIn(message, self.group_chat.messages)

    def test_get_messages(self):
        message1 = Message(1, 2, 'Hello')
        message2 = Message(2, 1, 'Hi')
        self.group_chat.add_message(message1)
        self.group_chat.add_message(message2)
        messages = self.group_chat.get_messages()
        self.assertEqual(len(messages), 2)
        self.assertIn(message1, messages)
        self.assertIn(message2, messages)


if __name__ == '__main__':
    unittest.main()