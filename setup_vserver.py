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
NUM_NODES = 2
TASKS = 'tasks.json'
ORGANIZATION_PREFIX = 'NLESC '

COLLABORATION_ID = 1


def get_tasks() -> List[Dict[str, any]]:
    with open(TASKS, 'r') as f:
        return json.load(f)


def main():
    client = VantageClient(DEFAULT_USERNAME, DEFAULT_PASSWORD)

    organization_ids = []
    # Every node needs its own organization. User triggering tasks will have separate organization
    for n in range(NUM_NODES + 1):
        organization = ORGANIZATION

        result = client.post('organization', organization)
        organization_id = result['id']
        organization_ids.append(organization_id)

        print(f'Created organization with id {organization_id}')

    # Create collaboration
    collaboration = {'name': COLLABORATION_NAME, 'organization_ids': organization_ids, 'id': COLLABORATION_ID}
    result = client.post('collaboration', collaboration)

    collaboration_id = result['id']

    print(f'Created collaboration with id {collaboration_id}')

    # Create user tied to organization
    # Might already exist
    usernames = []

    for id in organization_ids:
        try:
            username = f'admin_{id}'
            create_user(client, id, username)
            usernames.append(username)
        except Exception as e:
            print(e)

    # Authenticate new user and create new nodes
    for name in usernames:
        client = VantageClient(name, 'admin')

        # Create node
        result = client.post('node', {'collaboration_id': collaboration_id})

        print(f'Created node with id: {result}')


def create_user(client, organization_id, username):
    user = dict(ADMIN_USER)
    user['username'] = username
    user['organization_id'] = organization_id
    result = client.post('user', user)
    print(f'Created new user:\n{result}')


if __name__ == '__main__':
    main()
