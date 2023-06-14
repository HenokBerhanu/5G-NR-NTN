#!/bin/bash

docker build -t oai-spgwu-tiny:v1.5.0 -f /home/vagrant/5G-NR-NTN/deploy_Core/openair-spgwu-tiny/Dockerfile.ubuntu .

sudo docker build -f docker/Dockerfile.ubuntu --target oai-spgwu-tiny-builder --tag oai-spgwu:develop --no-cache .

git clone -b develop https://github.com/OPENAIRINTERFACE/openair-spgwu-tiny.git

docker build -f openair-spgwu-tiny/docker/Dockerfile.ubuntu --target oai-spgwu-tiny-builder --tag oai-spgwu:develop --no-cache openair-spgwu-tiny/

git submodule deinit --force .
git submodule update --init --recursive