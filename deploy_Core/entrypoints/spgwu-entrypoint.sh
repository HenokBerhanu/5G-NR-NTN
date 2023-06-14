#!/bin/bash
set -eumb

echo "Running spgwu to check logs use tail -100f ~/home/henok/oai_xn_handover/5G-NR-NTN/deploy_Core/logs/spgw_u.log"
exec nohup /usr/local/bin/spgwu -c /openair-spgwu-tiny/etc/spgw_u.conf -o >> /openair-spgwu-tiny/etc/spgw_u.log 2>&1
