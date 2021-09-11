# ACTIVIDAD Nº 1

## TÍTULO DE LA ACTIVIDAD: Creando un cluster de MySQL

## TEXTO DE LA ACTIVIDAD

Siguiendo el [Ejemplo2: Despliegue de un cluster de MySQL](ejemplo2.md) de esta unidad, crea un cluster de MySQL con un primario y un secundario y realiza algunas pruebas para comrpobar su funcionamiento.

Realiza los siguientes pasos:

1. Crea los ficheros yaml necesarios para definir el ConfigMap, los servicios y el StatefulSet, de manera que los volúmenes asociados tengan 2GiB de tamaño y el servicio MySQL que ejecuten los secundarios se denomine `mysql-lectura`.
1. Crea un pod efímero que pueble la base de datos con la información que quieras.
1. Crea un pod efímero que consulte la base de datos del secundario.

Para superar la actividad deberás entregar en un fichero comprimido los siguientes pantallazos:

1. Pantallazo con la definición de los recursos (**pantallazo1.jpg**).
2. Pantallazo donde se visualice que se han creado los pods, los servicios y los volúmenes (**pantallazo2.jpg**).
3. Pantallazo donde se visualice la consulta a la base de datos (**pantallazo3.jpg**).


## RECURSOS

* Conexión a internet
* Los ficheros del [Ejemplo 2: Despliegue de un cluster de MySQL](ejemplo2.md).

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

2 horas
