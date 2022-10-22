import json
import logging
from os import path


def chunker(servers: list, chunk_size: int = 10) -> iter:
    """Break list of servers based on size"""
    return (servers[pos:pos + chunk_size] for pos in range(0, len(servers), chunk_size))


def load_servers_list(file_path: str) -> list:
    """Open file with list of servers and save list in to memory"""
    assert isinstance(file_path, str), "File path should be a string type"
    try:
        with open(file_path, 'r') as servers:
            c = servers.read()
            content_list = c.split('\n')
    except FileNotFoundError as err:
        logging.exception(f'File error: {err}')
        raise
    else:
        return content_list


def write_to_file(output_list: list, file_path: str):
    """Save collected data in to a file in a json format"""
    assert isinstance(file_path, str), "File path should be a string type"
    assert isinstance(output_list, list), "Expected a list type"
    try:
        with open(file_path, 'w') as output:
            json.dump(output_list, output)
        assert path.exists(file_path)
    except Exception as err:
        logging.exception(f"File error: {err}")
        raise


if __name__ == '__main__':
    content = load_servers_list('data/servers.txt')
    for group in chunker(content, chunk_size=50):
        print(group)
