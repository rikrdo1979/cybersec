![image text](https://github.com/rikrdo1979/cybersec/blob/main/arachnida/spider.jpg)

## Proyecto Arachnida

Los metadatos son información que se utiliza para describir otros datos. Son esencialmente datos sobre datos.
Frecuentemente se utililizan en imágenes y documentos, pudiendo llegar a revelar información sensible de quienes lo han creado o manipulado. En este proyecto, se crean dos instrumentos que te permitirán extraer información automáticamente de la web y después analizarla para conocer o eliminar datos sensibles.

## Spider

El programa spider permite extraer todas las imágenes de un sitio web, de manera recursiva, proporcionando una url como parámetro.

./spider \[-rlp\] URL
• -r : descarga de forma recursiva las imágenes en una URL recibida como
parámetro.
• -r -l \[N\] : indica el nivel profundidad máximo de la descarga recursiva.
por defecto será 5.
• -p \[PATH\] : indica la ruta donde se guardarán los archivos descargados.

Ruta por defecto ./data/

## Scorpion

Scorpion recibe archivos como parámetros y es capaz de analizarlos en busca datos EXIF y otros metadatos, mostrándolos en pantalla.
El programa será compatible, al menos, con las mismas extensiones que gestiona spider.
