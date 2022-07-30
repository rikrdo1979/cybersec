NAME:

    stockholm - encripta y renombra los ficheros dentro de ~/infection/

SYNOPSIS:

    stockholm [ OPCION ] ...

DESCRITION

    STOCKHOLM es una aplicación desarrollada en Python, que al ejecutarla cifra [ AES 128 ] y renombra con la extension [ .ft ] todos los ficheros contenido en una carpeta [ ~/infection/ ] , solo se veran afectados los ficheros con las extensiones que se detallan en el fichero adjunto [ wannacry_ext_list.txt ]

    -help      Muestra la ayuda 
    -version   Muestra la version del programa
    -silent    No muestra ningun output
    -reverse   Descifra y renombra los ficheros afectados
    
LIBRERIAS UTILIZADAS

    os
    sys
    argparse
    time
    cryptography
    
AUTHOR:

    Written by rikrdo
