import sys
sys.path.extend(['api.worker', 'common.file_manager'])
from common.file_manager import load_servers_list, chunker, write_to_file
from api.worker import Worker
from api.report import Report


if __name__ == '__main__':
    path = '/app/src/client/data'
    content = load_servers_list(f'{path}/servers.txt')
    w = Worker()
    for group in chunker(content, chunk_size=50):
        w.spawn_workers(group)

    write_to_file(w.output_list, f'{path}/output.json')
    r = Report(f'{path}/output.json')
    r.aggregate_df()
    print(r)
