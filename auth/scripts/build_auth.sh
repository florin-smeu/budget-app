#!/bin/bash
cd ..
docker build -t kubecaf-auth .
docker tag kubecaf-auth:latest florinsmeu/kubecaf-auth:0.1
docker push florinsmeu/kubecaf-auth:0.1
