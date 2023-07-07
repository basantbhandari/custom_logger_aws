import unittest
import inspect
from logger.log_utils import get_calling_module_name, get_current_date_time_str, display_log


class LogUtilsCase(unittest.TestCase):
    def test_get_calling_module_name(self):
        result = get_calling_module_name(inspect.stack())
        self.assertEqual(result, "case.py")

    def test_get_current_date_time_str(self):
        result = get_current_date_time_str()
        self.assertIsInstance(result, str)

    def test_display_log_failure(self):
        display_log(log_mode="DEBUG",
                    calling_module="main.py",
                    date_time="2020:10:10 10:10:10",
                    message="debug message")
        self.assertEquals(None, None)


if __name__ == '__main__':
    unittest.main()
