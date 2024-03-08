import unittest
from gcs_app.messaging.messaging import Message, Conversation


class TestMessaging(unittest.TestCase):
    def setUp(self):
        self.conversation = Conversation(1, 2)

    def test_add_message(self):
        message = Message(1, 2, 'Hello')
        self.conversation.add_message(message)
        self.assertIn(message, self.conversation.messages)

    def test_get_messages(self):
        message1 = Message(1, 2, 'Hello')
        message2 = Message(2, 1, 'Hi')
        self.conversation.add_message(message1)
        self.conversation.add_message(message2)
        messages = self.conversation.get_messages()
        self.assertEqual(len(messages), 2)
        self.assertIn(message1, messages)
        self.assertIn(message2, messages)


if __name__ == '__main__':
    unittest.main()