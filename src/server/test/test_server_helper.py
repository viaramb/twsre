from unittest import TestCase
from unittest.mock import patch
from server.api.server_helper import (generate_random_vars,
                                      generate_version_nums,
                                      get_server_type)


class ServerHelperTest(TestCase):
    @patch('server.api.server_helper.random.randrange')
    def test_generate_random_vars(self, mock_rr):
        expected = (1, 1, 0)
        mock_rr.return_value = 1
        results = generate_random_vars()
        self.assertEqual(results, expected)

    @patch('server.api.server_helper.random.randrange')
    def test_generate_version_nums(self, mock_rr):
        mock_rr.return_value = 1
        expected = '1.1.1'

        results = generate_version_nums('Webapp')
        self.assertEqual(results, expected)

        results = generate_version_nums('Cache')
        self.assertEqual(results, expected)

    def test_get_server_type(self):
        self.assertEqual(get_server_type(0), 'Cache')
        self.assertEqual(get_server_type(1), 'Database')
        self.assertEqual(get_server_type(2), 'Webapp')