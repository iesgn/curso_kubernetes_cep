# Describiendo un pod

Aunque podemos crear un pod directamente con kubectl:

    kubectl run nginx --image=nginx

Lo que habitualmente vamos a hacer es trabajar con ficheros yaml donde describimos el recurso que queremos crear en el cluster, un ejemplo podría ser el contenido del fichero `pod.yam`:

```yaml
apiVersion: v1 # required
kind: Pod # required
metadata: # required
 name: nginx # required
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

* `apiVersion`: v1: La versión de la API que vamos a usar.
* `kind: Pod`: La clase de recurso que estamos definiendo.
* `metadata`: Información que nos permite identificar unívocamente al recurso:
    * `name`: Nombre del pod
    * `labels`: Las [Labels](https://kubernetes.io/docs/concepts/overview/working-with-objects/labels/) nos permiten etiquetar los recursos de kubernetes (por ejemplo un pod) con información del tipo clave/valor.
* `spec`: Definimos las características del recurso. En el caso de un pod indicamos los contenedores que van a formar el pod, en este caso sólo uno. 
    * `image`: La imagen desde la que se va a crear el contenedor
    * `name`: Nombre del contenedor.
    * `imagePullPolicy`: Las imágenes se guardan en un registro interno. Se pueden utilizar registros públicos (google, docker hub,...) y registros privados. La política por defecto es `IfNotPresent`, que se baja la imagen si no está en el registro interno. Si queremos forzar la descarga indicamos `imagePullPolicy:Always`.

## Para seguir aprendiendo

* Para más información acerca de los pod puedes leer: la [documentación de la API](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.20/#pod-v1-core) y la [guía de usuario](https://kubernetes.io/docs/concepts/workloads/pods/).
* Para más información acerca de la estructura de la definición de los objetos de Kubernetes: [Understanding Kubernetes Objects](https://kubernetes.io/docs/concepts/overview/working-with-objects/kubernetes-objects/).


