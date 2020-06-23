#!/usr/bin/env python3

import time
from typing import List

import click
import pandas as pd
import vantage6.client as vtgclient

DEFAULT_USERNAME = 'admin'
DEFAULT_PASSWORD = 'admin'

DEFAULT_WAIT_TIME = 1
DEFAULT_NUM_RETRIES = 20

DEFAULT_HOST = 'http://localhost'
DEFAULT_PORT = 5001

DEFAULT_IMAGE = 'localhost:5000/v6-carrier-py'
DEFAULT_METHOD = 'correlation_matrix'
DEFAULT_COLLABORATION_ID = '1'
DEFAULT_ORGANIZATION_IDS = '1'


@click.command(context_settings={'ignore_unknown_options': True,
                                 'allow_extra_args': True},
               help='Run a task on vantage6 nodes. Optionally pass extra'
                    'keyword arguments to be passed to the algorithm'
                    '(i.e. "--key value")')
@click.option('--method', default=DEFAULT_METHOD,
              help='Method to run')
@click.option('--image', default=DEFAULT_IMAGE,
              help='Docker image to run')
@click.option('--collaboration_id', default=DEFAULT_COLLABORATION_ID,
              help='Identifier for collaboration to run task with', type=int)
@click.option('--organization_ids', default=DEFAULT_ORGANIZATION_IDS,
              help='Identifier for organization ids that should run task, '
                   'pass as comma-separated string ("1,2")')
@click.option('--username', default=DEFAULT_USERNAME)
@click.option('--password', default=DEFAULT_PASSWORD)
@click.option('--host', default=DEFAULT_HOST,
              help='Host for vantage6 server')
@click.option('--port', default=DEFAULT_PORT, type=int,
              help='Port of vantage6 server')
@click.option('--wait_time', default=DEFAULT_WAIT_TIME, type=int,
              help='Time in seconds to wait in between polling tries')
@click.option('--num_retries', default=DEFAULT_NUM_RETRIES, type=int,
              help='Number of retries for polling task results')
# Will be true if called with --master, false if called with --rpc
@click.option('--master/--rpc', default=True,
              help='--master will run a master algorithm'
                   '--rpc will run a RPC algorithm')
@click.pass_context
def main(context, method: str, image: str, collaboration_id: int,
         organization_ids: str, master: bool, username: str, password: str,
         host: str, port: int, wait_time: int, num_retries: int):
    # context.args collects unkown arguments in a list:
    # (['--unknown_var', 'value3', '--unknown_var2', 'value4'])
    kwargs = {context.args[i][2:]: context.args[i + 1]
              for i in range(0, len(context.args), 2)}

    organization_ids = [int(organization_id) for organization_id in organization_ids.split(',')]

    client = vtgclient.Client(host, port)
    client.authenticate(username, password)
    client.setup_encryption(None)

    task = client.post_task(name=method,
                            image=image,
                            collaboration_id=collaboration_id,
                            organization_ids=organization_ids,
                            input_={'method': method,
                                    'master': master,
                                    'kwargs': kwargs})

    print(task)
    results = []

    for i in range(num_retries - 1):
        print(f'Number of tries {i}')
        time.sleep(wait_time)
        try:
            results = client.get_results(task_id=task['id'])
            print(results)
            if ((len(results) > 0) or master) and all(map(lambda x: x['finished_at'], results)):
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
