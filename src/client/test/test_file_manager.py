import types
import os
import platform
from unittest import TestCase
from client.common.file_manager import (chunker,
                                        load_servers_list,
                                        write_to_file)


class TestFileManager(TestCase):
    def setUp(self) -> None:
        if platform.system() == 'Windows':
            self.servers_list = '../data/servers.txt'
            self.output = '../data/output.json'
        else:
            self.servers_list = '/app/src/client/data/servers.txt'
            self.output = '/app/src/client/data/output.json'

    def test_chunker(self):
        servers = ['server-0001',
                   'server-0002',
                   'server-0003',
                   'server-0004']
        results = chunker(servers, chunk_size=2)
        self.assertIsInstance(results, types.GeneratorType)

    def test_load_servers_list_ok(self):
        expected = ['server-0001', 'server-0002', 'server-0003']
        results = load_servers_list(self.servers_list)
        self.assertEqual(expected, results[:3])

    def test_load_servers_list_exception(self):
        self.assertRaises(FileNotFoundError, lambda: load_servers_list('no_file'))

    def test_write_to_file_ok(self):
        output_list = [{"application": "Webapp1",
                        "error_count": 1042811524,
                        "requests_count": 5194800879,
                        "success_count": 4151986925,
                        "version": "0.0.1"}]
        write_to_file(output_list, self.output)
        self.assertTrue(os.path.exists(self.output))
