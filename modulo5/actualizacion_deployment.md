# Actualización y rollout de Deployment

Una vez que hemos creado un Deployment a partir de una imagen de una versión determinada, tenemos los pods ejecutando la versión indicada de la aplicación. 

¿Cómo podemos actualizar a una nueva versión de la aplicación? Se seguiran los siguientes pasos:

1. Tendremos que modificar el valor del parámetro `image` para indicar una nueva imagen indicando la nueva versión. 
2. En ese momento el Deployment se actualiza, es decir, se crea un nuevo ReplicaSet que creará nuevos pods de la nueva versión de la aplicación.
3. Según la estrategía de depliegue indicada se irán borrando los antiguos pods y se crearán lo nuevos.
4. El Deployment guardará el ReplicaSet antiguo, por si en algún momento queremos volver a la versión anterior.

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
Si nos fijamos vamos a desplegar la versión 1.31 de la aplicación mediawiki, creamos el despliegue:

    kubectl apply -f mediawiki-deployment.yaml --record

Con la opción `--record` vamos a registrar los comando que vamos a ejecutar a continuación para ir actualizando el despliegue. De esta forma al visualizar el historial de modificaciones veremos las instrucciones que han provado cada actualización.

Podemos comprobar los recursos que hemos creado:

    kubectl get all

Y si accedemos al pod con un `port-forwad` comprobamos que la versión actual de la mediawiki es la 1.31:

    kubectl port-forward deployment mediawiki 8080:80

imagen

## Actualizar un Deployment

A continuación queremos desplegar una versión más reciente de la mediawki. Para ello tenemos que modificar el campo `image` de nuestro Deployment, esta operación la podemos hacer de varias formas:

1. Modificando el fichero yaml y volviendo a ejecutar un `kubectl apply`.
2. Ejecutando la siguiente instrucción:

        kubectl set image deployment mediawiki contenedor-mediawiki=mediawiki:1.34 --all --record

¿Hace falta poner --all?

Al ejecutar la actualización del Deployment podemos observar que se ha creado un nuevo ReplicaSet, que creará los nuevos pods a partir de la versión modificada de la imagen. ¿Cómo se crean los nuevos pods y se drestruyen los antiguos? Dependerá de la estratégia de depliegue:

  * Por defector la estrategía de despliegue es `Recreate` que elimina los Pods antiguos y crea los nuevos.
  * Si indicamos en el despliegue el tipo de estrtégia como: `RollingUpdate`, se van creando los nuevos pods, comprueba que funcionan y se eliminan los antiguos.

Veamos los recursos que se han creado en la actualización:

  kubectl get all

Además podemos ver el historial de actualizaciones que hemos hecho sobre el despliegue:

  kubectl rollout history deployment mediawiki

Y volvemos a acceder a la aplicación con un `port-forward` para comprobar que realmente se ha desplegado la versión 1.34.

imagen

## Rollout del Deployment

Ahora vamos a desplegar una versión que da un error (la versión 2 de la aplicación no existe). ¿Podremos volver al despliegue anterior?

    kubectl set image deployment mediawiki contenedor-mediawiki=mediawiki:2 --all  --record

Dependiendo de la estrategia de despliegue, esto puede provocar que la aplicación se quede en la versión anterior (`RollingUpdate`) o que no haya ningún pod válido desplegado (`Recreate`). En cualquier caso, se puede volver a la versión anterior del despliegue mediante rollout:

    kubectl rollout undo deployment mediawiki
  kubectl get all

Y terminamos comprobando el historial de actualizaciones:

    kubectl rollout history deployment mediawiki