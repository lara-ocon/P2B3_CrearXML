# Practica2_Bloque3
Transformar a formato XML la tipología de datos de los csvs de pizzas - Adquisición de datos - IMAT
Hecho por Lara Ocón Madrid

En esta práctica, hemos creado un archivo XML que guarda información acerca del número del tamaño, el numero de nans
y la tipología de las columnas, de los distintos csv que hemos utilizado en las prácticas del bloque 2 de "Maven Pizzas".

Hay dos maneras de ejecutar el programa, una es usando docker y la otra es corriendolo de forma normal. a continuación se explican ambos casos:

1) Para correr con docker se suministran dos ficheros de script: createdocker.sh crea un docker para ejecutar el programa y rundocker arranca el docker. Una vez se ha hecho esto basta con ejecutar 

"python3 ./informe_datos.py"

El programa carga los  dataframes los csv dentro de la carpeta ficheros, extraerá su información y la insertará en un árbol XML. Finalmente, exportará dicho arbol al archivo "reporte_tipologia_datos.xml".

El script de creación del docker instala las librerías necesarias.

Para salir de docker basta con teclear "exit"

2) Para ejecutarlo de forma normal basta con ejecutar:

"python3 ./informe_datos.py"

y se obtiene el mismo resultado, pero en la máquina local (no en el docker)

En este caso, para ejecutarlo, es necesario tener instaladas las librerías especificadas en requirements.txt.
