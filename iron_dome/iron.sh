#!/bin/bash
while true; do

evento=$(inotify-hookable -w /home/rikrdo/cybersec/iron_dome/logs/) &&

echo $evento >> logfile.log

done
