#!/bin/bash

LINK="casadellibro.com"
LINKFILE="href"
EXT_TXT="txt"
SRC_PATH=$(pwd)
DEEP=0

# Search and list href hiperlinks

curl -sSL $LINK | tr "\t\r\n'" '   "' | \
    grep -i -o '<a[^>]\+href[ ]*=[ \t]*"\(ht\|f\)tps\?:[^"]\+"' | \
	    sed -e 's/^.*"\([^"]\+\)".*$/\1/g' | cut -d "?" -f1 | sort | uniq > $LINKFILE.$DEEP.$EXT_TXT
N=1
while [ $N -le 2 ]
	do
		for line in $(cat $LINKFILE.$DEEP.$EXT_TXT)
		do curl -sSL $line | tr "\t\r\n'" '   "' | \
		 grep -i -o '<a[^>]\+href[ ]*=[ \t]*"\(ht\|f\)tps\?:[^"]\+"' | \
			 sed -e 's/^.*"\([^"]\+\)".*$/\1/g' | cut -d "?" -f1 | sort | uniq >> $LINKFILE.$N.$EXT_TXT
		done	
		DEEP="$N"
       (( N++ ))
done
