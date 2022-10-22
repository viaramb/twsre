from unittest import TestCase
from unittest.mock import patch
from client.common.collector import get_data
from requests.exceptions import HTTPError


def request_call(*args, **kwargs):
    class MockReponse:
        def __init__(self, status_code):
            self.status_code = status_code
            self.raise_for_status = object

    return MockReponse(200)


def request_bad_call(*args, **kwargs):
    class MockReponse:
        def __init__(self, status_code):
            self.status_code = status_code

        def raise_for_status(self):
            if 400 >= self.status_code:
                raise HTTPError

    return MockReponse(200)


class TestCollector(TestCase):
    @patch('client.common.collector.requests.get', side_effect=request_call)
    def test_get_data_ok(self, mock_get):
        mock_get.raise_for_status.return_value = 200
        results = get_data('https://myurl.io')
        self.assertEqual(results.status_code, 200)

    @patch('client.common.collector.requests.get', side_effect=request_bad_call)
    def test_get_data_exception(self, mock_get):
        mock_get.raise_for_status.return_value = 400
        self.assertRaises(HTTPError, lambda: get_data('https://myurl.io'))
