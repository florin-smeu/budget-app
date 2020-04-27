#!/bin/bash
cd ..
docker stack rm kubecaf
docker swarm leave --force
