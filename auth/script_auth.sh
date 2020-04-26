#!/bin/bash
docker build -t budget-auth .
docker tag budget-auth:latest florinsmeu/budget-auth:0.1
docker push florinsmeu/budget-auth:0.1
