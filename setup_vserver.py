import requests
import json

DEFAULT_USERNAME = 'root'
DEFAULT_PASSWORD = 'root'
HOST = 'localhost'
PORT = 5000
PREFIX = 'api'
ENCODING = 'utf-8'
OK = 200
POST = 'POST'
SERVER_ROOT = f'{HOST}:{PORT}/{PREFIX}/'


def get_url(endpoint) -> str:
    return 'http://' + SERVER_ROOT + endpoint


def request(endpoint, payload, headers=None, method='GET') -> dict:
    if headers is None:
        headers = {}

    url = get_url(endpoint)

    print(f'Request url: {url}')

    headers['Content-Type'] = 'application/json'
    response = requests.request(method, url, headers=headers, data=json.dumps(payload))

    if response.status_code == OK:
        return response.json()
    else:
        raise Exception(f'Request returned status {response.status_code}\nMessage: {response.content}')


def main():
    # Get user token
    result = request('user/token', {'username': DEFAULT_USERNAME, 'password': DEFAULT_PASSWORD}, method=POST)
    access_token = result['access_token']
    bearer_token = f'Bearer {access_token}'

    # Create organization
    organization = {'address1': 'my address 1, Amsterdam',
                    'country': 'the Netherlands',
                    'name': 'NLEsC',
                    'zipcode': '1234ab'}

    result = request('organization', organization, {'Authorization': bearer_token}, POST)
    organization_id = result['id']

    print(result)


if __name__ == '__main__':
    main()
