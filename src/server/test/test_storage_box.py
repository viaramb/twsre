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
                    "requests_count": 1000,
                    "error_count": 10,
                    "success_count": 990}
        mock_grv.return_value = (1000, 10, 990)
        mock_gvn.return_value = '0.0.1'
        mock_rr.return_value = 1
        mock_j.return_value = expected

        results = endpoint('Cache')

        self.assertEqual(results, expected)
