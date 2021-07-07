# ACTIVIDAD Nº 1

## TÍTULO DE LA ACTIVIDAD: Trabajando con Deployments

## TEXTO DE LA ACTIVIDAD

En esta actividad vamos a crear un Deployment de una aplicación web. Sigamos los siguientes pasos:

1. Crea un fichero yaml con la descripción del recurso Deployment, teniendo en cuenta los siguientes aspectos:
    * Indica nombres distintos para el Deployment y para el contenedor de los Pods que va a controlar.
    * El Deployment va a crear 2 réplicas.
    * La imagen que debes desplegar es `iesgn/test_web:latest`.
    * Indica de manera adecuada una etiqueta en la especificación del Pod que vas a definir que coincida con el *selector* del Deployment.
2. Crea el Deployment.
3. Comprueba los recursos que se han creado: Deployment, ReplicaSet y Pods.
4. Obtén información detallada del Deployment creado.
5. Crea un una redirección utilizando el `port-forward` para acceder a la aplicación, sabiendo que la aplicación ofrece el servicio en el puerto 80, y accede a la aplicación con un navegador web.
6. Accede  a los logs del despliegue para comprobar el acceso que has hecho en el punto anterior.
7. Elimina el Deployment y comprueba que se han borrado todos los recursos creados.

Para superar la actividad deberás entregar en un fichero comprimido los siguientes pantallazos:

1. Pantallazo del fichero yaml que has creado con la definición del Deployment (**pantallazo1.jpg**).
2. Pantallazo donde se comprueba los recursos que se han creado (**pantallazo2.jpg**).
3. Pantallazo donde se ve la información detallada del Deployment (**pantallazo3.jpg**).
4. Pantallazo donde se vea el acceso desde un navegador web a la aplicación usando el `port-forward` (**pantallazo4.jpg**).
5. Pantallazo donde se vea los logs del despliegue después del acceso (**pantallazo5.jpg**).

## RECURSOS

* Conexión a internet

## ¿ES OBLIGATORIO HACER ESTA ACTIVIDAD PARA SUPERAR EL CURSO? (S/N)

Sí

## ¿ES UNA ACTIVIDAD INDIVIDUAL O DE GRUPO?

Individual

## ¿ES UNA ACTIVIDAD CALIFICABLE?

Sí

### ¿Tiene que ser calificada por el tutor/a? (S/N)

Sí

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
