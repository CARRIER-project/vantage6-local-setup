import base64
import json
import time
from typing import Dict
import vantage6.client as vtgclient

from carrier import VantageClient

USERNAME = 'admin'
PASSWORD = 'admin'

POST = 'POST'
WAIT_TIME = 1
RETRIES = 10

HOST = 'http://localhost'
PORT = 5000

IMAGE = 'localhost:5001/v6-carrier-py'


def encode_input(x: Dict[str, any]) -> str:
    s = json.dumps(x).encode()
    return str(base64.encodebytes(s))


def main():
    client = vtgclient.Client(HOST, PORT)
    client.authenticate(USERNAME, PASSWORD)
    client.setup_encryption(None)

    task_input = {'method': 'RPC_column_names', 'args': [], 'kwargs': {}}

    task = client.post_task('column names', IMAGE, 1,
                            json.dumps(task_input).encode())

    print(task)

    time.sleep(WAIT_TIME)
    results = client.get_results()

    print(results[-1])


if __name__ == '__main__':
    main()
