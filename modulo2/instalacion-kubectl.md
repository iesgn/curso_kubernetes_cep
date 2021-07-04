# Instalación de kubectl

kubectl es la herramienta de línea de comandos para interactuar con la
API de kubernetes, es por tanto la herramienta fundamental que vamos a
utilizar durante todo el curso para gestionar nuestros objetos en el
cluster recién creado con minikube.

kubectl está escrito en Go y de nuevo su instalación es muy simple, ya
que se trata de un binario enlazado estáticamente y sin
dependencias. Las instrucciones para su instalación están disponibles
en la [documentación de
k8s](https://kubernetes.io/es/docs/tasks/tools/install-kubectl/).

## Opción 1. Instalar binario desde el proyecto

Al igual que hemos hecho con minikube, podemos descargar el binario
directamente desde la URL del proyecto e instalarlo en
`/usr/local/bin`:

```
curl -LO
"https://storage.googleapis.com/kubernetes-release/release/$(curl -s
https://storage.googleapis.com/kubernetes-release/release/stable.txt)/bin/linux/amd64/kubectl"
chmod +x ./kubectl
sudo mv ./kubectl /usr/local/bin/kubectl
```

Este binario obviamente no se actualiza y tendremos que repetir el
proceso cuando cambiemos la versión de k8s.

## Opción 2. Instalar desde repositorios no oficiales

El término repositorio no oficial se utiliza para aquellos
repositorios que se añaden y que no son los propios de la distribución
que estamos utilizando. En este caso, los repositorios no oficiales
los proporciona el propio proyecto k8s.

En el caso de las distribuciones Debian y derivadas, el repositorio es
`https://packages.cloud.google.com/apt/` y en la documentación se
detallan los pasos para instalar `kubectl` a través de apt.

La ventaja de este método respecto al anterior es que sí se
actualizará `kubectl` adecuadamente como cualquier otro paquete que
tengamos instalado en nuestra distro.

## Opción 3. Instalar desde repositorio oficial

En el caso de Debian, se ha añadido soporte para Kubernetes a partir
de la versión `bullseye` o Debian 11, por lo que si tenemos instalada
esa versión, podemos instalar `kubectl` directamente con apt:

```
sudo apt install kubernetes-client
```

## Opción 4. Instalar desde snap

Ubuntu no proporciona de forma directa un paquete con el cliente de
k8s, pero sí lo hace a través de snap, por lo que quienes utilicen
dicho sistema, lo tienen disponible con un simple:

```
sudo snap install kubectl --classic
```

## Configuración kubectl

Una vez instalado `kubectl` podemos comprobar que está disponible y su
versión con:

```
usuario@equipo:~$ kubectl version
Client Version: version.Info{Major:"1", Minor:"20", GitVersion:"v1.20.2", GitCommit:"faecb196815e248d3ecfb03c680a4507229c2a56", GitTreeState:"archive", BuildDate:"2021-01-14T10:55:09Z", GoVersion:"go1.15.6", Compiler:"gc", Platform:"linux/amd64"}
The connection to the server localhost:8080 was refused - did you
specify the right host or port?
```

En el caso anterior, estamos utilizando la versión 1.20.2 y nos
informa de que no ha podido conectarse al cluster de kubernetes con la
configuración por defecto (`localhost:8080`). Es decir, aunque
tengamos kubectl y minikube instalados, el primero no está configurado
todavía para conectarse al cluster de k8s que ejecuta minikube.

La solución más sencilla es parar minikube y volverlo a arrancar,
porque de esta manera minikube configurará automáticamente
`kubectl`. Lo que va a hacer minikube es configurar el fichero
`~/.kube/config` de la siguiente manera:

```
apiVersion: v1
clusters:
- cluster:
    certificate-authority: /home/alberto/.minikube/ca.crt
    extensions:
    - extension:
        last-update: Sun, 04 Jul 2021 11:25:04 CEST
        provider: minikube.sigs.k8s.io
        version: v1.21.0
      name: cluster_info
    server: https://192.168.39.69:8443
  name: minikube
contexts:
- context:
    cluster: minikube
    extensions:
    - extension:
        last-update: Sun, 04 Jul 2021 11:25:04 CEST
        provider: minikube.sigs.k8s.io
        version: v1.21.0
      name: context_info
    namespace: default
    user: minikube
  name: minikube
current-context: minikube
kind: Config
preferences: {}
users:
- name: minikube
  user:
    client-certificate: /home/alberto/.minikube/profiles/minikube/client.crt
    client-key: /home/alberto/.minikube/profiles/minikube/client.key
```

Donde en cada caso variará la dirección IP del servidor del cluster
(en este caso la 192.168.39.69) y la ubicación de los ficheros de los
certificados y claves x509 (en este caso en el directorio
`/home/alberto`).

Una vez configurado correctamente `kubectl`, podemos repetir el
comando:

```
kubectl version
Client Version: version.Info{Major:"1", Minor:"20", GitVersion:"v1.20.2", GitCommit:"faecb196815e248d3ecfb03c680a4507229c2a56", GitTreeState:"archive", BuildDate:"2021-01-14T10:55:09Z", GoVersion:"go1.15.6", Compiler:"gc", Platform:"linux/amd64"}
Server Version: version.Info{Major:"1", Minor:"20", GitVersion:"v1.20.7", GitCommit:"132a687512d7fb058d0f5890f07d4121b3f0a2e2", GitTreeState:"clean", BuildDate:"2021-05-12T12:32:49Z", GoVersion:"go1.15.12", Compiler:"gc", Platform:"linux/amd64"}
```

En el que comprobamos que ya aparece la versión del servidor y por
tanto se ha podido conectar con el cluster que gestiona
minikube. Además podemos ejecutar nuestro primer comando propiamente
de `kubectl`:

```
kubectl get nodes
NAME       STATUS   ROLES                  AGE   VERSION
minikube   Ready    control-plane,master   23h   v1.20.7
```

