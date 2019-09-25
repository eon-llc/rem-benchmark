#!/bin/bash

# timestamp in ISO-8601
date -u +"%Y-%m-%dT%H:%M:%SZ"

# perform benchmark
remcli wallet unlock < /root/walletpass
remcli push action rembenchmark cpu '[]' -p rembenchmark@active -f
remcli wallet stop

# add a delimeter for easy processing
echo "--action--"