# Vantage 6 local setup
Local setup can be run as follows:

```shell script
docker-compose up -d

# Run docker registry separately. Node tasks are run in a network separate from the node itself. By making the registry
# available from the host network it will be accessable by all docker containers
docker run -d  --name registry --network host registry:2 
```

The `run_task.py` script runs a custom algorithm [available on github](https://github.com/CARRIER-project/vantage6-algorithms)
Make sure this task is published to the local registry by running `push_to_local_registry.sh` from that repo

```
python run_task.py
```
