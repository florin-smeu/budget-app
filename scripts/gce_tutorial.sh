#!/bin/bash

#cd ..

# 1. gcloud init and configure project
#gcloud init

# 2. gcloud config list to see config and project id is ok
#gcloud config list

# 3. create machines use configured project id
#docker-machine vm01 -d google --google-tags kubecaf-swarm --google-project kubecaf1
#docker-machine vm02 -d google --google-tags kubecaf-swarm --google-project kubecaf1

# WARNING if an error occurs create credentials on gcp, download json and export
# GOOGLE_APPLICATION_CREDENTIALS var to the json path

# 4. configure firewall rules to add needed ports 
#gcloud compute firewall-rules create auth --allow tcp:8886 --source-ranges=0.0.0.0/0 --description="rule for auth"
#gcloud compute firewall-rules create visualizer --allow tcp:8080 --source-ranges=0.0.0.0/0 --description="rule for visualizer"
#gcloud compute firewall-rules create frontend --allow tcp:8889 --source-ranges=0.0.0.0/0 --description="rule for frontend"
#gcloud compute firewall-rules create backend --allow tcp:8888 --source-ranges=0.0.0.0/0 --description="rule for backend"

# 5. ssh into vm01 and create swarm
#docker-machine ssh  vm01
	# sudo docker-swarm init
	# copy token
	# logout

# 6. ssh into vm02 and add to swarm
#docker-machine ssh vm02
	# sudo <token>
	# logout

# 7. scp docker-compose to vm01
#docker-machine scp docker-compose.yml vm01:.

# 8. ssh into vm01 and deploy stack
#docker-machine ssh vm01
#docker stack deploy c docker-compose.yml kubecaf

# All done


