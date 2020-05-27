import json
import time

import carrier.vantage_client as vtgclient

USERNAME = 'admin'
PASSWORD = 'admin'

POST = 'POST'
WAIT_TIME = 1
RETRIES = 10

HOST = 'http://localhost'
PORT = 5000

IMAGE = 'localhost:5001/v6-carrier-py'
METHOD = 'RPC_column_names'


def main():
    client = vtgclient.VantageClient(USERNAME, PASSWORD)

    task_input = {'method': METHOD, 'args': [], 'kwargs': {}}
    organizations = [{'id': 1, 'input': task_input}]

    task = client.post_task('column names', IMAGE, 1, organizations)

    print(task)

    for i in range(RETRIES):
        time.sleep(WAIT_TIME)
        try:
            results = client.get_results(task['id'])
            break
        except Exception as e:
            print(e)

    print(results)


if __name__ == '__main__':
    main()
