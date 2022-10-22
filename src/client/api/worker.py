import multiprocessing as mp
import random

try:
    from common.collector import get_data
    from common.file_manager import write_to_file
    from common.client_helper import generate_endpoint
except ModuleNotFoundError as err:
    from client.common.collector import get_data
    from client.common.file_manager import write_to_file
    from client.common.client_helper import generate_endpoint


class Worker:
    def __init__(self):
        self._output_list = []

    @property
    def output_list(self) -> list:
        return self._output_list

    @output_list.setter
    def output_list(self, result: dict):
        self._output_list.append(result)

    def _generate_url(self, server: str = '127.0.0.1') -> str:
        """Create URL to connect to REST Api endpoint"""
        server = '127.0.0.1'  # NOTE: in a real world scenario this line should be commented or deleted.
        endpoint = generate_endpoint(random.randrange(0, 3))
        return f"https://{server}:5000/api/v1/{endpoint}"

    def _fetch(self, url: str = None):
        """Connect to server and get components status"""
        r = get_data(url)
        if r.status_code == 200:
            return r.json()

    def _append_to_list(self, result: dict):
        """After REST connection is completed append result to output_list"""
        self.output_list = result

    def spawn_workers(self, group: list):
        """Multiprocess function to generate a number of jobs to collect REST Api data"""

        pool = mp.Pool()
        for server in group:
            url = self._generate_url(server)
            pool.apply_async(self._fetch, args=(url,), callback=self._append_to_list)

        pool.close()
        pool.join()


if __name__ == '__main__':
    from src.client.common.file_manager import load_servers_list, chunker
    content = load_servers_list('../data/servers.txt')
    w = Worker()
    for group in chunker(content, chunk_size=50):
        w.spawn_workers(group)

    write_to_file(w.output_list, '../data/output.json')


