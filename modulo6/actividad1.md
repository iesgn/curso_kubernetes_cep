# ACTIVIDAD Nº 1

## TÍTULO DE LA ACTIVIDAD: Despliegue y acceso de la aplicación GuestBook

## TEXTO DE LA ACTIVIDAD

Una vez que tenemos creado el despliegue de la aplicación, que realizamos en la [Actividad 5.3: Despliegue de la aplicación GuestBook](../modulo5/actividad3.md), vamos a crear los Services correspondientes para acceder a ella:

### Service para acceder a la aplicación

El primer Service que vamos a crear nos va a permitir acceder a la aplicación GuestBook desde el exterior, para ello crea un fichero yaml con la definición del Service a partir de la siguiente plantilla:

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

Tienes que poner el tipo del Service, el puerto del servicio será el 80 y el nombre del puerto de la aplicación que hemos asignado en el Deployment es `http-server`.

Realiza los siguientes pasos:

1. Elabora el fichero yaml con la definición del Service, y créalo.
2. Comprueba el puerto que le han asignado al Service para acceder desde el exterior.
3. Accede a la ip del nodo master y al puerto asignado desde un navegador web para ver la aplicación.
4. Responde la siguiente pregunta: ¿Por qué aparece el mensaje de error: **Waiting for database connection...**?

### Service para acceder a la base de datos

A continuación vamos a crear el Service para acceder a la base de datos. Vamos a crear el fichero yaml para su definición a partir de la siguiente plantilla:

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
Tienes que poner el tipo del Service, el puerto del servicio será el 6379 y el nombre del puerto de la base de datos que hemos asignado en el Deployment es `redis-server`. **Nota: No cambies el nombre del Service, ya que la aplicación guestbook va a acceder por defecto a la base de datos usando el nombre `redis`**.

Realiza los siguientes pasos:

1. Elabora el fichero yaml con la definición del Service, y créalo.
2. Lista los Services que has creado.
3. Accede a la ip del nodo master y al puerto asignado desde un navegador web para ver la aplicación. Comprueba que funciona sin ningún problema.

### Acceso a la aplicación usando Ingress

Vamos a crear el fichero yaml de definición del recurso Ingress para acceder a la aplicación a partir de la siguiente plantilla:

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
              number: 80
```
Indica un host del tipo *www.tunombre.org*, indica el nombre del Service que creaste para acceder a la aplicación guestbook y ten en cuenta que el puerto de dicho servicio era el 80.

Realiza los siguientes pasos:

1. Activa el *addon* ingress en minikube para instalar el Ingress Controller.
2. Crea La definición del recurso Ingress con los datos sugeridos, y crea el recurso Ingress.
3. Modifica el fichero `/etc/hosts` de tu ordenador para configurar la resolución estática.
3. Accede a la aplicación usando el nombre que has asignado.

Para superar la actividad deberás entregar en un fichero comprimido los siguientes pantallazos:

1. Pantallazo donde se vea el acceso desde un navegador web a la aplicación cuando sólo tenemos el servicio para acceder a la aplicación (tiene que aparecer el mensaje de error) (**pantallazo1.jpg**).
2. Pantallazo donde se vea el acceso desde un navegador web a la aplicación usando la ip del nodo master y el puerto asignado al Service (**pantallazo2.jpg**).
3. Pantallazo donde se vea el acceso desde un navegador web a la aplicación usando el nombre que hemos configurado en el recurso Ingress (**pantallazo3.jpg**).

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

* Se entregan los documentos, contienen lo solicitado y los contenidos son originales.

## ¿ES NECESARIO TENER TERMINADA ALGUNA ACTIVIDAD O RECURSO ANTERIOR? Indique cuáles.

No

## TIEMPO ESTIMADO PARA REALIZAR LA ACTIVIDAD

1 hora
