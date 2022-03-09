# Solicitud de volúmenes

Independientemente de cómo haya aprovisionado el almacenamiento el administrador del cluster (de forma dinámica o de forma estática), el desarrollador debe hacer una **solicitud de almacenamiento**, indicando las características del volumen que necesita.

Un desarrollador no necesita conocer los distintos tipos de volúmenes disponibles en el cluster. ¡Son detalles muy específicos!

Un desarrollador se centra en indicar los requerimientos que debe tener el volumen que necesita:

* Tamaño.
* Tipo de acceso (sólo lectura o lectura / escritura).
* Tipo de volumen (sólo si es importante).

Para hacer la solicitud de un volumen, el desarrollador debe crear un recurso en el cluster llamado *PersitentVolumenClaim*, veamos un ejemplo:

```yaml
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
    name: pvc1
spec:
  storageClassName: manual
  accessModes:
    - ReadWriteOnce
  resources:
    requests:
      storage: 1Gi
```

En esta solicitud el desarrollador indica los requisitos que necesita para su almacenamiento:

* `storageClassName: manual`: Con esto indicamos que no se use ningún aprovisionador dinámico. Si no pongo esta línea se intentaran asociar un volumen de forma dinámica.
* `accessModes`: El tipo de acceso que necesita.
* Y el tamaño que necesita en `resources`, `requests`, `storage`.

Una vez que se crea este recurso, el cluster intentará asignar un volumen (ya sea de forma estática o dinámica) que cumpla con los requisitos indicados.

## Vídeo

[https://www.youtube.com/watch?v=YV21W_hjo0Q](https://www.youtube.com/watch?v=YV21W_hjo0Q)
