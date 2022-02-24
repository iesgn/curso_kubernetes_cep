# StatefulSets

El objeto [StatefulSet](https://kubernetes.io/docs/concepts/workloads/controllers/statefulset/) controla el despliegue de Pods con identidades únicas y persistentes, y nombres de host estables. El uso de StatefulSets es alternativo al de despliegues (Deployments) y su objetivo principal es poder utilizar en Kubernetes aplicaciones más restrictivas que no se ajusten bien a las características de los despliegues, principalmente aplicaciones con estado que necesiten algunas características fijas y estables en los Pods, algo que no puede ocurrir con los despliegues en los pods que son completamente indistinguibles unos de otros y la aplicación puede utilizar cualquiera de ellos en cada momento.

Veamos algunos ejemplos en los es adecuado utilizar StatefulSet en lugar de Deployment y por qué:

* Un despliegue de redis primario-secundario: necesita que **el primario esté operativo antes de que podamos configurar las réplicas**.
* Un cluster mongodb: Los diferentes nodos deben **tener una identidad de red persistente** (ya que el DNS es estático), para que se produzca la sincronización después de reinicios o fallos.
* Zookeeper: cada nodo necesita **almacenamiento único y estable**, ya que el identificador de cada nodo se guarda en un fichero.

Por lo tanto el objeto StatefulSet nos ofrece las siguientes **características**:

* Estable y único identificador de red (Ejemplo mongodb)
* Almacenamiento estable (Ejemplo Zookeeper)
* Despliegues y escalado ordenado (Ejemplo redis)
* Eliminación y actualizaciones ordenadas

**Por lo tanto cada Pod es distinto (tiene una identidad única)**, y este hecho tiene algunas consecuencias:

* El nombre de cada Pod tendrá un número (1,2,...) que lo identifica y que nos proporciona la posibilidad de que la creación actualización y eliminación sea ordenada. Se crearán en orden ascendente y se eliminarán en orden descendente.
* Si un nuevo Pod es recreado, obtendrá el mismo nombre (hostname), los mismos nombres DNS (aunque la IP pueda cambiar) y el mismo volumen que tenía asociado.
* Necesitamos crear un Service especial, llamado **Headless Service**, que nos permite acceder a los Pods de forma independiente, pero que no balancea la carga entre ellos, por lo tanto este Service no tendrá una ClusterIP.

## StatefulSet vs Deployment

* A diferencia de un Deployment, un StatefulSet mantiene una identidad fija para cada uno de sus Pods.
* Eliminar y/o escalar un StatefulSet no eliminará los volúmenes asociados con StatefulSet.
* StatefulSets actualmente requiere que un Headless Service sea responsable de la identidad de red de los Pods.
* Al utilizar StatefulSet, cada Pod recibe un PersistentVolume independiente.
* StatefulSet actualmente no admite el escalado automático.

## Creando el *Headless Service* para acceder a los Pods del StatefulSet

Una de las características de los Pods controlados por un StatefulSet es que son únicos (todos los Pods son distintos), por lo tanto al acceder a ellos por medio de la definición de un Service no necesitamos el balanceo de carga entre ellos.

Para acceder a los Pods de un StatefulSet vamos a crear un Service Headless que se caracteriza por no tener IP (ClusterIP) y por lo tanto no va a balancear la carga entre los distintos Pods. Este tipo de Service va a crear una entrada DNS por cada Pod, que nos permitirá acceder a cada Pod de forma independiente. El nombre DNS que se creará será `<nombre del Pod>.<dominio del StatefulSet>`. El dominio del StatefulSet se indicará en la definición del recurso usando el parámetro `serviceName`.

Veamos un ejemplo de definición de un Headless Service (fichero [`service.yaml`](files/ejemplo1/service.yaml):

```yaml
apiVersion: v1
kind: Service
metadata:
  name: nginx
  labels:
    app: nginx
spec:
  ports:
  - port: 80
    name: web
  clusterIP: None
  selector:
    app: nginx
```

En esta definición podemos observar que al indicar `clusterIP: None` estamos creando un Headless Service, que no tendrá ClusterIP (por lo que no balanceará la carga entre los pods). Este Service será el responsable de crear, por cada Pod seleccionado con el `selector`, una entrada DNS.

## Creando el recurso StatefulSet

Vamos a definir nuestro recurso StatefulSet en un fichero yaml [`statefulset.yaml`](files/ejemplo1/statefulset.yaml):

```yaml
apiVersion: apps/v1
kind: StatefulSet
metadata:
  name: web
spec:
  serviceName: "nginx"
  replicas: 2
  selector:
    matchLabels:
      app: nginx
  template:
    metadata:
      labels:
        app: nginx
    spec:
      containers:
      - name: nginx
        image: k8s.gcr.io/nginx-slim:0.8
        ports:
        - containerPort: 80
          name: web
        volumeMounts:
        - name: www
          mountPath: /usr/share/nginx/html
  volumeClaimTemplates:
  - metadata:
      name: www
    spec:
      accessModes: [ "ReadWriteOnce" ]
      resources:
        requests:
          storage: 1Gi
```

Vamos a estudiar las características de la definición de este recurso:

* Con el parámetro `serviceName` indicaremos el nombre de dominio que va a formar parte del nombre DNS que el Headless Service va a crear para cada Pod.
* Con el parámetro `selector` se indica los Pods que vamos a controlar con StatefulSet.
* Una de las características que hemos indicado del StatefulSet es que cada Pod va a tener un almacenamiento estable. El tipo de almacenamiento se indica con el parámetro `volumeClaimTemplates` que se define de forma similar a un `PersistentVolumenClaim`.
* Además observamos en la definición del contenedor que el almacenamiento que hemos definido se va a montar en cada Pod (en este ejemplo el punto de montaje es el DocumentRoot de nginx), con el parámetro `volumeMounts`.

## Ejemplo: Creación de un StatefulSet

Vamos a crear los recursos estudiados en este apartado: el Service Headless y el StatefulSet, y vamos a comprobar sus características.

Lo primero es crear el Headless Service:

```bash
kubectl apply -f service.yaml
```

### Creación ordenada de Pods

El statefulSet que hemos definido va a crear dos Pods (`replicas: 2`). Para observar cómo se crean de forma ordenada podemos usar dos terminales, en la primera ejecutamos:

```bash
watch kubectl get pod
```

Con esta instrucción vamos a ver en "vivo" cómo se van creando los Pods, que vamos a crear al ejecutar en otra terminal la instrucción:

```bash
kubectl apply -f statefulset.yaml
```

### Comprobamos la identidad de red estable

En este caso vamos a comprobar que los hostname y los nombres DNS son estables para cada Pod. Las ips de los Pods pueden cambiar si eliminamos el recurso StatefulSet y lo volvemos a crear, pero los nombres van a permanecer.

Para ver los nombres de los Pods podemos ejecutar lo siguiente:

```bash
for i in 0 1; do kubectl exec web-$i -- sh -c 'hostname'; done
web-0
web-1
```

Veamos los nombres DNS. En este ejemplo el Headless Service ha creado una entrada en el DNS para cada Pod. El nombre DNS que se creará será `<nombre del pod>.<dominio del StatefulSet>`. El dominio del StatefulSet se indicará en la definición del recurso usando el parámetro `serviceName`. En este caso el nombre del primer Pod será `web-0.nginx`. Vamos a comprobarlo, haciendo una consulta DNS desde otro pod:

```bash
kubectl run -i --tty --image busybox:1.28 dns-test --restart=Never --rm
/ # nslookup web-0.nginx
...
Address 1: 172.17.0.4 web-0.nginx.default.svc.cluster.local
/ # nslookup web-1.nginx
...
Address 1: 172.17.0.5 web-1.nginx.default.svc.cluster.local
```

### Eliminación de pods

Podemos usar las dos terminales para observar cómo la eliminación también se hace de forma ordenada. En la primera terminal ejecutamos:

```bash
watch kubectl get pod
```

Y en la segunda:

```bash
kubectl delete pod -l app=nginx
```

Al eliminar los Pods, el statefulSet ha creado nuevos Pods que serán idénticos a los anteriores y por lo tanto mantendrán la identidad de red, es decir tendrán los mismos hostname y los mismos nombres DNS (aunque es posible que cambien las ip):

```bash
for i in 0 1; do kubectl exec web-$i -- sh -c 'hostname'; done
web-0
web-1

kubectl run -i --tty --image busybox:1.28 dns-test --restart=Never --rm
/ # nslookup web-0.nginx
...
/ # nslookup web-1.nginx
...
```

### Escribiendo en los volúmenes persistente

Podemos comprobar que se han creado los distintos volúmenes para cada pod:

```bash
kubectl get pv,pvc
```

Y podemos comprobar que realmente la información que guardemos en el directorio que hemos montado en cada Pod es persistente:

```bash
for i in 0 1; do kubectl exec "web-$i" -- sh -c 'echo "$(hostname)" > /usr/share/nginx/html/index.html'; done
for i in 0 1; do kubectl exec -i -t "web-$i" -- sh -c 'curl http://localhost/'; done
web-0
web-1
```

Ahora si eliminamos los Pods, los nuevos Pods creados mantendrán la información:

```bash
kubectl delete pod -l app=nginx
for i in 0 1; do kubectl exec -i -t "web-$i" -- sh -c 'curl http://localhost/'; done
web-0
web-1
```

## Vídeo

[https://www.youtube.com/watch?v=ULaNgtJ8NHQ](https://www.youtube.com/watch?v=ULaNgtJ8NHQ)
