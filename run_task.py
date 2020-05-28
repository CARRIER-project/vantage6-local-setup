import base64
import time
import pickle
import carrier.vantage_client as vtgclient

USERNAME = 'admin'
PASSWORD = 'admin'

POST = 'POST'
WAIT_TIME = 5
RETRIES = 10

HOST = 'http://localhost'
PORT = 5000

IMAGE = 'localhost:5000/v6-carrier-py'
METHOD = 'column_names'


def main():
    client = vtgclient.VantageClient(USERNAME, PASSWORD)

    task_input = {'method': METHOD, 'args': [], 'kwargs': {}}
    organizations = [{'id': 1, 'input': task_input}]

    # Using my own client because official python client fails for non-encrypted connections
    task = client.post_task('column names', IMAGE, 1, organizations)

    print(task)

    for i in range(RETRIES):
        time.sleep(WAIT_TIME)
        try:
            result = client.get(f'result/{get_task_result_id(task)}')

            output = result['result']
            if output:
                output = pickle.loads(base64.decodebytes(output.encode('ascii')))
                print(f'Result: {output}')
                break
        except Exception as e:
            print(e)


def get_task_result_id(task):
    return task['results'][0]['id']


if __name__ == '__main__':
    main()
