#!/bin/bash

SCRIPT_DIR="/root/rem-benchmark/scripts"
FILE_PATH="${SCRIPT_DIR}/benchmark-check.sh"

#---------------------------------
# SCHEDULE THIS SCRIPT AS CRON
#---------------------------------
if ! crontab -l | grep -q ''
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
python log_to_db.py