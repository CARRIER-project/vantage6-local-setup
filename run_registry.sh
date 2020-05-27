# The easiest way for the node to find the local registry is by attaching it to the host network.

docker run -d  --name registry --network host registry:2