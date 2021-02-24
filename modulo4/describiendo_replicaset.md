# Describiendo un ReplicaSet

En este caso también vamos a definir el recurso de ReplicaSet en un fichero, por ejemplo como este:

```yaml
apiVersion: apps/v1
kind: ReplicaSet
metadata:
  name: replicaset-nginx
  namespace: default
spec:
  replicas: 2
  selector:
    matchLabels:
      app: nginx
  template:
    metadata:
      labels:
        app: nginx
    spec:
      containers:
        - image: nginx
          name: contenedor-nginx
```

Algunos de los parámetros definidos ya lo hemos estudiado en la definición del pod. Los nuevos parámetros de este recurso son los siguientes:

* `replicas`: Indicamos el número de pods que siempre se van a estar ejecutando.
* `selector`: Seleccionamos los pods que va a controlar el ReplicaSet por medio de las etiquetas. Es decir este ReplicaSet controlo los pods cuya etiqueta `app` es igual a `nginx`.
* `template`: El recurso ReplicaSet contiene la definición de un pod. Fíjate que el pod que hemos definido en la sección `template` tiene indicado el label necesario para que sea seleccionado por el ReplicaSet (`app: nginx`).

## Para seguir aprendiendo

* Para más información acerca de los ReplicaSet puedes leer: la [documentación de la API](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.20/#replicaset-v1-apps) y la [guía de usuario](https://kubernetes.io/docs/concepts/workloads/controllers/replicaset/).