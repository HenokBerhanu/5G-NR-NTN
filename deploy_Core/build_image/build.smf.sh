#!/bin/bash

docker build -t oai-smf:v1.5.0 -f /home/vagrant/5G-NR-NTN/deploy_Core/oai-cn5g-smf/Dockerfile.smf.ubuntu .

git clone -b develop https://gitlab.eurecom.fr/oai/cn5g/oai-cn5g-smf.git

docker build -f oai-cn5g-smf/docker/Dockerfile.smf.ubuntu --target oai-smf-builder --tag oai-smf:develop --no-cache oai-cn5g-smf/

git submodule deinit --force .
git submodule update --init --recursive