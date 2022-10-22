from unittest import TestCase
from client.common.client_helper import generate_endpoint


class TestClientHelper(TestCase):
    def test_generate_endpoint(self):
        self.assertEqual(generate_endpoint(0), 'cache')
        self.assertEqual(generate_endpoint(1), 'database')
        self.assertEqual(generate_endpoint(2), 'webapp')
