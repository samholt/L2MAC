import unittest
from gcs_app.status.status import Status, StatusList
from datetime import datetime, timedelta


class TestStatus(unittest.TestCase):
    def setUp(self):
        self.status_list = StatusList()
        self.status1 = Status(1, 'Hello')
        self.status2 = Status(2, 'Hi')
        self.status_list.add_status(self.status1)
        self.status_list.add_status(self.status2)

    def test_is_expired(self):
        self.status1.timestamp -= timedelta(hours=25)
        self.assertTrue(self.status1.is_expired())
        self.assertFalse(self.status2.is_expired())

    def test_remove_expired_statuses(self):
        self.status1.timestamp -= timedelta(hours=25)
        self.status_list.remove_expired_statuses()
        self.assertNotIn(self.status1, self.status_list.statuses)
        self.assertIn(self.status2, self.status_list.statuses)

    def test_get_statuses(self):
        statuses = self.status_list.get_statuses()
        self.assertEqual(len(statuses), 2)
        self.assertIn(self.status1, statuses)
        self.assertIn(self.status2, statuses)


if __name__ == '__main__':
    unittest.main()