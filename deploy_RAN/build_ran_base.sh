#!/bin/bash

docker build --target ran-base --tag ran-base:latest --file docker/Dockerfile.base.ubuntu20 .

#https://gitlab.eurecom.fr/oai/openairinterface5g/-/blob/develop/docker/README.md