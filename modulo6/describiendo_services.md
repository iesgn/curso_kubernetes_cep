# Describiendo Services

## Services NodePort

Suponemos que tenemos desplegado nginx usando el fichero yaml: [`nginx-deployment.yaml`](../modulo5/files/nginx-deployment.yaml):

    kubectl apply -f nginx-deployment.yaml

Por lo tanto tenemos dos pods ofreciendo el servidor web nginx, a los que queremos acceder desde el exterior y que se balancee la carga entre ellos.

Aunque podríamos crear un recurso Service desde la línea de comandos:

    kubectl expose deployment/nginx --port=80 --type=NodePort

Normalmente lo que hacemos es describir las características del Service en un fichero yaml [`nginx-srv.yaml`](files/nginx-srv.yaml):

```yaml
apiVersion: v1
kind: Service
metadata:
  name: nginx
spec:
  type: NodePort
  ports:
  - name: service-http
    port: 80
    targetPort: http
  selector:
    app: nginx
```
Veamos la descripción:

* Vamos a crear un recurso Service (parámetro `kind`) y lo nombramos como `nginx` (parámetro `name`). Este nombre será importante para la resolución dns.
* En la especificación del recurso indicamos el tipo de servicio (parámetro `type`).
* A continuación, definimos el puerto por el que va a ofrecer el servicio y lo nombramos (dentro del apartado `port`: el parámetro `port` y el parámetro `name`). Además, debemos indicar el puerto en el que los pods están ofreciendo el servicio (parámetro `targetPort`), en este caso, hemos usado el nombre del puerto (`http`) que indicamos en el recurso Deployment:

```yaml
   ...
   ports:
    - name: http
      containerPort: 80
   ...
```
* Por ultimo, seleccionamos los pods a los que vamos acceder y vamos a balancear la carga seleccionando los pods por medio de sus etiquetas (parámetro `selector`).

**Nota: La definición de un servicio de tipo ClusterIP sería exactamente igual, pero cambiando el parámetro `type`.**

## Para seguir aprendiendo

Para más información acerca de los Services puedes leer: [la documentación de la API](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.20/#service-v1-core) y la [guía de usuario](https://kubernetes.io/docs/concepts/services-networking/service/).
