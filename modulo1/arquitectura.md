# Arquitectura básica

## Nodos

k8s es un software que se instala en varios nodos que se gestionan de
forma coordinada, es decir, un clúster de nodos. Aunque es posible en
casos muy peculiares instalar algunos [nodos sobre sistemas
Windows](https://kubernetes.io/docs/setup/production-environment/windows/intro-windows-in-kubernetes/),
la situación normal es que se trate de un cluster de nodos linux. No
es necesario que todos los nodos tengan la misma versión y ni siquiera
que sean la misma distribución, aunque en muchos casos sí lo sea por
simplicidad en el despliegue y mantenimiento.

Los nodos del clúster pueden ser máquinas físicas o virtuales, pero
quizás lo más habitual es que se traten de instancias de nube de
infraestructura, es decir, máquinas virtuales ejecutándose en algún
proveedor de IaaS (AWS, GCP, OpenStack, etc.)

Se distingue entre dos tipos de nodos:

* Los nodos *master*: Son los que ejecutan los servicios principales
de k8s y ordenan a los otros nodos los contenedores que deben
ejecutar. Como el uso del término master es últimamente muy
controvertido en los paises de habla inglesa, se está cambiando su
denominación por *control plane* node.
* Los nodos *worker*: Son los que reciben las órdenes de los
controladores y en los que se ejecutan los contenedores de las
aplicaciones.

## Componentes de un nodo master

* **kube-apiserver** Gestiona la API de k8s
* **etcd** Almacén clave-valor que guarda la configuración del clúster
* **kube-scheduler** Selecciona el nodo donde ejecutar los contenedores
* **kube-controller-manager** Ejecuta los controladores de k8s
* **docker/rkt/containerd/...** Ejecuta los contenedores que sean
  necesarios en el controlador
* **cloud-controller-manager** Ejecuta los controladores que
interactúan con el proveedor de nube:
  * nodos
  * enrutamiento
  * balanceadores
  * volúmenes

## Componentes de un nodo worker

* **kubelet** Controla los Pods asignados a su nodo
* **kube-proxy** Permite la conexión a través de la red
* **docker/rkt/containerd/...** Ejecuta los contenedores
* **supervisord** Monitoriza y controla kubelet y docker

## Complementos (addons)

Los elementos anteriores forman la estructura básica de k8s, pero es
muy habitual que se proporcione funcionalidad adicional a través de
complementos de k8s, que en muchas ocasiones se ejecutan a su vez como
contenedores y son gestionados por el propio Kubernetes. Algunos de
estos complementos son:

* **Cluster DNS** Proporciona registros DNS para los servicios de
  k8s. Normalmente a través de [CoreDNS](https://coredns.io/)
* **Web UI** Interfaz web para el manejo de k8s
* **Container Resource Monitoring** Recoge métricas de forma
centralizada. Múltiples opciones: [prometheus](https://prometheus.io/), [sysdig](https://sysdig.com/)
* **Cluster-level Logging** Almacena y gestiona los logs de los contenedores

## Esquema de nodos y componentes

Se crea un cluster de k8s en los que algunos nodos actúan como master
(normalmente se crea un conjunto impar de nodos master que
proporcionen alta disponibilidad) y el resto actúa como worker en los
que se ejecutan los contenedores de las aplicaciones. Los nodos se
comunican entre sí a través de una red que proporciona la capa de
infraestructura y se crea una red para la comunicación de los
contenedores, que suele ser una red de tipo
[overlay](https://en.wikipedia.org/wiki/Overlay_network).

<img src="https://github.com/iesgn/curso_kubernetes_cep/raw/main/modulo1/img/arquitectura.png" alt="arquitectura" />

## Vídeo

[https://www.youtube.com/watch?v=mF-OGBbA57k](https://www.youtube.com/watch?v=mF-OGBbA57k)
