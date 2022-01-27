# Introducción a la instalación de minikube

El "cluster" de k8s que vamos a utilizar en este curso es el de un
solo nodo que va a encargarse de realizar tanto las tareas de master,
con los componentes principales de Kubernetes, como de worker,
ejecutando las cargas de trabajo en contenedores (ya veremos más
adelante que realmente utiliza algo que se llama Pod).

Minikube se distribuye como un programa que se instala en nuestra
máquina física (podría instalarse igualmente en una máquina virtual a
la que tuviésemos acceso completo) y que al ejecutarlo crea una
máquina virtual linux con un cluster de Kubernetes completamente
configurado y listo para su uso. Podemos instalar minikube en nuestra
máquina con sistema linux, windows o mac y en una variedad importante
de sistemas de virtualización, aunque en el curso recomendaremos sólo
algunas combinaciones que hemos probado y que incluyen toda la
funcionalidad necesaria para realizar el curso.

**Nota:** Puede haber interacción si utilizamos más de un
sistema de virtualización en nuestro equipo, por ejemplo, la
utilización en Windows de virtualbox para unas cosas e hyper-v para
minikube, puede dar lugar a problemas, por lo que en general es
recomendable usar un solo sistema de virtualización.

Combinaciones de sistema operativo/virtualización recomendadas para el
curso:

* Linux + KVM
* Linux + VirtualBox
* Windows + HyperV
* Windows + VirtualBox
