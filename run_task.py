#!/usr/bin/env python3

import time
from typing import List

import pandas as pd
import vantage6.client as vtgclient

USERNAME = 'admin'
PASSWORD = 'admin'

POST = 'POST'
WAIT_TIME = 1
RETRIES = 20

HOST = 'http://localhost'
PORT = 5001

IMAGE = 'localhost:5000/v6-carrier-py'
METHOD = 'get_printable_graph'
COLLABORATION_ID = 1
ORGANIZATION_IDS = [1]  # [2, 3, 6]
MASTER = False
NUM_NODES = 1


def main():
    client = vtgclient.Client(HOST, PORT)
    client.authenticate(USERNAME, PASSWORD)
    client.setup_encryption(None)

    task = client.post_task(name=METHOD, image=IMAGE, collaboration_id=COLLABORATION_ID,
                            organization_ids=ORGANIZATION_IDS,
                            input_={'method': METHOD, 'master': MASTER, 'kwargs': {'exclude_orgs': ORGANIZATION_IDS}})

    print(task)
    results = []

    for i in range(RETRIES):
        print(f'Number of tries {i}')
        time.sleep(WAIT_TIME)
        try:
            results = client.get_results(task_id=task['id'])
            print(results)
            if ((len(results) > 0) or MASTER) and all(map(lambda x: x['finished_at'], results)):
                print('\nReceived result:')
                print_result(results)
                break
        except Exception as e:
            print(e)

    print_logs(results)


def print_logs(results):
    for r in results:
        print(f'Log for organization {r["organization"]["id"]}')
        print(r['log'])


def print_result(result: List[any]):
    for idx, r in enumerate(result):
        result_data = r['result']
        if isinstance(result_data, pd.DataFrame):
            print(f'{idx}:\n{result_data.to_string()}')
        else:
            print(f'{idx}: {result_data}')


def get_task_result_id(task):
    return task['results'][0]['id']


if __name__ == '__main__':
    main()
