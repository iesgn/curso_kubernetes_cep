# DaemonSet

El objeto [DaemonSet (DS)](https://kubernetes.io/docs/concepts/workloads/controllers/daemonset/) se utiliza cuando queremos ejecutar un pod en
todos los nodos del cluster o al menos en un conjunto de ellos que
tienen una serie de características en común. Un DaemonSet se utiliza
en algunas circunstancias muy concretas, por ejemplo:

* Ejecutar un pod en cada nodo para la monitorización del cluster:
  Prometheus, Sysdig, collectd, datadog, etc.
* Ejecutar un pod en cada nodo para la recolección y gestión de logs:
  fluentd, logstash
* Ejecutar un pod en cada nodo para el almacenamiento del cluster:
  ceph o glusterfs

Un ejemplo de DaemonSet tendría el siguiente aspecto:

```yaml
apiVersion: apps/v1
kind: DaemonSet
metadata:
  name: daemonset1
spec:
  selector:
      matchLabels:
        name: daemonset-pod 
  template:               # Plantilla con las características del Pod
    metadata:
      labels:
        name: daemonset-pod 
    spec:
      nodeSelector:
        type: worker-prod # Etiqueta del nodo en el que se ejecuta (opcional)
      containers:
      - name: daemon-pod
        image: ...
```

Los parámetros tienen los valores habituales anteriormente descritos y
en este caso, se incluye una plantilla con la descripción del pod que
se ejecutará en cada nodo (en este caso en cada nodo con etiqueta
worker-prod).

## Para seguir aprendiendo
* Para más información acerca de los DaemonSets puedes leer la
[documentación de la API](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.20/#daemonset-v1-apps)
