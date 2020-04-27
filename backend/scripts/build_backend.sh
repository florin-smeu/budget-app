#!/bin/bash
cd ..
docker build -t kubecaf-backend .
docker tag kubecaf-backend:latest florinsmeu/kubecaf-backend:0.1
docker push florinsmeu/kubecaf-backend:0.1
