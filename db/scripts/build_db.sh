#!/bin/bash
cd ..
docker build -t kubecaf-db .
docker tag kubecaf-db:latest florinsmeu/kubecaf-db:0.1
docker push florinsmeu/kubecaf-db:0.1
