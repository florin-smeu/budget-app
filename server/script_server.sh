#!/bin/bash
docker build -t budget-app .
docker tag budget-app:latest florinsmeu/budget-app:0.34
docker push florinsmeu/budget-app:0.34
