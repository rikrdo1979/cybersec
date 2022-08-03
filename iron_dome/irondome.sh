#!/bin/bash
while true; do

inotifywait -e modify,create,delete -r /path/to/your/dir && \
echo "change" >> logfile.log

done
