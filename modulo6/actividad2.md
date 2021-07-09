# ACTIVIDAD Nº 2

## TÍTULO DE LA ACTIVIDAD: Despliegue y acceso de la Aplicación Lets-Chat

## TEXTO DE LA ACTIVIDAD

[Let's Chat](https://github.com/sdelements/lets-chat) es una aplicación web escrita en Node.js que utilizando una base de datos MongoDB nos posibilita la creación de salas de chats.

Vamos a realiza el despliegue y acceso a esta aplicación teniendo en cuenta los siguientes aspectos:

* La imagen docker que vamos a usar para el despliegue de Let's Chat es `sdelements/lets-chat` y para desplegar mongoDB utilizaremos la imagen `mongo`.
* Al crear el despliegue de Let's Chat podemos poner varias replicas, pero el despliegue de la base de datos, sólo creará una replica.
* El puerto en el que responde la aplicación es el 8080. La base de datos utiliza el puerto 27017.
* Vamos acceder desde el exterior a la aplicación. Sin embargo, no es necesario acceder desde el exterior a la base de datos.
* El nombre del Service para acceder a la base de datos debe ser `mongo` ya que por defecto la aplicación va a conectar a la base de datos usando ese nombre.
* Queremos acceder a la aplicación usando un nombre del tipo *www.chat-tunombre.org*.

Realiza los siguientes pasos:

1. Utilizando como modelos los ficheros yaml de la actividad anterior, crea los ficheros necesarios para crear los recursos en tu cluster de Kubernetes para desplegar esta aplicación.

Para superar la actividad deberás entregar en un fichero comprimido que contenga:

1. Los ficheros yaml que has creado.
2. Un pantallazo donde se vea el acceso desde un navegador web a la aplicación usando la ip del nodo master y el puerto asignado al Service (**pantallazo1.jpg**).
3. Un pantallazo donde se vea el acceso desde un navegador web a la aplicación usando el nombre que hemos configurado en el recurso Ingress (**pantallazo2.jpg**).

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
