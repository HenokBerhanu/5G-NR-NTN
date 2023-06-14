#!/bin/bash

docker build --target ran-build --tag ran-build:latest --file docker/Dockerfile.build.ubuntu20 .