# ACTIVIDAD Nº 2

## TÍTULO DE LA ACTIVIDAD: Despliegue y acceso de la aplicación Nextcloud 

## TEXTO DE LA ACTIVIDAD

Basándonos en el [Ejemplo completo: Despliegue y acceso a Wordpress + MariaDB](wordpress.md) vamos a realizar el despliegue de la aplicación NextCloud + MariaDB. Para ello ten en cuenta lo siguiente:

* El despliegue de la base de datos se haría de la misma forma que encontramos en el ejemplo de Wordpress, pero para esta actividad vamos a usar la imagen `mariadb:10.5`.
* Según la documentación de [NextCloud en DockerHub](https://hub.docker.com/_/nextcloud) las variables de entorno que tienes que modificar serían: `MYSQL_DATABASE`, `MYSQL_USER`, `MYSQL_PASSWORD` y `MYSQL_HOST`.
* Al igual que en el ejemplo utiliza un recurso ConfigMap para guardar los valores de configuración no sensibles, y un recurso Secret para los datos sensibles.
* Utiliza los ficheros yaml del ejemplo haciendo las modificaciones oportunas.

Para superar la actividad deberás entregar en un fichero comprimido los siguientes pantallazos:

1. Pantallazo donde se vea el contenido del fichero de despliegue de NextCloud (**pantallazo1.jpg**).
2. Pantallazo donde se vean los recursos que se han creado (**pantallazo2.jpg**).
3. Pantallazo donde se compruebe que la aplicación está funcionando (**pantallazo3.jpg**).

## RECURSOS

* Conexión a internet
* Los ficheros del [Ejemplo completo: Despliegue y acceso a Wordpress + MariaDB](wordpress.md).

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
