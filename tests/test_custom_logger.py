import unittest
from unittest.mock import patch
from logger.custom_logger import CustomLogger


class CustomLoggerTestCase(unittest.TestCase):
    """
    tests cases for custom logger class
    """

    @patch('logger.custom_logger.get_current_date_time_str')
    @patch('logger.custom_logger.get_calling_module_name')
    @patch('logger.custom_logger.environments')
    @patch('logger.custom_logger.display_log')
    def test_debug_log_displayed(self,
                                 mock_display_log,
                                 mock_environments,
                                 mock_get_calling_module_name,
                                 mock_get_current_date_time_str):
        # assumption
        mock_environments.log_mode = 1
        mock_get_calling_module_name.return_value = "main.py"
        mock_get_current_date_time_str.return_value = "2020:10:10 10:02:10"

        CustomLogger.debug("Debug message")
        self.assertTrue(mock_display_log.called)

    @patch('logger.custom_logger.get_current_date_time_str')
    @patch('logger.custom_logger.get_calling_module_name')
    @patch('logger.custom_logger.environments')
    @patch('logger.custom_logger.display_log')
    def test_info_log_displayed(self,
                                mock_display_log,
                                mock_environments,
                                mock_get_calling_module_name,
                                mock_get_current_date_time_str):
        # assumption
        mock_environments.log_mode = 1
        mock_get_calling_module_name.return_value = "main.py"
        mock_get_current_date_time_str.return_value = "2020:10:10 10:02:10"

        CustomLogger.info("info message")
        self.assertTrue(mock_display_log.called)

    @patch('logger.custom_logger.get_current_date_time_str')
    @patch('logger.custom_logger.get_calling_module_name')
    @patch('logger.custom_logger.environments')
    @patch('logger.custom_logger.display_log')
    def test_warning_log_displayed(self,
                                   mock_display_log,
                                   mock_environments,
                                   mock_get_calling_module_name,
                                   mock_get_current_date_time_str):
        # assumption
        mock_environments.log_mode = 1
        mock_get_calling_module_name.return_value = "main.py"
        mock_get_current_date_time_str.return_value = "2020:10:10 10:02:10"

        CustomLogger.warning("warning message")
        self.assertTrue(mock_display_log.called)

    @patch('logger.custom_logger.get_current_date_time_str')
    @patch('logger.custom_logger.get_calling_module_name')
    @patch('logger.custom_logger.environments')
    @patch('logger.custom_logger.display_log')
    def test_error_log_displayed(self,
                                 mock_display_log,
                                 mock_environments,
                                 mock_get_calling_module_name,
                                 mock_get_current_date_time_str):
        # assumption
        mock_environments.log_mode = 1
        mock_get_calling_module_name.return_value = "main.py"
        mock_get_current_date_time_str.return_value = "2020:10:10 10:02:10"

        CustomLogger.error("error message")
        self.assertTrue(mock_display_log.called)

    @patch('logger.custom_logger.get_current_date_time_str')
    @patch('logger.custom_logger.get_calling_module_name')
    @patch('logger.custom_logger.environments')
    @patch('logger.custom_logger.display_log')
    def test_critical_log_displayed(self,
                                    mock_display_log,
                                    mock_environments,
                                    mock_get_calling_module_name,
                                    mock_get_current_date_time_str):
        # assumption
        mock_environments.log_mode = 1
        mock_get_calling_module_name.return_value = "main.py"
        mock_get_current_date_time_str.return_value = "2020:10:10 10:02:10"

        CustomLogger.critical("critical message")
        self.assertTrue(mock_display_log.called)


if __name__ == '__main__':
    unittest.main()
