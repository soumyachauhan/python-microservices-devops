#!/bin/bash
apt-get update -y
apt-get install -y docker.io docker-compose
cd /home/ubuntu
git clone https://github.com/soumyachauhan/python-microservices-devops.git
cd python-microservices-devops
docker-compose up -d