#!/bin/bash

docker build -t oai-nrf:v1.5.0 -f /home/vagrant/5G-NR-NTN/deploy_Core/oai-cn5g-nrf/Dockerfile.nrf.ubuntu .

git clone -b develop https://gitlab.eurecom.fr/oai/cn5g/oai-cn5g-nrf.git

docker build -f oai-cn5g-nrf/docker/Dockerfile.nrf.ubuntu --target oai-nrf-builder --tag oai-nrf:develop --no-cache oai-cn5g-nrf/

docker exec -it oai-nrf /bin/bash
sudo docker-compose -p demo -f docker-compose2.yaml up -d