# Vantage 6 local setup

## If you're running for the first time
```shell script
# Run only vserver and database
docker-compose up -d vserver

# Setup organisation account and node
python setup_vserver.py
```
The last command will register a new node on the server and display its information. Copy the string found for `api_key`.
Now, open `mumc-node-config.yml` in your favorite editor and paste your copied api key after `api_key`. If there is
already an api key there you can replace it.

## Running the local setup
If you have already done the steps for first-time setup you can simply run:
```shell script
docker-compose up -d
```

# Executing a task
When your docker setup is running you can execute a task using `run_task.py`. Replace the value in `IMAGE` with your 
desired docker image

# Docker registry
For development purposes you might want to run your own local docker registry:
```
# Run docker registry separately. Node tasks are run in a network separate from the node itself. By making the registry
# available from the host network it will be accessable by all docker containers
docker run -d  --name registry --network host registry:2 
```

The `run_task.py` script runs a custom algorithm [available on github](https://github.com/CARRIER-project/vantage6-algorithms)
Make sure this task is published to the local registry by running `push_to_local_registry.sh` from that repo

```
python run_task.py
```
