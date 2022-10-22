from unittest import TestCase
from server_run import app
from flask import json


class FlaskTest(TestCase):
    def test_server_cache(self):
        response = app.test_client().get('/api/v1/cache')
        data = json.loads(response.get_data(as_text=True))
        self.assertIsInstance(data, dict)

    def test_server_webapp(self):
        response = app.test_client().get('/api/v1/webapp')
        data = json.loads(response.get_data(as_text=True))
        self.assertIsInstance(data, dict)

    def test_server_database(self):
        response = app.test_client().get('/api/v1/database')
        data = json.loads(response.get_data(as_text=True))
        self.assertIsInstance(data, dict)
