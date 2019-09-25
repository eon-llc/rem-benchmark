#!/bin/bash

SCRIPT_DIR="/root/rem-benchmark/scripts"
FILE_PATH="${SCRIPT_DIR}/benchmark-check.sh"
PROCESSOR_PATH="${SCRIPT_DIR}/log_to_db.py"

#---------------------------------
# SCHEDULE THIS SCRIPT AS CRON
#---------------------------------
if ! crontab -l | grep -q 'benchmark-check'
then
  (crontab -l ; echo "* * * * * ${FILE_PATH}") | crontab -
fi

#---------------------------------
# RESTART LOOP IF IT IS NOT RUNNING
#---------------------------------
pgrep benchmark-loop >/dev/null 2>&1 || $SCRIPT_DIR/benchmark-loop.sh &

#---------------------------------
# RUN LOG PROCESSOR
#---------------------------------
python $PROCESSOR_PATH