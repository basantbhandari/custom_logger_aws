import os
import unittest
from logger import environments


class EnvironmentsTestCase(unittest.TestCase):
    """
    environment test cases
    """
    def setUp(self):
        os.environ["log_mode"] = "1"
        os.environ["log_date_format"] = "%Y-%m-%d %H:%M:%S"

    def tearDown(self):
        del os.environ["log_mode"]
        del os.environ["log_date_format"]

    def test_environment_variable_set(self):
        self.assertEqual(environments.log_mode, 1)
        self.assertEqual(environments.log_date_time_format, "%Y-%m-%d %H:%M:%S")


if __name__ == '__main__':
    unittest.main()
