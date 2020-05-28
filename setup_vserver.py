from typing import List, Dict

import requests
import json
from carrier import VantageClient

ORGANIZATION = {'address1': 'my address 1, Amsterdam',
                'country': 'the Netherlands',
                'name': 'NLEsC',
                'zipcode': '1234ab'}
ADMIN_USER = {'firstname': 'djura',
              'lastname': 'smits',
              'password': 'admin',
              'username': 'admin',
              'roles': ['admin']
              }

DEFAULT_USERNAME = 'root'
DEFAULT_PASSWORD = 'root'
HOST = 'localhost'
PORT = 5000
PREFIX = 'api'
ENCODING = 'utf-8'
OK_RESPONSES = [200, 201]
POST = 'POST'
SERVER_ROOT = f'{HOST}:{PORT}/{PREFIX}/'
COLLABORATION_NAME = 'collab1'
NUM_NODES = 1
TASKS = 'tasks.json'

COLLABORATION_ID = 1


def get_tasks() -> List[Dict[str, any]]:
    with open(TASKS, 'r') as f:
        return json.load(f)


def main():
    client = VantageClient(DEFAULT_USERNAME, DEFAULT_PASSWORD)

    # Create organization
    organization = ORGANIZATION

    result = client.post('organization', organization)
    organization_id = result['id']

    print(f'Created organization with id {organization_id}')

    # Create collaboration
    collaboration = {'name': COLLABORATION_NAME, 'organization_ids': [organization_id], 'id': COLLABORATION_ID}
    result = client.post('collaboration', collaboration)

    collaboration_id = result['id']

    print(f'Created collaboration with id {collaboration_id}')

    # Create user tied to organization
    # Might already exist
    try:
        user = dict(ADMIN_USER)
        user['organization_id'] = organization_id
        result = client.post('user', user)
    except Exception as e:
        print(e)

    print(f'Created new user:\n{result}')

    # Authenticate new user
    client = VantageClient('admin', 'admin')

    # Create nodes
    for i in range(NUM_NODES):
        result = client.post('node', {'collaboration_id': collaboration_id})

        print(f'Created node with id: {result}')


if __name__ == '__main__':
    main()
