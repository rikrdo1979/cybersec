#!/bin/bash

while getopts "rlp" FLAG
do
	case "${FLAG}" in
	r)
		echo "pasaste -r"
		;;
	l)
		echo "pasaste -l"
		;;
	p)
		echo "pasaste -p"
		;;
	*)	echo "opcion invalida"
		;;
	esac
done


IMG='img.file'

echo $IMG

for i in $@
do
  echo -e "$i\n"
done
