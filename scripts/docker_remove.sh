#!/bin/bash
# remove containers
docker rm $(docker ps -a -f status=exited -q)
#remove images
docker rmi $(docker images -a | grep -v "kubecaf")
