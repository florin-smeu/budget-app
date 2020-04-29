#!/bin/bash
cd ..
docker build -t kubecaf-frontend .
docker tag kubecaf-frontend:latest florinsmeu/kubecaf-frontend:0.1
docker push florinsmeu/kubecaf-frontend:0.1
