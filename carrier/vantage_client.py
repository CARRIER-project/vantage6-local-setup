import base64
import json
import pickle

import requests
from vantage6.client import Client

_HOST = 'http://localhost'
_PORT = 5001

HOST = 'localhost'
PORT = 5001
PREFIX = 'api'
DEFAULT_SERVER_ROOT = f'{HOST}:{PORT}/{PREFIX}/'
OK_RESPONSES = [200, 201]
DEFAULT_CONTENT_TYPE = 'application/json'
POST = 'POST'
DEFAULT_HEADERS = {'Content-Type': DEFAULT_CONTENT_TYPE}


def get_official_client(username, password):
    """
    Get official vantage6 client.

    :param username:
    :param password:
    :return:
    """
    client = Client(_HOST, _PORT)
    client.authenticate(username, password)
    client.setup_encryption(None)

    return client


class VantageClient():
    """
    Custom made vantage client to work around some problems the official has at the moment (such as authenticating root
    users).
    """

    def __init__(self, username, password):
        # Retrieve a authentication token
        self.token = self.get_token(username, password)
        self.headers = {
            'Authorization': f'Bearer {self.token}',
            'Content-Type': DEFAULT_CONTENT_TYPE
        }

    @staticmethod
    def get_url(endpoint) -> str:
        return 'http://' + DEFAULT_SERVER_ROOT + endpoint

    def get_token(self, username, password):
        result = self.request('token/user', {'username': username, 'password': password}, headers=DEFAULT_HEADERS,
                              method=POST)
        return result['access_token']

    def get(self, endpoint, payload=None, headers=None) -> dict:
        return self.request(endpoint, payload, headers, 'GET')

    def post(self, endpoint, payload, headers=None):
        print(f'Posting: {payload}')
        return self.request(endpoint, payload, headers, 'POST')

    def post_task(self, name, image, collaboration_id, organizations):
        for o in organizations:
            input_base64 = base64.b64encode(pickle.dumps(o['input']))
            o['input'] = str(input_base64, 'utf8')
            print(f'Base64 converted input: {o}')

        payload = {'collaboration_id': collaboration_id, 'image': image, 'name': name, 'organizations': organizations}
        return self.post('task', payload)

    def request(self, endpoint, payload, headers=None, method='GET') -> dict:
        if headers is None:
            headers = self.headers

        url = VantageClient.get_url(endpoint)

        print(f'Request {method} {url}')

        headers['Content-Type'] = 'application/json'
        response = requests.request(method, url, headers=headers, data=json.dumps(payload))

        if response.status_code in OK_RESPONSES:
            return response.json()
        else:
            raise Exception(f'Request returned status {response.status_code}\nMessage: {response.content}')
