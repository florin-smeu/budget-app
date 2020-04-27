#!/bin/bash
cd ..
docker stack rm kubecaf
docker swarm leave --force
docker swarm init
docker stack deploy -c docker-compose.yml kubecaf
