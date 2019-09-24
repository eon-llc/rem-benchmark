#!/bin/bash

SCRIPT_DIR="/root/rem-benchmark/scripts"
ACTIONS_LOG="${SCRIPT_DIR}/actions.log"

while :; do
    $SCRIPT_DIR/benchmark-actions.sh >>$ACTIONS_LOG 2>&1
    sleep $(shuf -i 12-18 -n 1)
done