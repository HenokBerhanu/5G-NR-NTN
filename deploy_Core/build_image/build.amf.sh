#!/bin/bash

docker build -t oai-amf:v1.5.0 -f /home/vagrant/5G-NR-NTN/deploy_Core/oai-cn5g-amf/Dockerfile.amf.ubuntu .

git clone -b develop https://gitlab.eurecom.fr/oai/cn5g/oai-cn5g-amf.git

docker build -f oai-cn5g-amf/docker/Dockerfile.amf.ubuntu --target oai-amf-builder --tag oai-amf:develop --no-cache oai-cn5g-amf/