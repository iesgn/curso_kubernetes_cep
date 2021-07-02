# Instalación de minikube

El "cluster" de k8s que vamos a utilizar en este curso es el de un
solo nodo que va a encargarse de realizar tanto las tareas de master,
con los componentes principales de kubernetes, como de worker,
ejecutando las cargas de trabajo en contenedores (ya veremos más
adelante que realmente utiliza algo que se llama pod). Aunque
evidentemente un cluster constituido por un solo nodo no es la
solución más adecuada en la mayoría de los casos, sí lo es en éste, en
el que queremos instalar kubernetes de forma rápida y fácil para
aprender sus características, pero no para usarlo en producción ni
nada similar.

## Instalación del binario minikube

Accedemos a
[https://minikube.sigs.k8s.io/docs/start/](https://minikube.sigs.k8s.io/docs/start/)
y seleccionamos el método que prefiramos para instalar, eligiendo
nuestro sistema operativo, arquitectura, etc.

Minikube se instala, como otras aplicaciones de Go, como un binario
enlazado estáticamente (autoconsistente), que no tiene dependencias de
nada y que tenemos que ubicar en algún directorio del PATH de nuestro
sistema. Veamos en particular la instalación directa del binario en un
sistema linux:

Paso 1: Descargamos como usuario normal y con ayuda de la aplicación
curl, la última versión del binario de minikube (en este caso para
arquitectura x86-64):

    usuario@equipo:~$ curl -LO https://storage.googleapis.com/minikube/releases/latest/minikube-linux-amd64

Paso 2: Movemos el binario a un directorio del PATH (lo recomendable
en este caso sería /usr/local/bin/) y establecemos permisos de
ejecución. Todo esto puede hacerse con los comandos `mv` y `chmod`, o
de forma más sencilla con `install`

    usuario@equipo:~$ sudo install minikube-linux-amd64	/usr/local/bin/minikube

Comprobamos que se ha instalado correctamente con:

    usuario@equipo:~$ minikube version
    minikube version: v1.21.0
    commit: 76d74191d82c47883dc7e1319ef7cebd3e00ee11

## Creación del cluster de k8s

