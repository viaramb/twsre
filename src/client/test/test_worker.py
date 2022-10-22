from unittest import TestCase
from unittest.mock import patch
from client.api.worker import Worker


def request_call(*args, **kwargs):
    class MockReponse:
        def __init__(self, status_code):
            self.status_code = status_code

        def json(self):
            return {"application": "Webapp0",
                    "error_count": 1042818183,
                    "requests_count": 5194800568,
                    "success_count": 4151986202,
                    "version": "1.0.2"}

    return MockReponse(200)


class TestWorker(TestCase):
    def setUp(self) -> None:
        self.w = Worker()

    @patch('client.api.worker.random.randrange')
    def test__generate_url(self, mock_rr):
        expected = f'https://127.0.0.1:5000/api/v1/cache'
        mock_rr.return_value = 0
        results = self.w._generate_url()
        self.assertEqual(expected, results)

    @patch('client.api.worker.get_data', side_effect=request_call)
    def test__fetch(self, mock_gd):
        expected = {"application": "Webapp0",
                    "error_count": 1042818183,
                    "requests_count": 5194800568,
                    "success_count": 4151986202,
                    "version": "1.0.2"}
        mock_gd.return_value = 200
        results = self.w._fetch('https://127.0.0.1:5000/api/v1/webapp')

        self.assertEqual(results, expected)

    @patch('client.api.worker.Worker._fetch')
    @patch('client.api.worker.Worker._generate_url')
    @patch('client.api.worker.mp.Pool.apply_async')
    @patch('client.api.worker.mp.Pool')
    def test_spawn_workers(self, mock_p, mock_as, mock_gurl, mock_f):
        servers = ['server-0001']
        mock_gurl.return_value = 'https://127.0.0.1:5000/api/v1/webapp'
        mock_f.return_value = 'json data'
        self.w.spawn_workers(servers)
        mock_p.assert_called_once()
        mock_gurl.assert_called_once()
