# Pod

La unidad más pequeña que puede utilizar Kubernetes es el Pod, en inglés pod significa "vaina", y podemos entender un pod como una envoltura que contiene uno o varios contenedores (en la mayoría de los casos un solo contenedor). Un pod representa un conjunto de contenedores que comparten almacenamiento y una única IP. Un aspecto muy importante que hay que ir asumiendo es que los pods son efímeros, se lanzan y en determinadas circunstancias se paran o se destruyen, creando en muchos casos nuevos pods que sustituyan a los anteriores. Esto tiene importantes ventajas a la hora de realizar modificaciones en los despliegues en producción, pero tiene una consecuencia directa sobre la información que pueda tener almacenada el pod, por lo que tendremos que utilizar algún mecanismo adicional cuando necesitemos que la información sobreviva a un pod. 

Por lo tanto, aunque Kubernetes es un orquestador de contenedores, **la unidad mínima de ejecución es el pod**, que contendrá uno a más contenedores según las necesidades:

* En la mayoría de los casos, y siguiendo el principio de un proceso por contenedor, evitamos tener sistemas (como máquinas virtuales) ejecutando docenas de procesos, por lo que lo más habitual será tener un pod en cuyo interior se define un contenedor que ejecuta un solo proceso.


* En determinadas circunstancias será necesario ejecutar más de un proceso en el mismo "sistema", como en los casos de procesos fuertemente relacionados, en esos casos tendremos más de un contenedor dentro del pod. Cada uno de los contenedores ejecutando un solo proceso, pero pudiendo compartir almacenamiento y una misma dirección IP como si se tratase de un sistema ejecutando múltiples procesos.

Existen además algunas razones que hacen que sea conveniente tener esta capa adicional por encima de la definición de contenedor:

* Kubernetes puede trabajar con distintos sistemas de gestión de contenedores (docker, containerd, rocket, cri-o, etc) por lo que es muy conveniente añadir una capa de abstracción que permita utilizar Kubernetes de una forma homogénea e independiente del sistema de contenedores interno asociado.


* Esta capa de abstracción añade información adicional necesaria en Kubernetes como por ejemplo, políticas de reinicio, comprobaciones de que la aplicación esté inicializada (readiness probe) o comprobaciones de que la aplicación haya realizado alguna acción especificada (liveness probe).

## Pod con un solo contenedor

En la situación más habitual, se definirá un pod con un contenedor en su interior para ejecutar un solo proceso y este pod estará ejecutándose mientras lo haga el correspondiente proceso dentro del contenedor. Algunos ejemplos pueden ser: ejecución en modo demonio de un servidor web, ejecución de un servidor de aplicaciones Java, ejecución de una tarea programada, ejecución en modo demonio de un servidor DNS, etc. 

## Pod multicontenedor

En algunos casos la ejecución de un solo proceso por contenedor no es la solución ideal, ya que existen procesos fuertemente acoplados que no pueden comunicarse entre sí fácilmente si se ejecutan en diferentes sistemas. La solución planteada en esos casos es definir un pod multicontenedor y ejecutar cada proceso en un contenedor, pudiéndose comunicar entre ellos como si lo estuvieran haciendo en el mismo sistema, utilizando un dispositivo de almacenamiento compartido si hiciese falta (para leer, escribir ficheros entre ellos) y compartiendo externamente una misma dirección IP. 

Un ejemplo típico de un pod multicontenedor es un servidor web nginx con un servidor de aplicaciones PHP-FPM, que se implementaría mediante un solo pod, pero ejecutando un proceso de nginx en un contenedor y otro proceso de php-fpm en otro contenedor.

Al tratarse este curso de un curso de introducción a Kubernetes no vamos a poder ver todas las cargas de trabajo, ni la ejecución y despliegue de todo tipo de aplicaciones, por lo que consideramos más razonable no utilizar ejemplos de pods multicontenedor y centrarnos en la comprensión de las características principales de kubernetes mediante ejemplos sencillos, comunes y muy apropiados para ejecutarse en Kubernetes, mediante en uso de pods con un solo contenedor.