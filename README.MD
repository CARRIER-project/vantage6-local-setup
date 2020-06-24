# Vantage 6 local setup

## Running the local setup
Simply run:
```shell script
docker-compose up --force-recreate

# Populate 'escience' node rdf store with sample data
./nodes/escience/populate-rdf-store.sh
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
