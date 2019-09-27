#!/bin/bash

SCRIPT_DIR="/root/rem-benchmark/scripts"
FILE_PATH="${SCRIPT_DIR}/benchmark-check.sh"
PROCESSOR_PATH="${SCRIPT_DIR}/log_to_db.py"
LOOP_PATH="${SCRIPT_DIR}/benchmark-loop.sh"
LOG_PATH="${SCRIPT_DIR}/log.txt"

#---------------------------------
# SCHEDULE THIS SCRIPT AS CRON
#---------------------------------
if ! crontab -l | grep -q 'benchmark-check'
then
  (crontab -l ; echo "* * * * * ${FILE_PATH}" >> $LOG_PATH 2>&1) | crontab -
fi

#---------------------------------
# RESTART LOOP IF IT IS NOT RUNNING
#---------------------------------
pgrep benchmark-loop >/dev/null 2>&1 || $LOOP_PATH &

#---------------------------------
# RUN LOG PROCESSOR
#---------------------------------
python $PROCESSOR_PATH