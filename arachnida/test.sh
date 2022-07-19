#!/bin/bash

SAVE_PATH="./data"

while getopts "r:l:p:" FLAG
do
	case "${FLAG}" in
	r)
		LINK="${OPTARG}"
		echo "la URL es: $LINK"
		;;
	l)
		DEEPNESS="${OPTARG}"
		if [ -z "${OPTARG}" ]; then
			DEEPNESS=5
			echo "El nivel de recursividad es: $DEEPNESS"
		else
			DEEPNESS="${OPTARG}"
			echo "El nivel de recursividad es: $DEEPNESS"
		fi
		;;
	p)
		if [ -z "${OPTARG}" ]; then
			SAVE_PATH="./data"
			echo "el path es ./data"
		else
			SAVE_PATH="${OPTARG}"
			echo "El path es: $SAVE_PATH"
		fi
		;;
	*)	echo "opcion invalida"
		;;
	esac
done
	# Controla modificadores inexistentes
	shift $(($OPTIND - 1))
	set +x

[ ! -d "$SAVE_PATH" ] && mkdir -p "$SAVE_PATH"

IMGFILE="img.txt"
LINKFILE="href"
EXT_TXT="txt"
SRC_PATH=$(pwd)
DEEP=1

# Search and list href hiperlinks

curl -sSL $LINK | tr "\t\r\n'" '   "' | \
    grep -i -o '<a[^>]\+href[ ]*=[ \t]*"\(ht\|f\)tps\?:[^"]\+"' | \
	    sed -e 's/^.*"\([^"]\+\)".*$/\1/g' | cut -d "?" -f1 | sort | uniq > $LINKFILE.$DEEP.$EXT_TXT

curl -sSL  $LINK | grep ".jpg\|.jpeg\|.png\|.gif\|.bmp" \
	| awk -F '<img' '{print $2}' | awk -F 'src=' '{print $2}' \
		| cut -d '"' -f2 | cut -d "?" -f1 | awk 'NF''{print $1}' \
			| grep "http" > $IMGFILE

N=2
while [ $N -le $DEEPNESS ]
	do
		for line in $(cat $LINKFILE.$DEEP.$EXT_TXT)
		do 
		curl -sSL $line | tr "\t\r\n'" '   "' | \
			grep -i -o '<a[^>]\+href[ ]*=[ \t]*"\(ht\|f\)tps\?:[^"]\+"' | \
			 sed -e 's/^.*"\([^"]\+\)".*$/\1/g' | cut -d "?" -f1 | sort | uniq >> $LINKFILE.$N.$EXT_TXT
		
		curl -sSL  $line | grep ".jpg\|.jpeg\|.png\|.gif\|.bmp" \
			| awk -F '<img' '{print $2}' | awk -F 'src=' '{print $2}' \
				| cut -d '"' -f2 | cut -d "?" -f1 | awk 'NF''{print $1}' \
					| grep "http" >> $IMGFILE
		done
		DEEP="$N"
       (( N++ ))
done

DEEP=1
N=2

cp $IMGFILE $SAVE_PATH

# Create img directory if not exist and follow

cd "$SAVE_PATH"

# Find img sources recusively and create a list in a file

# Copy img list file to parent dir

# Iterate each line in the file and download the file

for line in $(cat $IMGFILE)
	do curl -O -J $line
	done

# Remove img list file

rm $IMGFILE

cd $SRC_PATH