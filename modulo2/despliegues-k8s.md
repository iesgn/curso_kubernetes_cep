# Despliegues de aplicaciones en Kubernetes

Vamos a resumir brevemente, con la ayuda de un par de imágenes, la
forma que tiene k8s de hacer despliegues de aplicaciones y lo compararemos
con un despliegue "tradicional".

Aunque un despliegue real tiene
muchos más elementos que los que vamos a exponer a continuación, con
idea de simplificarlo todo y centrarnos en la diferencia de los
elementos que intervienen, supondremos una aplicación "tradicional" de
dos capas, en las que una serie de equipos son los que están expuestos
a Internet y los que pueden ejecutar una parte del código de la
aplicación a través de servidores web (a los que de forma genérica
denominaremos "front-end"), mientras que otra serie de equipos
ejecutan otra parte de código y gestionan el almacenamiento y las
bases de datos (a los que llamaremos de forma genérica "back-end").

<img src="https://github.com/iesgn/curso_kubernetes_cep/raw/main/modulo2/img/esquema-tradicional.png" alt="esquema-tradicional" />

En la imagen anterior, vemos que el balanceador de carga expuesto al
exterior recibe la petición, que asigna a alguna de las máquinas
virtuales o físicas que forman el "front-end" y que éstas a su vez se
comunican con alguna de las máquinas del "back-end" a través del
balanceador de carga intermedio.

En el caso de Kubernetes, esto se realiza utilizando una serie de
objetos internos, que normalmente se ejecutan sobre contenedores,
denominados Pods, ReplicaSets,  Deployments, Services e
Ingress Controllers. Hay bastantes más objetos de k8s, pero nos
centraremos en éstos que son los principales. 

En la siguiente imagen
podemos ver la forma en la que una petición externa se gestionaría:

<img src="https://github.com/iesgn/curso_kubernetes_cep/raw/main/modulo2/img/esquema-k8s.png" alt="esquema-k8s" />

En los siguientes módulos veremos uno a uno estos objetos de k8s y
aprenderemos paso a paso cómo se interactúa con ellos y cómo se
definen, pero a modo de resumen, podemos enumerar sus principales
funciones en la siguiente lista:

* Pods: ejecutan los contenedores
* ReplicaSets:
  * Se encargan de que no haya caída del servicio
  * Gestionan la tolerancia a fallos
  * Proporcionan escalabilidad dinámica
* Deployments:
  * Gestionan las actualizaciones continuas
  * Realizan despliegues automáticos
* Services:
  * Gestionan el acceso a los pods
  * Balancean la carga entre los Pods disponibles
* Ingress:
  * Gestionan el acceso desde el exterior a través de nombre

## Vídeo

[https://www.youtube.com/watch?v=9bCXCemP4aY](https://www.youtube.com/watch?v=9bCXCemP4aY)
