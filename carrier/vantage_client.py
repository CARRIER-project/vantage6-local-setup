import requests
import json
import base64

HOST = 'localhost'
PORT = 5000
PREFIX = 'api'
DEFAULT_SERVER_ROOT = f'{HOST}:{PORT}/{PREFIX}/'
OK_RESPONSES = [200, 201]
DEFAULT_CONTENT_TYPE = 'application/json'
POST = 'POST'
DEFAULT_HEADERS = {'Content-Type': DEFAULT_CONTENT_TYPE}


class VantageClient():

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

    def get(self, endpoint, payload, headers=None) -> dict:
        return self.request(endpoint, payload, headers, 'GET')

    def post(self, endpoint, payload, headers=None):
        return self.request(endpoint, payload, headers, 'POST')

    def post_task(self, name, image, collaboration_id, organizations):
        for o in organizations:
            input_base64 = base64.encodebytes(json.dumps(o['input']).encode())
            o['input'] = str(input_base64)

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
