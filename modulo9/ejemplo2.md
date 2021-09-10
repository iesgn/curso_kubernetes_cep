# Ejemplo 2: Despliegue de un cluster de MySQL

Una base de datos relacional es un ejemplo perfecto de aplicación con
estado, cualquier petición puede depender del estado resultante de una
petición anterior, y todas las peticiones deben consultar o
modificar la base de datos que incluya la última modificación
realizada. Las implicaciones que tiene esto si queremos desplegar la
base de datos sobre Kubernetes son importantes, ya que será necesario
que la base de datos se pueda desplegar en un cluster para
proporcionar disponibilidad, se pueda adaptar a variaciones de demanda
y no haya interrupciones, mientras que hay que garantizar que todos
los pods accedan a la base de datos de forma coherente.

* ¿Podemos utilizar un Deployment con réplicas indistinguibles que se
crean o destruyen a demanda?
* ¿Necesitamos un volumen adicional para almacenar localmente la base
  de datos en cada pod?
* ¿Cómo garantizamos la replicación de la base de datos entre los
  nodos?

Hay diferentes formas de afrontar esto y dependen mucho de las
características de la base de datos en cuestión. En este ejemplo vamos
a desplegar un cluster de MySQL con un nodo primario (también
denominado *master*) en modo lectura y escritura (se podrán hacer
consultas y modificaciones de la base de datos) y varios nodos
secundarios en modo lectura (sólo se utilizarán para realizar
consultas). Utilizaremos para ello un StatefulSet, en el que los
diferentes pods son distinguibles entre sí, tienen siempre el mismo
nombre DNS interno y el mismo volumen se conecta siempre al mismo
pod. El primer nodo que se desplegará será el primario, con un volumen
asociado para la base de datos, el resto de nodos se arrancarán
después del primario y al iniciarse sincronizarán la base de datos con
la del primario y la almacenarán también en un volumen diferente para
cada pod.

Este ejemplo es probablemente el más avanzado de todo el curso y
utilizaremos además otros recursos como ConfigMap, Services o
volúmenes. Este ejemplo está extraído directamente de la documentación
de k8s: [Run a Replicated Stateful
Application](https://kubernetes.io/docs/tasks/run-application/run-replicated-stateful-application/).

**Nota** Las características de este cluster no son para poner en
producción, ya que se ha simplificado la configuración de MySQL, para
centrarnos en los aspectos relacionados con Kubernetes.

**Nota** Para este ejemplo es posible que la máquina virtual que hemos
creado para instalar minikube no tenga recursos suficientes, por lo
que habría que eliminar el cluster y volverlo a crear con suficientes
recursos (en el ejemplo siguiente creamos un nuevo cluster de k8s con
8 GiB de RAM y 4 cores virtuales:

```
minikube stop
minikube delete
minikube start --driver ... --memory 8192 --cpus 4
```

Aunque si no disponemos de esos recursos, podría modificarse el
StatefulSet limitando el número de réplicas a dos.

Vamos pues con la creación de este cluster, para lo que utilizaremos
diferentes objetos de Kubernetes que hemos visto durante todo el
curso.

Creamos un ConfigMap para modificar el fichero de configuración de
MySQL, de manera que el primario genere los registros para la
sincronización y los secundarios actúen en modo lectura:
[configmap.yaml](ejemplo1/configmap.yaml)

```yaml
apiVersion: v1
kind: ConfigMap
metadata:
  name: mysql
  labels:
    app: mysql
data:
  primary.cnf: |
    # Modificación del primario
    [mysqld]
    log-bin
  replica.cnf: |
    # Modificación de los secundarios
    [mysqld]
    super-read-only
```

```
kubectl apply -f configmap.yaml
```

Creamos dos servicios, uno de tipo Headless asociado con el
StatefulSet para gestionar los nombres internos de los pods y otro
para balancear entre los diferentes pods secundarios las peticiones de
lectura: [servicios.yaml](ejemplo1/servicios.yaml)

```yaml
# Servicio para usar los nombres DNS internamente
apiVersion: v1
kind: Service
metadata:
  name: mysql
  labels:
    app: mysql
spec:
  ports:
  - name: mysql
    port: 3306
  clusterIP: None
  selector:
    app: mysql
---
# Servicio para balancear los clientes entre los nodos secundarios
# en modo lectura
apiVersion: v1
kind: Service
metadata:
  name: mysql-read
  labels:
    app: mysql
spec:
  ports:
  - name: mysql
    port: 3306
  selector:
    app: mysql
```

```
kubectl apply -f servicios.yaml
```

Y ya por último creado el StatefulSet, que en este caso es el objeto
más complicado que vamos a ver en este curso. Veamos los elementos que
utiliza:

* Está formado inicialmente por tres pods, de los que en el primero se
ejecutará el servidor MySQL primario y en los otros dos los servidores
MySQL secundarios.

* Se define un volumen de 10 GiB para cada pod a través de un
  volumeClaim.

* Utiliza dos contenedores en cada pod, el principal que se encarga de
  ejecutar el proceso mysql y uno adicional que se encarga de la
  sincronización de la base de datos mediante
  [XtraBackup](https://www.percona.com/software/mysql-database/percona-xtrabackup). Ambos
  contenedores deben poder acceder al mismo volumen en el que se
  encuentra la base de datos, en el punto de montaje `/var/lib/mysql`.

* Utiliza [InitContainers](https://kubernetes.io/docs/concepts/workloads/pods/init-containers/)
que no hemos visto en el curso; estos contenedores se ejecutan dentro
del pod antes del contenedor normal y se utilizan para realizar
configuraciones o modificaciones previas a la utilización del
contenedor que va a ejecutar la aplicación. Una vez que el
InitContainer ha finalizado se lanza el contenedor normal. En este
caso se utilizan para la configuración inicial del contenedor mysql
mediante un script que se lanza como un comando (si el índice es 0 configura el contenedor como primario y si es otro
número, lo hace como secundario). El otro InitContainer se utiliza
para clonar inicialmente la base de datos en los secundarios con
`xtrabackup`.

* Se establecen límite de consumo de recursos y se definen las pruebas
  de disponibilidad para que Kubernetes pueda comprobar si se está
  ofreciendo el servicio de forma adecuada.

* Se define el acceso a la base de datos sin contraseña, lo que hace
  que el sistema no sea válido para un despliegue real.

[statefulset.yaml](ejemplo1/statefulset.yaml)
```yaml
apiVersion: apps/v1
kind: StatefulSet
metadata:
  name: mysql
spec:
  selector:
    matchLabels:
      app: mysql
  serviceName: mysql
  replicas: 3
  template:
    metadata:
      labels:
        app: mysql
    spec:
      initContainers:
      - name: init-mysql
        image: mysql:5.7
        command:
        - bash
        - "-c"
        - |
          set -ex
          # Generate mysql server-id from pod ordinal index.
          [[ `hostname` =~ -([0-9]+)$ ]] || exit 1
          ordinal=${BASH_REMATCH[1]}
          echo [mysqld] > /mnt/conf.d/server-id.cnf
          # Add an offset to avoid reserved server-id=0 value.
          echo server-id=$((100 + $ordinal)) >> /mnt/conf.d/server-id.cnf
          # Copy appropriate conf.d files from config-map to emptyDir.
          if [[ $ordinal -eq 0 ]]; then
            cp /mnt/config-map/primary.cnf /mnt/conf.d/
          else
            cp /mnt/config-map/replica.cnf /mnt/conf.d/
          fi
        volumeMounts:
        - name: conf
          mountPath: /mnt/conf.d
        - name: config-map
          mountPath: /mnt/config-map
      - name: clone-mysql
        image: gcr.io/google-samples/xtrabackup:1.0
        command:
        - bash
        - "-c"
        - |
          set -ex
          # Skip the clone if data already exists.
          [[ -d /var/lib/mysql/mysql ]] && exit 0
          # Skip the clone on primary (ordinal index 0).
          [[ `hostname` =~ -([0-9]+)$ ]] || exit 1
          ordinal=${BASH_REMATCH[1]}
          [[ $ordinal -eq 0 ]] && exit 0
          # Clone data from previous peer.
          ncat --recv-only mysql-$(($ordinal-1)).mysql 3307 | xbstream -x -C /var/lib/mysql
          # Prepare the backup.
          xtrabackup --prepare --target-dir=/var/lib/mysql
        volumeMounts:
        - name: data
          mountPath: /var/lib/mysql
          subPath: mysql
        - name: conf
          mountPath: /etc/mysql/conf.d
      containers:
      - name: mysql
        image: mysql:5.7
        env:
        - name: MYSQL_ALLOW_EMPTY_PASSWORD
          value: "1"
        ports:
        - name: mysql
          containerPort: 3306
        volumeMounts:
        - name: data
          mountPath: /var/lib/mysql
          subPath: mysql
        - name: conf
          mountPath: /etc/mysql/conf.d
        resources:
          requests:
            cpu: 500m
            memory: 1Gi
        livenessProbe:
          exec:
            command: ["mysqladmin", "ping"]
          initialDelaySeconds: 30
          periodSeconds: 10
          timeoutSeconds: 5
        readinessProbe:
          exec:
            # Check we can execute queries over TCP (skip-networking is off).
            command: ["mysql", "-h", "127.0.0.1", "-e", "SELECT 1"]
          initialDelaySeconds: 5
          periodSeconds: 2
          timeoutSeconds: 1
      - name: xtrabackup
        image: gcr.io/google-samples/xtrabackup:1.0
        ports:
        - name: xtrabackup
          containerPort: 3307
        command:
        - bash
        - "-c"
        - |
          set -ex
          cd /var/lib/mysql

          # Determine binlog position of cloned data, if any.
          if [[ -f xtrabackup_slave_info && "x$(<xtrabackup_slave_info)" != "x" ]]; then
            # XtraBackup already generated a partial "CHANGE MASTER TO" query
            # because we're cloning from an existing replica. (Need to remove the tailing semicolon!)
            cat xtrabackup_slave_info | sed -E 's/;$//g' > change_master_to.sql.in
            # Ignore xtrabackup_binlog_info in this case (it's useless).
            rm -f xtrabackup_slave_info xtrabackup_binlog_info
          elif [[ -f xtrabackup_binlog_info ]]; then
            # We're cloning directly from primary. Parse binlog position.
            [[ `cat xtrabackup_binlog_info` =~ ^(.*?)[[:space:]]+(.*?)$ ]] || exit 1
            rm -f xtrabackup_binlog_info xtrabackup_slave_info
            echo "CHANGE MASTER TO MASTER_LOG_FILE='${BASH_REMATCH[1]}',\
                  MASTER_LOG_POS=${BASH_REMATCH[2]}" > change_master_to.sql.in
          fi

          # Check if we need to complete a clone by starting replication.
          if [[ -f change_master_to.sql.in ]]; then
            echo "Waiting for mysqld to be ready (accepting connections)"
            until mysql -h 127.0.0.1 -e "SELECT 1"; do sleep 1; done

            echo "Initializing replication from clone position"
            mysql -h 127.0.0.1 \
                  -e "$(<change_master_to.sql.in), \
                          MASTER_HOST='mysql-0.mysql', \
                          MASTER_USER='root', \
                          MASTER_PASSWORD='', \
                          MASTER_CONNECT_RETRY=10; \
                        START SLAVE;" || exit 1
            # In case of container restart, attempt this at-most-once.
            mv change_master_to.sql.in change_master_to.sql.orig
          fi

          # Start a server to send backups when requested by peers.
          exec ncat --listen --keep-open --send-only --max-conns=1 3307 -c \
            "xtrabackup --backup --slave-info --stream=xbstream --host=127.0.0.1 --user=root"
        volumeMounts:
        - name: data
          mountPath: /var/lib/mysql
          subPath: mysql
        - name: conf
          mountPath: /etc/mysql/conf.d
        resources:
          requests:
            cpu: 100m
            memory: 100Mi
      volumes:
      - name: conf
        emptyDir: {}
      - name: config-map
        configMap:
          name: mysql
  volumeClaimTemplates:
  - metadata:
      name: data
    spec:
      accessModes: ["ReadWriteOnce"]
      resources:
        requests:
          storage: 10Gi
```

```
kubectl apply -f statefulset.yaml
```

Podemos ir comprobando con `kubectl` cómo se van creando los
diferentes pods y contenedores, tanto los InitContainers como los
contenedores de cada pod y al tratarse de un StatefulSet, los pods no
se crean en paralelo, lo hacen de manera secuencial (algo fundamental
en este caso, ya que hasta que no ha terminado el primer pod que
contiene el contendor primario, no deben lanzarse los secundarios).

## Prueba de funcionamiento de la base de datos

Creamos un pod efímero con un cliente de MySQL para crear una tabla
con un registro en el pod mysql-0 (con nombre DNS mysql-0.mysql):

```
kubectl run mysql-client --image=mysql:5.7 -i --rm --restart=Never --\
  mysql -h mysql-0.mysql <<EOF
CREATE DATABASE prueba;
CREATE TABLE prueba.saludos (mensaje VARCHAR(250));
INSERT INTO prueba.saludos VALUES ('Bienvenidos al curso del CEP de k8s');
EOF
```

Una vez realizada la modificación en la base de datos, se eliminará el
pod con el cliente MySQL. Creamos a continuación otro pod que
realizará una consulta a la base de datos, pero lo hará a `mysql-read`
con lo que comprobaremos que se ha realizado la sincronización a los
secundarios:

```
kubectl run mysql-client --image=mysql:5.7 -i -t --rm --restart=Never --\
  mysql -h mysql-read -e "SELECT * FROM prueba.saludos"
```

Podemos comprobar los servidores que responden a una consulta a
`mysql-read` solicitando el identificador del servidor en unas cuantas
de iteraciones:

```
kubectl run mysql-client-loop --image=mysql:5.7 -i -t --rm --restart=Never --\
  bash -ic "for i in `seq 1 10`; do mysql -h mysql-read -e 'SELECT
  @@server_id,NOW()'; sleep 1; done"
```
