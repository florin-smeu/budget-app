#!/bin/bash
docker stack rm budgetapp
docker swarm leave --force
docker swarm init
docker stack deploy -c docker-compose.yml budgetapp

