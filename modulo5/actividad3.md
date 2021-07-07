# ACTIVIDAD Nº 3

## TÍTULO DE LA ACTIVIDAD: Despliegue de la aplicación GuestBook

## TEXTO DE LA ACTIVIDAD

En esta tarea vamos a desplegar una aplicación web que requiere de dos servicios para su ejecución. La aplicación se llama GuestBook y necesita los siguientes servicios:

* La aplicación Guestbook es una aplicación web desarrollada en python que es servida en el puerto 5000/tcp. Utilizaremos la imagen `iesgn/guestbook`.
* Esta aplicación guarda la información en una base de datos no relacional redis, que utiliza el puerto 6379/tcp para recibir las conexiones. Usaremos la imagen `redis`.

Por lo tanto si tenemos dos servicios distintos, tendremos dos ficheros yaml para crear dos recursos Deployment, uno para cada servicio. Con esta manera de trabajar podemos obtener las siguientes características:

1. Cada conjunto de Pods creado en cada despliegue ejecutarán un solo proceso para ofrecer el servicio.
2. Cada conjunto de Pods se puede escalar de manera independiente. Esto es importante, si identificamos que al acceder a alguno de los servicios se crea un cuello de botella, podemos escalarlo para tener más Pods ejecutando el servicio.
3. Las actualizaciones de los distintos servicios no interfieren en el resto.
4. Lo estudiaremos en un módulo posterior, pero podremos gestionar el almacenamiento de cada servicio de forma independiente.

Por lo tanto para desplegar la aplicaciones tendremos dos ficheros.yaml:

* [guestbook-deployment.yaml](../modulo6/files/guestbook/guestbook-deployment.yaml)
* [redis-deployment.yaml](../modulo6/files/guestbook/redis-deployment.yaml)

Para realizar el despliegue realiza los siguientes pasos:

1. Usando los ficheros anteriores crea los dos Deployments.
2. Comprueba que los recursos que se han creado: Deployment, ReplicaSet y Pods.
3. Crea una redirección utilizando el `port-forward` para acceder a la aplicación, sabiendo que la aplicación ofrece el servicio en el puerto 5000, y accede a la aplicación con un navegador web.

¿Qué aparece en la página principal de la aplicación?. Aparece el siguiente mensaje: **Waiting for database connection...**. Por lo tanto podemos indicar varias conclusiones:

1. Hasta ahora no estamos accediendo de forma "normal" a las aplicaciones. El uso de la opción `port-forward` es un mecanismo que realmente nos posibilita acceder a la aplicación, pero utilizando un proxy. Deberíamos acceder a las aplicaciones usando una ip y un puerto determinado.
2. Parece que tampoco hay acceso entre los Pods de los distintos despliegues. Parece que los Pods de la aplicación guestbook no pueden acceder al Pod donde se está ejecutando la base de datos redis.

En el siguiente módulo estudiaremos los recursos que nos ofrece la API de Kubernetes para permitirnos el acceso a las aplicaciones desde el exterior, y para que los distintos Pods de los despliegues puedan acceder entre ellos.

Para superar la actividad deberás entregar en un fichero comprimido los siguientes pantallazos:

1. Pantallazo donde se comprueba los recursos que se han creado (**pantallazo1.jpg**).
2. Pantallazo donde se vea el acceso desde un navegador web a la aplicación usando el `port-forward`, y se vea el mensaje de error al no poder acceder a la base de datos (**pantallazo2.jpg**).

## RECURSOS

* Conexión a Internet
* Los siguiente ficheros:
  * [guestbook-deployment.yaml](../modulo6/files/guestbook/guestbook-deployment.yaml)
  * [redis-deployment.yaml](../modulo6/files/guestbook/redis-deployment.yaml)


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
