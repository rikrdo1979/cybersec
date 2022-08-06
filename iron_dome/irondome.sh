#!/bin/bash
while true; do

evento=$(inotifywait -e modify,create,delete -r /home/rikrdo/cybersec/iron_dome/logs/) &&

echo $evento >> logfile.log

done
