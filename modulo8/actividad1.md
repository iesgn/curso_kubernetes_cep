# ACTIVIDAD Nº 1

## TÍTULO DE LA ACTIVIDAD:  Desplegando un servidor web persistente

## TEXTO DE LA ACTIVIDAD

Siguiendo la guía explicada en el [Ejemplo 2: Gestión dinámica de volúmenes](ejemplo2.md), vamos a crear un servidor web que permita la ejecución de scripts PHP con almacenamiento persistente.

Para realizar esta actividad vamos a usar asignación dinámica de volúmenes y puedes usar, como modelos, los ficheros del ejemplo 2.

Realiza los siguientes pasos:

1. Crea un fichero yaml para definir un recurso PersistentVolumenClaim que se llame `pvc-webserver` y para solicitar un volumen de 2Gb.
2. Crea el recurso y comprueba que se ha asociado un volumen de forma dinámica a la solicitud.
3. Crea un fichero yaml para desplegar un servidor web desde la imagen `php:7.4-apache`, asocia el volumen al Pod que se va a crear e indica el punto de montaje en el *DocumentRoot* del servidor: `/var/www/html`.
4. Despliega el servidor y crea un fichero `info.php` en `/var/www/html`, con el siguiente contenido: `<?php phpinfo(); ?>`.
5. Define y crea un Service NodePort, accede desde un navegador al fichero `info.php` y comprueba que se visualiza de forma correcta.
6. Comprobemos la persistencia: elimina el Deployment, vuelve a crearlo y vuelve a acceder desde el navegador al fichero `info.php`. ¿Se sigue visualizando?

Para superar la actividad deberás entregar en un fichero comprimido los siguientes pantallazos:

1. Pantallazo con la definición del recurso PersistentVolumenClaim (**pantallazo1.jpg**).
2. Pantallazo donde se visualice los recursos `pv` y `pvc` que se han creado (**pantallazo2.jpg**).
3. Pantallazo donde se vea el fichero yaml para el despliegue (**pantallazo3.jpg**).
4. Pantallazo donde se vea el acceso a `info.php` (**pantallazo4.jpg**).
5. Pantallazo donde se vea que se ha eliminado y se ha vuelto a crear el despliegue y se sigue sirviendo el fichero `info.php` (**pantallazo5.jpg**).


## RECURSOS

* Conexión a internet
* Los ficheros del [Ejemplo 2: Gestión dinámica de volúmenes](ejemplo2.md).

## ¿ES OBLIGATORIO HACER ESTA ACTIVIDAD PARA SUPERAR EL CURSO? (S/N)

Si

## ¿ES UNA ACTIVIDAD INDIVIDUAL O DE GRUPO?

Individual

## ¿ES UNA ACTIVIDAD CALIFICABLE?

Si

### ¿Tiene que ser calificada por el tutor/a? (S/N) 

Si

### ¿Es de calificación automática?

No

### ¿Es calificada por el resto de compañeros/as del curso? (S/N)

No

## EVALUACIÓN

* Se entregan los documentos, contienen lo solicitado y los contenidos son originales.

## ¿ES NECESARIO TENER TERMINADA ALGUNA ACTIVIDAD O RECURSO ANTERIOR? Indique cuáles.

No

## TIEMPO ESTIMADO PARA REALIZAR LA ACTIVIDAD

1 hora
