#!/usr/bin/env python3

import click

from carrier import VantageClient

USERNAME = 'root'
PASSWORD = 'root'
ADMIN_PASSWORD = 'admin'
COLLABORATION_ID = 1

ORGANIZATION_BASE = ORGANIZATION = {'address1': 'my address 1, Amsterdam',
                                    'country': 'the Netherlands',
                                    'zipcode': '1234ab'}


@click.command()
@click.argument('name')
def create_node(name):
    client = VantageClient(USERNAME, PASSWORD)

    # Create organization for node
    organization = dict(ORGANIZATION_BASE)
    organization['name'] = name
    result = client.post('organization', organization)
    organization_id = result['id']

    username = f'admin_{organization_id}'
    # Create user for organization
    create_user(client, organization_id, username)

    # Create node
    client = VantageClient(username, ADMIN_PASSWORD)
    result = client.post('node', {'collaboration_id': COLLABORATION_ID, 'organization_id': organization_id})
    api_key = result['api_key']

    print(f'Created new node. Api key: {api_key}')


def create_user(client, organization_id, username):
    user = {'firstname': ' ', 'lastname': ' ', 'username': username, 'organization_id': organization_id,
            'password': ADMIN_PASSWORD, 'roles': ['admin']}
    result = client.post('user', user)
    print(f'Created new user:\n{result}')


if __name__ == '__main__':
    create_node()
