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
@click.option('--org-id')
@click.option('--username')
@click.option('--password', default=ADMIN_PASSWORD)
def create_node(name, org_id, username, password):

    if not (org_id and username):

        client = VantageClient(USERNAME, PASSWORD)

    if not org_id:
        print('Creating new organization')
        org_id = create_organization(client, name)

    if not username:
        username = f'admin_{org_id}'
        print(f'Creating new user {username}')
        # Create user for organization
        create_user(client, org_id, username)

    # Create node
    client = VantageClient(username, password)
    result = client.post('node', {'collaboration_id': COLLABORATION_ID, 'organization_id': org_id})
    api_key = result['api_key']

    print(f'Created new node. Api key: {api_key}')


def create_organization(client, name):
    # Create organization for node
    organization = dict(ORGANIZATION_BASE)
    organization['name'] = name
    result = client.post('organization', organization)
    org_id = result['id']
    return org_id


def create_user(client, organization_id, username):
    user = {'firstname': ' ', 'lastname': ' ', 'username': username, 'organization_id': organization_id,
            'password': ADMIN_PASSWORD, 'roles': ['admin']}
    result = client.post('user', user)
    print(f'Created new user:\n{result}')


if __name__ == '__main__':
    create_node()
