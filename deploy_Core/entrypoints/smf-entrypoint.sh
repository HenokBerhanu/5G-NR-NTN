#!/bin/bash
set -eumb

echo "Running smf to check logs use tail -100f ~/oai-docker-compose/logs/smf.log"
exec nohup /usr/local/bin/smf -c /openair-smf/etc/smf.conf -o >> /openair-smf/etc/smf.log 2>&1
