# Instalación de kubectl en linux

**kubectl** es la herramienta de línea de comandos utilizada para
interactuar con la API de Kubernetes. Es por tanto la herramienta
fundamental que vamos a utilizar durante todo el curso para gestionar
nuestros objetos en el cluster recién creado con minikube.

kubectl está escrito en Go y de nuevo su instalación es muy simple, ya
que se trata de un binario enlazado estáticamente y sin
dependencias. Las instrucciones para su instalación están disponibles
en la [documentación de
k8s](https://kubernetes.io/es/docs/tasks/tools/install-kubectl/). A
continuación veremos algunas de las opciones que tenemos para
instalarlo.

## Opción 1. Instalar binario desde el proyecto

Al igual que hemos hecho con minikube, podemos descargar el binario
directamente desde la URL del proyecto e instalarlo en
`/usr/local/bin`:

```
curl -LO "https://storage.googleapis.com/kubernetes-release/release/$(curl -s https://storage.googleapis.com/kubernetes-release/release/stable.txt)/bin/linux/amd64/kubectl"
sudo install kubectl /usr/local/bin/kubectl
```

Este binario obviamente no se actualiza y tendremos que repetir el
proceso cuando se actualice.

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

En estos momentos se instala la versión 1.20 de kubectl.

## Opción 4. Instalar desde snap

Ubuntu no proporciona de forma directa un paquete con el cliente de
k8s, pero sí lo hace a través de snap, por lo que quienes utilicen
dicho sistema, lo tienen disponible con un simple:

```
sudo snap install kubectl --classic
```

## Configuración kubectl

Una vez instalado `kubectl` podemos comprobar que está disponible y cuál es su
versión, con la instrucción:

```
kubectl version
Client Version: version.Info{Major:"1", Minor:"23", GitVersion:"v1.23.3", GitCommit:"816c97ab8cff8a1c72eccca1026f7820e93e0d25", GitTreeState:"clean", BuildDate:"2022-01-25T21:25:17Z", GoVersion:"go1.17.6", Compiler:"gc", Platform:"linux/amd64"}
The connection to the server localhost:8080 was refused - did you specify the right host or port?
```

En el caso anterior, estamos utilizando la versión 1.22.2 y nos
informa de que no ha podido conectarse al cluster de Kubernetes con la
configuración por defecto (`localhost:8080`). Es decir, aunque
tengamos kubectl y minikube instalados, el primero no está configurado
todavía para conectarse al cluster de k8s que ejecuta minikube.

La solución más sencilla es parar minikube y volverlo a arrancar,
porque de esta manera minikube configurará automáticamente
`kubectl`. Si nos fijamos en la salida de minikube anterior, en la que
no teníamos instalado `kubectl`, aparecía la línea:

```
💡  kubectl not found. If you need it, try: 'minikube kubectl -- get pods -A'
```

Pero si lo volvemos a repetir ahora, esa línea no aparecerá y se
configurará `kubectl` para poder usar el cluster que proporciona
minikube. Lo que va a hacer minikube es configurar el fichero
`~/.kube/config` de la siguiente manera:

```
apiVersion: v1
clusters:
- cluster:
    certificate-authority: /home/alberto/.minikube/ca.crt
    extensions:
    - extension:
        last-update: Sun, 30 Jan 2022 20:45:08 CET
        provider: minikube.sigs.k8s.io
        version: v1.24.0
      name: cluster_info
    server: https://192.168.39.115:8443
  name: minikube
contexts:
- context:
    cluster: minikube
    extensions:
    - extension:
        last-update: Sun, 30 Jan 2022 20:45:08 CET
        provider: minikube.sigs.k8s.io
        version: v1.24.0
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
(en este caso la 192.168.39.221) y la ubicación de los ficheros de los
certificados y claves x509 (en este caso en el directorio
`/home/alberto`).

Una vez configurado correctamente `kubectl`, podemos repetir el
comando:

```
kubectl version

Client Version: version.Info{Major:"1", Minor:"23", GitVersion:"v1.23.3", GitCommit:"816c97ab8cff8a1c72eccca1026f7820e93e0d25", GitTreeState:"clean", BuildDate:"2022-01-25T21:25:17Z", GoVersion:"go1.17.6", Compiler:"gc", Platform:"linux/amd64"}
Server Version: version.Info{Major:"1", Minor:"22", GitVersion:"v1.22.3", GitCommit:"c92036820499fedefec0f847e2054d824aea6cd1", GitTreeState:"clean", BuildDate:"2021-10-27T18:35:25Z", GoVersion:"go1.16.9", Compiler:"gc", Platform:"linux/amd64"}
```

Comprobamos que ya aparece la versión del servidor y por
tanto se ha podido conectar con el cluster que gestiona
minikube. Además podemos ejecutar nuestro primer comando propiamente
de `kubectl`:

```
kubectl get nodes
NAME       STATUS   ROLES                  AGE   VERSION
minikube   Ready    control-plane,master   21m   v1.22.3
```

Si queremos utilizar el autocompletado, podemos generarlo e
incorporarlo a nuestro entorno con:

```
echo 'source <(kubectl completion bash)' >>~/.bashrc
```

Y para poder usarlo en esta misma sesión (no será necesario más
adelante, ya que el fichero .bashrc se lee cada vez que se inicia una
sesión):

```
source ~/.bashrc
```

## Vídeo

[https://www.youtube.com/watch?v=0p_JGucaSco](https://www.youtube.com/watch?v=0p_JGucaSco)
