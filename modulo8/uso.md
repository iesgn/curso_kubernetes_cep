# Uso de volúmenes

Una vez que hemos solicitado el almacenamiento, y se ha asignado un volumen (ya sea de forma dinámica o estática), vamos a definir el uso que se va a hacer de este volumen. 

Como ejemplo, vamos a definir un Pod que utilice dicho volumen, para ello vamos a crear un fichero yaml con la siguiente definición:

```yaml
kind: Pod
apiVersion: v1
metadata:
  name: task-pv-pod
spec:
  volumes:
    - name: task-pv-storage
      persistentVolumeClaim:
       claimName: pvc1
  containers:
    - name: task-pv-container
      image: nginx
      ports:
        - containerPort: 80
          name: "http-server"
      volumeMounts:
        - mountPath: "/usr/share/nginx/html"
          name: task-pv-storage
```

* En la especificación de este Pod, además de indicar el contenedor, hemos indicado que va a tener un volumen (campo `volumes`). 
* En realidad definimos una lista de volúmenes (en este caso solo definimos uno) indicando su nombre (`name`) y la solicitud del volumen (`persistentVolumeClaim`, `claimName`).
* Además en la definición del contenedor tendremos que indicar el punto de montaje del volumen (`volumeMounts`) señalando el directorio del contenedor (`mountPath`) y el nombre (`name`).

Cuando el Pod termina, el pvc mantiene el volumen reservado (bound). Es necesario que se borre explícitamente el pvc para liberarlo.

La recuperación del volumen dependerá de la política de reciclaje que tuviera asignada.
