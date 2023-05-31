#!/bin/bash
set -eumb

echo "Running amf to check logs use tail -100f ~/oai-docker-compose/logs/amf.log"
exec nohup /usr/local/bin/amf -c /openair-amf/etc/amf.conf -o >> /openair-amf/etc/amf.log 2>&1
