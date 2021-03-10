# ACTIVIDAD Nº 1

## TÍTULO DE LA ACTIVIDAD: Despliegue y acceso de la aplicación GuestBook

## TEXTO DE LA ACTIVIDAD

**Nota: Si realizaste la Actividad 5.3: Despliegue de la aplicación GuestBook, que era voluntaria salta directamente al apartado "Acceso a la aplicación".**

### Despliegue de la aplicación

En esta tarea vamos a desplegar una aplicación web que requiere de dos servicios para su ejecución. La aplicación se llama GuestBook y necesita los dos siguientes servicios:

* La aplicación guestbook es una aplicación web desarrollada en python que es servida por el puerto 5000/tcp. Utilizaremos la imagen `iesgn/guestbook`.
* Esta aplicación guarda la información en una base de datos no relacional redis, que utiliza el puerto 6379/tcp para conectarnos. Usaremos la imagen `redis`.

Por lo tanto para desplegar la aplicaciones tendremos dos ficheros.yaml:

* [guestbook-deployment.yaml](files/guestbook/guestbook-deployment.yaml)
* [redis-deployment.yaml](files/guestbook/redis-deployment.yaml)

Para realizar el despliegue realiza los siguientes pasos:

1. Usando los ficheros anteriores crea los dos despliegues.
2. Comprueba que los recursos que se han creado: Deployment, ReplicaSet y Pods.

### Acceso a la aplicación

Una vez que tenemos creado el despliegue, vamos a crear los servicios correspondientes:

#### Servicio para acceder a la aplicación

El primer servicio que vamos a crear es el servicio para acceder a la aplicación GuestBook desde el exterior, para ello crea un fichero yaml con la definición del servicio a partir de la siguiente plantilla:

```yaml
apiVersion: v1
kind: Service
metadata:
  name: guestbook
  labels:
    app: guestbook
    tier: frontend
spec:
  type: 
  ports:
  - port: 
    targetPort: 
  selector:
    app: guestbook
    tier: frontend
```

Tienes que poner el tipo de servicio, el puerto del servicio será el 80 y el nombre del puerto de la aplicación que hemos asignado en el despliegue es `http-server`.

Realiza los siguientes pasos:

1. Crea el fichero yaml con la definición del servicio, y crea el servicio.
2. Comprueba el puerto que te han asignado al servicio para acceder desde el exterior.
3. Accede a la ip del nodo master y al puerto asignado desde un navegador web para ver la aplicación.
4. Responde la siguiente pregunta: ¿Por qué aparece el mensaje de error: **Waiting for database connection...**?

#### Servicio para acceder a la base de datos

A continuación vamos a crear el servicio para acceder a la base de datos. Vamos a crear el fichero yaml para su definición a partir de la siguiente plantilla:

```yaml
apiVersion: v1
kind: Service
metadata:
  name: redis
  labels:
    app: redis
    tier: backend
spec:
  type: 
  ports:
  - port: 
    targetPort: 
  selector:
    app: redis
    tier: backend
```
Tienes que poner el tipo de servicio, el puerto del servicio será el 6379 y el nombre del puerto de la base de datos que hemos asignado en el despliegue es `redis-server`. **Nota: No cambies el nombre del servicio, ya que la aplicación guestbook va acceder por defecto a la base de datos usando el nombre `redis`**.

Realiza los siguientes pasos:

1. Crea el fichero yaml con la definición del servicio, y crea el servicio.
2. Lista los servicios que has creado.
3. Accede a la ip del nodo master y al puerto asignado desde un navegador web para ver la aplicación. Y comprueba que funciona sin ningún problema.

#### Acceso a la aplicación usando Ingress

Vamos a crear el fichero yaml de definición del recurso ingress para acceder a la aplicación a partir de la siguiente plantilla:

```yaml
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: guestbook
spec:
  rules:
  - host: 
    http:
      paths:
      - path: /
        pathType: Prefix
        backend:
          service:
            name: 
            port:
              number: 
```
Indica un host del tipo *www.tunombre.org*, indica el nombre del servicio que creaste para acceder a la aplicación guestbook y ten en cuenta que el puerto de dicho servicio era el 80.

Realiza los siguientes pasos:

1. Activa el addon ingress en minikube para instalar el ingress controller.
2. Crea La definición del recurso ingress con los datos sugeridos, y crea el recurso ingress.
3. Modifica el fichero `/etc/hosts` de tu ordenador para configurar la resolución estática.
3. Accede a la aplicación usando el nombre que has asignado.

Para superar la actividad deberás entregar en un fichero comprimido los siguientes pantallazos:

1. Pantallazo donde se vea el acceso desde un navegador web a la aplicación cuando sólo tenemos el servicio para acceder a la aplicación (Tiene que aparecer el mensaje de error).
2. Pantallazo donde se vea el acceso desde un navegador web a la aplicación usando la ip del nodo master y el puerto asignado al servicio.
5. Pantallazo donde se vea el acceso desde un navegador web a la aplicación usando el nombre que hemos configurado en el recurso ingress.

## RECURSOS

* Conexión a internet
* Los siguiente ficheros: 
  * [guestbook-deployment.yaml](files/guestbook/guestbook-deployment.yaml)
  * [redis-deployment.yaml](files/guestbook/redis-deployment.yaml)

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
