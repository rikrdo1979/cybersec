#!/bin/bash

# Comprueba 
# PATH="./data/"
# [ ! -d "./data" ] && mkdir $PATH
# cd data

IMGFILE="img.txt"
LINKFILE="href.txt"

# Get console options 

while getopts "r:l:p:" FLAG
do
	case "${FLAG}" in
	r)
		# Descarga de forma recursiva las imagenes de la URL pasada
		
		echo "pasaste -r"
		;;
	l)
		# Nivel de profundidad de la descarga. Default = 5
		
		echo "pasaste -l"
		;;
	p)
		# Indica la ruta donde se guardarán los archivos descargados. Default = ./data/
		
		echo "pasaste -p"
		;;
	*)	
	
		# Si faltan parametros mensaje de error
		
		echo "Error faltan parámetros"
		;;
	esac
done

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

