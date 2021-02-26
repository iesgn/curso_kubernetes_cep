# Gestionando los pods

Tenemos un fichero [`pod.yaml`](files/pod.yaml) donde hemos definido un pod  de la siguiente manera:

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: pod-nginx
  namespace: default
  labels:
    app: nginx
    service: web
spec:
  containers:
    - image: nginx
      name: contenedor-nginx
```

Para crear el pod desde el fichero yaml:

    kubectl create -f pod.yaml

Y podemos ver que el pod se ha creado:

    kubectl get pods

Si queremos saber en qué nodo del cluster se está ejecutando:

    kubectl get pod -o wide

Para obtener información más detallada del pod:

    kubectl describe pod pod-nginx

Para eliminar el pod:

    kubectl delete pod pod-nginx

Para obtener los logs del pod:

    kubectl logs nginx

Si quiero conectarme al contenedor:

    kubectl exec -it pod-nginx -- /bin/bash

Podemos acceder a la aplicación, redirigiendo un puerto de localhost al puerto de la aplicación:

    kubectl port-forward pod-nginx 8080:80

Y accedemos al servidor web en la url http://localhost:8080.

**NOTA: Esta no es la forma con la que accedemos a las aplicaciones en kuberentes. Para el acceso a las aplicaciones usaremos un recurso llamado `service`. Con la anterior instrucción lo que estamos haciendo es una redirección desde locashost el puerto 8080 al puerto 80 del pod.**

Para obtener las labels de los pods que hemos creado:

    kubectl get pods --show-labels

Los Labels lo hemos definido en la sección metadata del fichero yaml, pero también podemos añadirlos a los pods ya creados:

    kubectl label pods pod-nginx service=web --overwrite=true

Los Labels me van a permitir seleccionar un recurso determinado, por ejemplo para visualizar los pods que tienen un label con un determinado valor:

    kubectl get pods -l service=web

También podemos visualizar los valores de los labels como una nueva columna:

    kubectl get pods -Lservice
