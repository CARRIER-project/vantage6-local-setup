# Vantage 6 local setup

Setting up your local test environment can be done as follows:

## 1. Running vantage6 server

Running the vantage6 server and gui:

```shell script
docker-compose up -d
```

## 2. Admin stuff

In order to add and use a v6 node you will have to do some administation. You can do this in the
gui.

- In your browser, go to `http://localhost:8080` and log in with username `root` and
  password `root`.
- Go to the page "organization"
- Create two new organizations. One for the v6 user and one for the node.
- Create a new collaboration and add your organizations to it. Disable encryption since it's a local
  test setup anyway.
- View your collaboration on the collaboration page, unfold it
- Press `Register node for YOUR_ORGANIZATION` for one of your organizations
- A window will pop up providing you with an api key. Copy it to somewhere safe
- Next, go to the `users` page.
- Create a new user and assign it to the other organization, give it the role of "researcher"


## 3. Install a node outside of docker

You will have to install, register and set up a node as well.
Installing the node is as follows:

```shell script
pip install vantage6==3.3.7
```

We are installing version 3.3.7 because this is the same version that is running in docker compose.

Set up a node with the command:

```shell
vnode new
```

You will need you api key. This is the key that will let the vantage6 server know the identity of
this node.

To set up a node you will have to follow the instructions from
the [vantage6 documentation](https://docs.vantage6.ai/en/main/use/node.html#use-node). You can use
the command `vnode new` to follow the wizard.

Fill in the wizard as follows:

```shell
? Please enter a configuration-name: test                                                     
? Please select the environment you want to configure:  application                           
? Enter given api-key: YOUR API KEY                                  
? The base-URL of the server: `http://host.docker.internal` (win/mac) or  http://172.17.0.1 (linux)
? Enter port to which the server listens: 5001                                                
? Path of the api: /api                                                                       
? Task directory path: /HOMEDIR/.local/share/vantage6/node/test                           
? Default database path: ABSOLUTE_PATH_TO_PROJECT/nodes/whas500.csv                                                    
? Do you want to add another database?  No                                                    
? Which level of logging would you like?  DEBUG                                               
? Do you want to connect to a VPN server?  No                                                 
? Enable encryption?  false 
```

The config file will be saved at `/HOMEDIR/.config/vantage6/node/test.yaml`

# Logging in with the vantage6 client
The docker compose includes a jupyter notebook environment where you can play around with the
vantage6 client.
Check the jupyter log by running the following in the root project directory:
```docker-compose logs -f jupyter```

You will find the link (including authentication token) in the logs.

Open the link in the browser and create a new notebook.

You will log in to your vantage6 server as follows.

Import the v6 client class:
```python
from vantage6.client import Client
```

Connect to the server:
```python
v6_client = Client("http://172.17.0.1", 5001)  # Host can be http://host.docker.internal depending on your system.
```

```python
v6_client.authenticate('your_username', 'Your_password123')
v6_client.setup_encryption(None) # We aren't using encryption
```
We're in!



# Docker registry

For development purposes you might want to run your own local docker registry:

```
# Run docker registry separately. Node tasks are run in a network separate from the node itself. By making the registry
# available from the host network it will be accessable by all docker containers
docker run -d  --name registry --network host registry:2
```

# How to test things

## Using the `run_task.py` command

The `run_task.py` script runs a custom
algorithm [available on github](https://github.com/CARRIER-project/vantage6-algorithms)
Make sure this task is published to the local registry by running `push_to_local_registry.sh` from
that repo

```
python run_task.py
```

## Using the `test_federated_learning.ipynb` notebook

If you run docker-compose up docker will automatically spin up a jupyter notebook server for you.
You can use the
`test_federated_learning.ipynb` notebook to run test tasks. You can grab the token from the
docker-compose output.
