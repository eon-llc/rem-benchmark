#!/bin/bash

API_URL="http://127.0.0.1:8888"
WALLET_NAME=""
WALLET_PASS=""

date
remcli -u "$API_URL" wallet unlock -n "$WALLET_NAME" --password "$WALLET_PASS"
remcli -u "$API_URL" push action rembenchmark cpu '[]' -p rembenchmark@active -f
remcli -u "$API_URL" wallet stop

# add a delimeter for easy processing
echo "--action--"