import requests
import json

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
NUM_NODES = 2


def get_url(endpoint) -> str:
    return 'http://' + SERVER_ROOT + endpoint


def request(endpoint, payload, headers=None, method='GET') -> dict:
    if headers is None:
        headers = {}

    url = get_url(endpoint)

    print(f'Request {method} {url}')

    headers['Content-Type'] = 'application/json'
    response = requests.request(method, url, headers=headers, data=json.dumps(payload))

    if response.status_code in OK_RESPONSES:
        return response.json()
    else:
        raise Exception(f'Request returned status {response.status_code}\nMessage: {response.content}')


def get_token(username, password):
    result = request('token/user', {'username': username, 'password': password}, method=POST)
    access_token = result['access_token']
    bearer_token = f'Bearer {access_token}'
    return bearer_token


def main():
    # Get user token
    bearer_token = get_token(DEFAULT_USERNAME, DEFAULT_PASSWORD)

    # Create organization
    organization = ORGANIZATION

    headers = {'Authorization': bearer_token}
    result = request('organization', organization, headers, POST)
    organization_id = result['id']

    print(f'Created organization with id {organization_id}')

    # Create collaboration
    collaboration = {'name': COLLABORATION_NAME, 'organization_ids': [organization_id]}
    result = request('collaboration', collaboration, headers, POST)

    collaboration_id = result['id']

    print(f'Created collaboration with id {collaboration_id}')

    # Create user tied to organization
    user = dict(ADMIN_USER)
    user['organization_id'] = organization_id
    result = request('user', user, headers, POST)

    print(f'Created new user:\n{result}')

    # Retrieve token for this new user
    bearer_token = get_token('admin', 'admin')
    headers = {'Authorization': bearer_token}

    # Create nodes
    for i in range(NUM_NODES):
        result = request('node', {'collaboration_id': collaboration_id}, headers, POST)
        node_id = result['id']
        api_key = result['api_key']

        print(f'Created node with id: {node_id}\nApi key: {api_key}')


if __name__ == '__main__':
    main()
