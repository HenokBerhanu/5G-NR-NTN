#!/bin/bash

docker build -t oai-spgwu-tiny:v1.5.0 -f /home/vagrant/5G-NR-NTN/deploy_Core/openair-spgwu-tiny/Dockerfile.ubuntu .

sudo docker build -f docker/Dockerfile.ubuntu --target oai-spgwu-tiny-builder --tag oai-spgwu:develop --no-cache .