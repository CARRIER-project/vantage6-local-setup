# Vantage6 installation

Install:
```shell
virtualenv venv
source venv/bin/activate
pip install vantage6
```

Configure server:
```shell
# --user parameter makes sure config is stored in user directory, not system wide
vserver new --user # Wizard prompts you for basic info

vserver start --user
```

At the first run, a new user will be created:
```
username: root
password: root

```
In order to get access to the REST api you will need to request a user token:

```shell
# Get your user token
curl --location --request POST 'localhost:5000/api/token/user' \
--header 'Content-Type: application/json' \
--data-raw '{
  "username": "root",
  "password": "root"
}'

```

Now you can configure your organization, collaboration and node.
This can also be done by importing a configuration file, but using the REST api ensures
the input is validated, which is nice when trying out vantage6 for the first time.

Make sure to replace `YOUR_API_KEY` with the key received in the previous step.

```shell
# Organization

curl --location --request POST 'localhost:5000/api/organization' \
--header 'Authorization: Bearer YOUR_API_KEY' \
--header 'Content-Type: application/json' \
--data-raw '{
  "address1": "Some Street 11, Amsterdam",
  "country": "Netherlands",
  "name": "escience center",
  "zipcode": "1234ab"
}'

# Collaboration
curl --location --request POST 'localhost:5000/api/collaboration' \
--header 'Authorization: Bearer YOUR_API_KEY' \
--header 'Content-Type: application/json' \
--data-raw '{
    "name": "collab1",
    "organization_ids": [
        1
    ]
}'

# Add organization to collaboration

curl --location --request POST 'localhost:5000/api/collaboration/1/organization' \
--header 'Authorization: Bearer YOUR_API_KEY' \
--header 'Content-Type: application/json' \
--data-raw '{"id": 1}'


# Create user tied to organization

curl --location --request POST 'localhost:5000/api/user' \
--header 'Authorization: Bearer YOUR_API_KEY' \
--header 'Content-Type: application/json' \
--data-raw '{
	
  "firstname": "djura",
  "lastname": "smits",
  "password": "admin",
  "organization_id": "1",
  "username": "admin",
  "roles": ["admin"]

}'

# Now retrieve token for this new user
#
#
#

# Node
# Create node
curl --location --request POST 'localhost:5000/api/node' \
--header 'Authorization: Bearer YOUR_API_KEY' \
--header 'Content-Type: application/json' \
--data-raw '{
	"collaboration_id": 1
}'

```
Check the api key that you have received and use that for your configuration of the vnode.

```bash
vnode new # Follow wizard and specify api key
```
