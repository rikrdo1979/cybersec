#!/bin/bash

# Get console options 

while getopts "r:l:p:" FLAG
do
	case "${FLAG}" in
	r)
		LINK="${OPTARG}"
		echo "la URL es: $LINK"
		;;
	l)
		DEEPNESS="${OPTARG}"
		echo "El nivel de recursividad es: $DEEPNESS"
		;;
	p)
		if [ -z "${OPTARG}" ]; then
			SAVE_PATH="./data"
			echo "el path es ./data"
		else
			SAVE_PATH="${OPTARG}"
			echo "*** el path es: $SAVE_PATH"
			[ ! -d "$SAVE_PATH" ] && mkdir -p "$SAVE_PATH"
		fi
		;;
	*)	echo "opcion invalida"
		;;
	esac
done
	# Controla modificadores inexistentes
	shift $(($OPTIND - 1))
	set +x

IMGFILE="img.txt"
LINKFILE="href.txt"

# Search and list href hiperlinks

curl -sSL  $1 | tr "\t\r\n'" '   "' | \
    grep -i -o '<a[^>]\+href[ ]*=[ \t]*"\(ht\|f\)tps\?:[^"]\+"' | \
	    sed -e 's/^.*"\([^"]\+\)".*$/\1/g' > $LINKFILE

# Create imagenes directory if not exist and follow

[ ! -d "./imagenes" ] && mkdir ./imagenes
cd imagenes

# Find img sources recusively and create a list in a file

curl -sSL  $1 | grep ".jpg\|.jpeg\|.png\|.gif\|.bmp" \
	| awk -F '<img' '{print $2}' | awk -F 'src=' '{print $2}' \
		| cut -d '"' -f2 | cut -d "?" -f1 | awk 'NF''{print $1}' > $IMGFILE

# Copy img list file to parent dir

cp $IMGFILE  ../

# Iterate each line in the file and download the file

for line in $(cat $IMGFILE)
	do curl -O -J $line
	done

# Remove img list file

rm $IMGFILE

cd ..

