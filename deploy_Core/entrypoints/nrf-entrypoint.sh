#!/bin/bash
set -eumb

echo "Running nrf to check logs use tail -100f ~/home/henok/5G-NR-NTN/deploy_Core/logs/nrf.log"
exec nohup /usr/local/bin/nrf -c /openair-nrf/etc/nrf.conf -o >> /openair-nrf/etc/nrf.log 2>&1
