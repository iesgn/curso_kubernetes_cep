# Actualización y rollout de Deployment

Una vez que hemos creado un Deployment a partir de una imagen de una versión determinada, tenemos los pods ejecutando la versión indicada de la aplicación. 

¿Cómo podemos actualizar a una nueva versión de la aplicación? Se seguiran los siguientes pasos:

1. Tendremos que modificar el valor del parámetro `image` para indicar una nueva imagen indicando la nueva versión. 
2. En ese momento el Deployment se actualiza, es decir, se crea un nuevo ReplicaSet que creará nuevos pods de la nueva versión de la aplicación.
3. Según la estrategía de depliegue indicada se irán borrando los antiguos pods y se crearán lo nuevos.
4. El deployment guardará el ReplicaSet antiguo, por si en algún momento queremos volver a la versión anterior.

Veamos este proceso con más detalles estudiando un ejemplo de despliegue:

## Desplegando la aplicación mediawiki

Vamos a partir del fichero  [`mediawiki-deployment.yaml`](files/mediawiki-deployment.yaml) para desplegar la aplicación:

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: mediawiki
  labels:
    app: mediawiki
spec:
  replicas: 1
  selector:
    matchLabels:
      app: mediawiki
  template:
    metadata:
      labels:
        app: mediawiki
    spec:
      containers:
      - name: contenedor-mediawiki
        image: mediawiki:1.31
        ports:
        - containerPort: 80
```
