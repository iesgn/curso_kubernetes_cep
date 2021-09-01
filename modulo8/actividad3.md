# ACTIVIDAD Nº 3

## TÍTULO DE LA ACTIVIDAD: Haciendo persistente la aplicación Nextcloud 

## TEXTO DE LA ACTIVIDAD

Esta actividad es la continuación de la actividad voluntaria [Actividad 7.2: Despliegue y acceso de la aplicación Nextcloud](../modulo7/actividad2.md).

Siguiendo la guía que hemos desarrollado en [Ejemplo 3: Wordpress con almacenamiento persistente](wordpress.md) vamos a configurar el despliegue de Nextcloud para que use volúmenes (vamos a usar dos volúmenes, uno para la aplicación y otro para la base de datos) para que la información no se pierda.

Realiza los siguientes pasos:

1. Crea los ficheros yaml para definir los recursos PersistentVolumenClaim para solicitar dos volúmenes de 4Gb.
2. Crea esos recursos y comprueba que se ha asociado un volumen de forma dinámica a cada solicitud.
3. Modifica los ficheros de despliegue de la aplicación y la base de datos para asociar los volúmenes a cada uno. Según la documentación de la imagen [Nextcloud](https://hub.docker.com/_/nextcloud) en Docker Hub, la forma más sencilla de hacer persistente la aplicación es montar el volumen en el directorio`/var/www/html/`.
5. Accede a la aplicación, configúrala y sube un fichero.
6. Comprobemos la persistencia: elimina los despliegues, vuelve a crearlos y vuelve a acceder desde el navegador y comprueba que la aplicación está configurada y mantiene el fichero que habías subido.

Para superar la actividad deberás entregar en un fichero comprimido los siguientes pantallazos:

1. Pantallazo donde se vean los ficheros yaml modificados para los despliegues (**pantallazo1.jpg**).
2. Pantallazo donde se vea el acceso a la aplicación con el fichero que has subido (**pantallazo2.jpg**).
3. Pantallazo donde se vea que se han eliminado y se han vuelto a crear los despliegues y que la aplicación sigue sirviendo el fichero que habíamos subido (**pantallazo3.jpg**).

## RECURSOS

* Conexión a internet

## ¿ES OBLIGATORIO HACER ESTA ACTIVIDAD PARA SUPERAR EL CURSO? (S/N)

No

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
