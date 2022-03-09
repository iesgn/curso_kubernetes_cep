# Orquestadores de contenedores

Tan pronto como se fue extendiendo el uso de docker para el desarrollo
de aplicaciones web, surgió la necesidad de desarrollar software de
orquestadores de contenedores para gestionar de forma coordinada
múltiples nodos en los que se estuvieran ejecutando contenedores y
para proporcionar funcionalidad no ofrecida por docker engine y
que es necesaria en la puesta en producción de la aplicación.

## Docker swarm

Lógicamente la propia empresa Docker Inc. comenzó pronto el desarrollo
de su orquestador que extendía la funcionalidad de docker y creó el
proyecto [Swarm](https://docs.docker.com/engine/swarm/) (enjambre),
aunque en las últimas versiones de docker-engine, ya se incluye swarm
como un componente y no es necesario instalarlo de forma separada.

Actualmente se considera que docker swarm es una solución de
orquestación de contenedores sencilla y que es adecuada para
determinados entornos no muy exigentes, pero no puede
competir con Kubernetes en grandes entornos expuestos a Internet. Su
desarrollo continúa, pero ya no como un competidor de Kubernetes, de
hecho la propia Docker Inc. publicita
[Kubernetes](https://www.docker.com/products/kubernetes) como un
producto sobre el que ofrecen servicios.

## Apache Mesos

[Apache Mesos](http://mesos.apache.org/) es un proyecto de software
libre que proporciona un orquestador de contenedores. Este proyecto
actualmente está bajo el paraguas de la Apache Software Foundation,
pero originalmente fue desarrollado por la empresa Mesosphere, hoy
renombrada a [D2iQ](https://d2iq.com/). Mesos ha ido derivando de un
competidor de Kubernetes hacia un software que proporcione soluciones
más específicas, como [DC/OS](https://dcos.io/).

## Hashicorp Nomad

[Nomad](https://www.nomadproject.io/) es un proyecto de la prestigiosa
empresa Hashicorp (Vagrant, Terraform, etc.) y su idea es ser un
software de orquestación más simple, que se centre en la gestión del
cluster de nodos y la ejecución de contenedores en ellos, pero sin
proporcionar todo el resto de funcionalidad adicional, por lo que
Nomad se utiliza junto a otro software cuando se pone en producción.

## Vídeo

[https://www.youtube.com/watch?v=XYh8PSQY5gs](https://www.youtube.com/watch?v=XYh8PSQY5gs)
