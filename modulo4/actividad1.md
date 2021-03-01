# ACTIVIDAD Nº 1

## TÍTULO DE LA ACTIVIDAD: Trabajando con ReplicaSet

## TEXTO DE LA ACTIVIDAD

Como indicamos en el contenido del módulo 4, no vamos a trabajar directamente con los Pods (realmente tampoco vamos a trabajar directamente con los ReplicaSet, en el siguiente módulo explicaremos los *Deployments* que serán el recurso con el que trabajaremos).  En ete ejercicio vamos a crear un ReplicaSet que va a controlar un conjunto de pod. Para ello realiza los siguientes pasos:

1. Crea un fichero yaml con la descripción del recurso ReplicaSet, teniendo en cuenta los siguientes aspectos:
    * Indica nombres distintos para el ReplicaSet y para el contenedor de los pods que va a controlar.
    * El ReplicaSet va a crear 3 réplicas.
    * La imagen que debes desplegar es `iesgn/test_web:latest`.
    * Indica de manera adecuada una etiqueta en la especificación del pod que vas a definir que coincida con el *selector* del ReplicaSet.
2. Crea el ReplicaSet.
3. Comprueba que que se ha creada el ReplicaSet y los 3 pods.
4. Obtén información detallada del ReplicaSet creado.
5. Vamos a probar la tolerancia a fallos: Elimna uno de los 3 pods, y comprueba que inmediatamente se ha vuelto a crear un nuevo pod.
6. Vamos a comprobar la escalabilidad: escala el ReplicaSet para tener 6 pods de la aplicación.
7. Elimina el replicaSet y comprueba que se han borrado todos los pods.

Para superar la actividad deberás entregar en un fichero comprimido los siguientes pantallazos:

1. Pantallazo del fichero yaml que has creado con la definición del ReplicaSet.
2. Pantallazo donde se comprueba que el ReplicaSet y los 3 pods se han creado.
3. Pantallazo donde se ve la información detallada del ReplicaSet.
4. Pantallazo donde se ve los pods que se han creado, después de eliminar uno de ellos.
5. Pantallazo donde se ve los pods que se han creado después del escalado.

## RECURSOS

* Conexión a internet

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

* Se entregan los documentos; contienen lo solicitado y los contenidos son originales.

## ¿ES NECESARIO TENER TERMINADA ALGUNA ACTIVIDAD O RECURSO ANTERIOR? Indique cuáles.

No

## TIEMPO ESTIMADO PARA REALIZAR LA ACTIVIDAD

1 hora
