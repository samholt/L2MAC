import unittest
import app


class TestApp(unittest.TestCase):
	def test_hello_world(self):
		self.assertEqual(app.hello_world(), 'Hello, World!')


if __name__ == '__main__':
	unittest.main()
