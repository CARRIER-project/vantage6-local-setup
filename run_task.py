import time

import vantage6.client as vtgclient

USERNAME = 'admin'
PASSWORD = 'admin'

POST = 'POST'
WAIT_TIME = 1
RETRIES = 10

HOST = 'http://localhost'
PORT = 5001

IMAGE = 'localhost:5000/v6-carrier-py'
METHOD = 'column_names'
COLLABORATION_ID = 1
ORGANIZATION_ID = 1


def main():
    client = vtgclient.Client(HOST, PORT)
    client.authenticate(USERNAME, PASSWORD)
    client.setup_encryption(None)

    task = client.post_task(name='Column names', image=IMAGE, collaboration_id=COLLABORATION_ID,
                            organization_ids=[ORGANIZATION_ID], input_={'method': 'column_names'})

    print(task)

    for i in range(RETRIES):
        print(f'Number of tries {i}')
        time.sleep(WAIT_TIME)
        try:
            result = client.get_results(task_id=task['id'])[0]

            if result['result']:
                print('\nReceived result:')
                print(result['result'])
                break
        except Exception as e:
            print(e)


def get_task_result_id(task):
    return task['results'][0]['id']


if __name__ == '__main__':
    main()
