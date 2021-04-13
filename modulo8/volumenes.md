# Volúmenes en Kubernetes

## Tipos de volúmenes 

Los [volúmenes](https://kubernetes.io/docs/concepts/storage/volumes/) nos permiten proporcional almacenamiento a los pods, y podemos usar distintos tipos que nos ofrecen distintas características:

* Proporcionados por el proveedor de cloud: AWS, Azure, GCE, OpenStack, etc
* Propios de kubernetes:
    * configMap: Para usar un configMap como un directorio desde el pod.
    * emptyDir: Volumen efímero con la misma vida que el pod. Usado como almacenamiento secundario o para compartir entre contenedores del mismo pod.
    * hostPath: Monta un directorio del host en el pod (usado excepcionalmente, pero el que nosotros vamos a usar con minikube).
    * ...
* Habituales en despliegues "on premises": glusterfs, cephfs, iscsi, nfs, etc.

## Trabajando con volúmenes

Al trabajar con volúmenes em kubernetes se realizan dos funciones claramente diferenciadas:

* **Desde el punto de vista del administrador del cluster de Kubernetes:**

    El administrador es el responsable de la gestión del almacenamiento en el clúster de k8s para proporcionar almacenamiento a las aplicaciones, entrando a detalle en configurar los diferentes mecanismo, bien proporcionados por el proveedor de cloud o configurados directamente. Para ello gestiona los recursos del cluster llamados *PersistentVolume* o *StorageClasses*. Ejemplos:
        
    * Configurar Azure Disk para que pueda usarlo k8s.
    * Configurar Cephfs o RBD en la red local para usarlo en k8s.

* **Desde el punto de vista del desarrollador de aplicaciones que van a ser ejecutadas en el cluster de Kubernetes:**

    A los desarrolladores de aplicaciones les interesa más la disponibilidad y características del almacenamiento, que los detalles sobre el mecanismo de almacenamiento. Para solicitar almacenamiento se va a utilizar el recurso del cluster *PersistentVolumeClaim*. Ejemplos:
    
    * Quiero 20 GiB de almacenamiento permanente que pueda compartir entre varios pods de varios nodos en modo lectura.
    * Quiero 10 GiB de almacenamiento provisional para usar desde un pod en modo lectura y escritura.

