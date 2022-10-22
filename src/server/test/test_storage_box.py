from unittest import TestCase
from unittest.mock import patch
from server.api.storage_box import endpoint


class StorageBoxTest(TestCase):
    @patch('server.api.storage_box.random.randrange')
    @patch('server.api.storage_box.jsonify')
    @patch('server.api.storage_box.generate_version_nums')
    @patch('server.api.storage_box.generate_random_vars')
    def test__endpoint(self, mock_grv, mock_gvn, mock_j, mock_rr):
        expected = {"application": 'Cache1',
                    "version": '0.0.1',
                    "requests_count": 'request',
                    "error_count": 'error_count',
                    "success_count": 'success_count'}
        mock_grv.return_value = ('request', 'error', 'success')
        mock_gvn.return_value = '0.0.1'
        mock_rr.return_value = 1
        mock_j.return_value = expected

        results = endpoint('Cache')

        self.assertEqual(results, expected)
