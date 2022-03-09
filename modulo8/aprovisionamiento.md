# Aprovisionamiento de volúmenes

Para que el administrador de Kubernetes defina los volúmenes disponibles en nuestro cluster tenemos dos posibilidades:


## Aprovisionamiento estático

En este caso, es el administrador del cluster el responsable de ir definiendo los distintos volúmenes disponibles en el cluster creando manualmente los distintos recursos PersistentVolumen (PV).

Un PersistentVolumen es un objeto que representa los volúmenes disponibles en el cluster. En él se van a definir los detalles del [backend](https://kubernetes.io/docs/concepts/storage/persistent-volumes/#types-of-persistent-volumes) de almacenamiento que vamos a utilizar, el tamaño disponible, los [modos de acceso](https://kubernetes.io/docs/concepts/storage/persistent-volumes/#access-modes), las [políticas de reciclaje](https://kubernetes.io/docs/concepts/storage/persistent-volumes/#reclaim-policy), etc.

Tenemos tres modos de acceso, que dependen del backend que vamos a utilizar:

* ReadWriteOnce: read-write solo para un nodo (RWO)
* ReadOnlyMany: read-only para muchos nodos (ROX)
* ReadWriteMany: read-write para muchos nodos (RWX)

Las políticas de reciclaje de volúmenes también dependen del backend y son:

* Retain: El PV no se elimina, aunque el PVC se elimine. El administrador debe borrar el contenido para la próxima asociación.
* Recycle: Reutilizar contenido. Se elimina el contenido y el volumen es de nuevo utilizable.
* Delete: Se borra después de su utilización.

A modo de resumen, ponemos en la siguiente tabla los modos de acceso de algunos de los sistemas de almacenamiento más usados:

|Plugin |ReadWriteOnce |ReadOnlyMany| ReadWriteMany|
|:---:|:---:|:---:|:---:|
|AWS EBS| ✓ | - | - |
|AzureFile|	✓ |	✓ |	✓ |
|AzureDisk|	✓ | - |	- |
|CephFS | ✓ | ✓ | ✓ |
|Cinder |	✓ |	- |	-|
|GCEPersistentDisk |	✓ |	✓ |	- |
|Glusterfs | ✓ | ✓ | ✓|
|HostPath |	✓ |	- |	- |
|iSCSI |	✓ |	✓ |	- |
|NFS |	✓ |	✓ |	✓ |
|RBD | ✓ | ✓ | - |

Por último, vemos un ejemplo de un fichero yaml que nos permite la definición de un *PersitentVolumen*:

```yaml
apiVersion: v1
kind: PersistentVolume
metadata:
  name: pv1
spec:
  storageClassName: manual
  capacity:
    storage: 5Gi
  accessModes:
    - ReadWriteOnce
  persistentVolumeReclaimPolicy: Recycle
  hostPath:
    path: /data/pv1
```

* `storageClassName: manual`: Indica que este volumen se puede asignar de forma estática, sin utilizar ningún "aprovisonador" de almacenamiento.
* Se indica al tamaño del volumen, con `capacity`, `storage`.
* `accessModes`: El modo de acceso.
* `persistentVolumeReclaimPolicy`: La política de reciclaje.
* Y por útimo se indica el tipo (backend) de almacenamiento, en este caso es de tipo `hostPath` que creará un directorio (`/data/pv1`) en el nodo para guardar la información.

## Aprovisionamiento dinámico

Cuando el desarrollador necesita almacenamiento para su aplicación, hace una petición de almacenamiento creando un recurso PersistentVolumenClaim (PVC) y de forma dinámica se crea el recurso PersistentVolume que representa el volumen y se asocia con esa petición. De otra forma explicado, cada vez que se cree un PersistentVolumenClaim, se creará bajo demanda un PersistentVolumen que se ajuste a las características seleccionadas.

Para conseguir la [gestión dinámica de volúmenes](https://kubernetes.io/docs/concepts/storage/dynamic-provisioning/), necesitamos [un "aprovisionador" de almacenamiento](https://kubernetes.io/docs/concepts/storage/storage-classes/#provisioner) (tendremos distintos aprovisionadores para los distintos tipos de almacenamiento).

Para definir los "aprovisionadores" de almacenamiento, usaremos el objeto *StorageClass*. En Minikube, por defecto, ya tenemos un provisionador para almacenamiento del tipo *hostPath* (monta un directorio del host en el pod).

```bash
kubectl get storageclass
NAME                 PROVISIONER                RECLAIMPOLICY   VOLUMEBINDINGMODE   ALLOWVOLUMEEXPANSION   AGE
standard (default)   k8s.io/minikube-hostpath   Delete          Immediate           false                  46d
```

En este caso la configuración del objeto `storageclass` se definió con las siguientes características:

* La política de reciclaje tiene el valor `Delete`.
* Y el modo de asociación (`VOLUMEBINDINGMODE`) tiene el valor `Immediate`, es decir, cuando se cree el objeto PersistenVolumenClaim se asociará de forma dinámica un volumen (objeto PersistenVolumen) inmediatamente. Otro valor podría ser `WaitForFirstConsumer`, en ese caso la asociación se haría cuando se utilizará el volumen.

## Vídeo

[https://www.youtube.com/watch?v=7D9R0_f60-Q](https://www.youtube.com/watch?v=7D9R0_f60-Q)
