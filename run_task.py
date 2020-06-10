import time
from typing import List

import vantage6.client as vtgclient

USERNAME = 'admin_3'
PASSWORD = 'admin'

POST = 'POST'
WAIT_TIME = 1
RETRIES = 20

HOST = 'http://localhost'
PORT = 5001

IMAGE = 'localhost:5000/v6-carrier-py'
METHOD = 'column_names'
COLLABORATION_ID = 1
ORGANIZATION_IDS = [1, 2]
MASTER = False
NUM_NODES = 2


def main():
    client = vtgclient.Client(HOST, PORT)
    client.authenticate(USERNAME, PASSWORD)
    client.setup_encryption(None)

    task = client.post_task(name='Column names', image=IMAGE, collaboration_id=COLLABORATION_ID,
                            organization_ids=ORGANIZATION_IDS, input_={'method': METHOD, 'master': MASTER})

    print(task)

    for i in range(RETRIES):
        print(f'Number of tries {i}')
        time.sleep(WAIT_TIME)
        try:
            results = client.get_results(task_id=task['id'])
            print(results)
            if ((len(results) == NUM_NODES) or MASTER) and all(map(lambda x: x['finished_at'], results)):
                print('\nReceived result:')
                print_result(results)
                break
        except Exception as e:
            print(e)


def print_result(result: List[any]):
    for idx, r in enumerate(result):
        print(f'{idx}: {r["result"]}')


def get_task_result_id(task):
    return task['results'][0]['id']


if __name__ == '__main__':
    main()
