# Describiendo un pod

Aunque podemos crear un pod directamente con kubectl:

    kubectl run nginx --image=nginx

Lo que habitualmente vamos a hacer es trabajar con ficheros yaml donde describimos el recurso que queremos crear en el cluster, un ejemplo podría ser el contenido del fichero `pod.yam`:

```yaml
apiVersion: v1 # required
kind: Pod # required
metadata: # required
 name: nginx # required
 namespace: default
 labels:
   app: nginx
   service: web
spec: # required
 containers:
   - image: nginx:1.16
     name: nginx
     imagePullPolicy: Always
```

Veamos cada uno de los parámetros que hemos definido:

* apiVersion: v1: La versión de la API que vamos a usar.
* kind: Pod: La clase de recurso que estamos definiendo.
* metadata: Información que nos permite identificar unívocamente al recurso (nombre, espacio de nombres donde estamos trabajando y etiquetas que me permiten caracterizar un recurso.).
* spec: Definimos las características del recurso. En el caso de un pod indicamos los contenedores que van a formar el pod, en este caso sólo uno. E indicamos la imagen desde la que se va a crear el contenedor, su nombre y podemos definir la política de descarga de la imagen.


