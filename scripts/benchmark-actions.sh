#!/bin/bash

date
remcli wallet unlock < /root/walletpass
remcli push action rembenchmark cpu '[]' -p rembenchmark@active -f
remcli wallet stop

# add a delimeter for easy processing
echo "--action--"