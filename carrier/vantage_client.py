import requests
import json

HOST = 'localhost'
PORT = 5000
PREFIX = 'api'
DEFAULT_SERVER_ROOT = f'{HOST}:{PORT}/{PREFIX}/'
OK_RESPONSES = [200, 201]
DEFAULT_CONTENT_TYPE = 'application/json'
POST = 'POST'


class VantageClient():

    def __init__(self, username, password):
        # Retrieve a authentication token
        self.token = VantageClient.get_token(username, password)
        self.default_headers = {
            'Authorization': f'Bearer {self.token}',
            'Content-Type': DEFAULT_CONTENT_TYPE
        }

    @staticmethod
    def get_url(endpoint) -> str:
        return 'http://' + DEFAULT_SERVER_ROOT + endpoint

    @staticmethod
    def get_token(username, password):
        result = VantageClient.request('token/user', {'username': username, 'password': password}, method=POST)
        return result['access_token']

    def request(self, endpoint, payload, headers=None, method='GET') -> dict:
        if headers is None:
            headers = self.default_headers

        url = VantageClient.get_url(endpoint)

        print(f'Request {method} {url}')

        headers['Content-Type'] = 'application/json'
        response = requests.request(method, url, headers=headers, data=json.dumps(payload))

        if response.status_code in OK_RESPONSES:
            return response.json()
        else:
            raise Exception(f'Request returned status {response.status_code}\nMessage: {response.content}')
