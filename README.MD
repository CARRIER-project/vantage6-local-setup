# Vantage 6 local setup

## Running the local setup
Running the vantage6 server and gui:
```shell script
docker-compose up -d
```
You will have to install, register and set up a node as well.
Installing the node is as follows:
```shell script
pip install vantage6
```

To set up a node you will have to follow the instructions from the [vantage6 documentation](https://docs.vantage6.ai/en/main/use/node.html#use-node).

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

# How to test things
## Using the `run_task.py` command
The `run_task.py` script runs a custom algorithm [available on github](https://github.com/CARRIER-project/vantage6-algorithms)
Make sure this task is published to the local registry by running `push_to_local_registry.sh` from that repo

```
python run_task.py
```
## Using the `test_federated_learning.ipynb` notebook
If you run docker-compose up docker will automatically spin up a jupyter notebook server for you. You can use the
`test_federated_learning.ipynb` notebook to run test tasks. You can grab the token from the docker-compose output.
