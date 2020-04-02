#!/bin/bash
docker build -t budget-db .
docker tag budget-db:latest florinsmeu/budget-db:0.1
docker push florinsmeu/budget-db:0.1
