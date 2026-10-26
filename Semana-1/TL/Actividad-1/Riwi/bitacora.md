BITACORA

Comandos utilizados:

"pwd" -> permite saber en qué directorio me encuentro ubicado.

"ls" -> permite visualizar los archivos y carpetas que hay en la ubicación actual.

"ls -a" -> permite visualizar todos los archivos y carpetas de la ubicación actual, incluyendo los ocultos.

"cd" -> permite cambiar de directorio o acceder a una carpeta.

"cd .." -> permite regresar al directorio anterior, es decir, al directorio padre.

"cd ~" -> permite ir al directorio raiz.

"clear" -> permite limpiar la pantalla de la terminal.

"mkdir" -> permite crear carpetas.

"rmdir" -> permite eliminar carpetas vacías.

"rm -r" -> permite eliminar carpetas y todo su contenido.

"touch" -> permite crear archivos.

"rm" -> permite eliminar archivos.

"cat" -> permite visualizar el contenido de un archivo de texto. También permite escribir texto en archivos utilizando los operadores > y >> y "EOF".

echo -> permite mostrar texto o el valor de una variable en la terminal. También permite escribir texto en archivos utilizando los operadores > y >>.

"head" -> permite visualizar las primeras líneas de un archivo.

"tail" -> permite visualizar las últimas líneas de un archivo.

"mv" -> permite mover archivos y carpetas de una ubicación a otra. También permite renombrarlos si se especifica un nuevo nombre en la misma ubicación.

"cp" -> permite copiar archivos de una ubicación a otra.

"cp -r" -> permite copiar carpetas y todo su contenido.

"find" -> permite buscar archivos y carpetas según su nombre, ubicación u otros criterios.

"grep" -> permite buscar palabras o patrones de texto dentro de archivos.




#Respuestas a puntos de control

1- Punto de control: explica la diferencia entre una ruta absoluta y una relativa utilizando dos carpetas que acabas de crear.

Ruta absoluta --> ~/Documentos/Riwi/proyectos/web ---> Inicia siempre de la raíz del sistema, no importar en qué directorio estemos ubicados. Por eso es absoluta: solo existe una forma de escribirse.

Ruta relativa --> ../proyectos/web ---> Depende del directorio o ubicación donde estemos parados, es decir, es la forma en que especificamos la ubicación de un archivo o directorio en relación con el directorio de trabajo actual, en lugar de idicar la ruta completa desde la raíz.


2- Punto de control: explica por qué .control_interno no aparece en el listado normal y cómo manejar nombres que contienen espacios.

No aparece en el listado normla, porque al tener un punto inicial en el nombre indica que es un archivo oculto y no puede verse simplemente con ls si no con ls -a. Además para manejar nombres que contienen espacios se puede usar _ o - entre cada palabra.


3- Punto de control: explica cuándo utilizarías > y cuándo >>.

Se utiliza > para crear contenido en el archivo si no existe, si el archivo ya existe con contenido	el contenido anterior se pierde, o sea, se sobrescribe.

se utiliza >> cuando se quieres adicionar información sin perder la existente, es decir, se conserva lo que ya hay y se añade el nuevo contenido al final.


4- Punto de control: demuestra que mover un archivo cambia su ubicación y conserva su contenido.

~/Documentos/Riwi/entrada$ cat cliente_ana.txt
Nombre: Ana Torres.
Empresa: Panadería Aurora.
Estado: activo.
Correo: ana@example.com
~/Documentos/Riwi/entrada$ mv cliente_ana.txt ../clientes/activos/
~/Documentos/Riwi/entrada$ cat cliente_ana.txt
cat: cliente_ana.txt: No such file or directory
~/Documentos/Riwi/entrada$ cd ../clientes/activos/
~/Documentos/Riwi/clientes/activos$ cat cliente_ana.txt
Nombre: Ana Torres.
Empresa: Panadería Aurora.
Estado: activo.
Correo: ana@example.com   


5- Punto de control: explica cómo el mismo comando permite mover y renombrar archivos.

El comando mv recibe dos argumentos: origen y destino. Si el destino es otra carpeta entonces mueve el archivo a esa carpeta. Sin embargo si el destino es un nombre en la misma carpeta entonces lo renombra.


6- Punto de control: explica la diferencia entre copiar un archivo y copiar una carpeta que contiene otras carpetas.

Copiar un archivo: cp toma un solo archivo y lo duplica en el destino indicado. No necesita otro comando extra.
Copiar una carpeta que contiene otras carpetas: cp no permite hacer eso solo. Necesita otro comando que lo acompaña -r para que ingrese a cada subcarpeta y copie todo lo que encuentre dentro, manteniendo la estructura. Sin -r, solo copia la carpeta vacía.

Pienso que la diferencia es que un archivo es una sola unidad, mientras que una carpeta con otras carpetas es un subconjunto de archivos que tiene capas adentro que cp no recorre por su cuenta.


7- Punto de control: explica la diferencia entre buscar por nombre de archivo y buscar dentro de su contenido.

Buscar por nombre de archivo básicamente le dices al sistema "encuéntrame el archivo que se llama así". No importa qué haya adentro. Mientras que buscar por contenido le dices al sistema "encuéntrame el archivo que tiene esta palabra escrita dentro". No importa cómo se llame.


8- Punto de control: explica por qué rmdir pudo eliminar una carpeta vacía, pero falló cuando contenía archivos.

rmdir solo puede borra la carpeta, no lo que hay dentro. Si la carpeta está vacía, no hay nada que proteger, así que la elimina. Si la carpeta tiene archivos, no la elimina porque borrar la carpeta sin borrar los archivos dejaría datos sueltos en el disco sin forma de accederlos por nombre.




Demostración de la terminal:

~/Documentos/Riwi$ find . -name "factura_001.txt" 
./administracion/facturas/factura_001.txt

~/Documentos/Riwi$ cat administracion/facturas/factura_001.txt
Número: 001.
Cliente: Ana Torres.
Valor: 150000.
Estado: pendiente.
Nuevo Estado: pago

~/Documentos/Riwi$ cp administracion/facturas/factura_001.txt respaldos/factura_001_copia.txt

~/Documentos/Riwi$ mv respaldos/factura_001_copia.txt respaldos/factura_001_respaldo.txt
~/Documentos/Riwi$ ls respaldos/
clientes  administracion  proyectos  factura_001_respaldo.txt  resumen_octubre_respaldo.txt   