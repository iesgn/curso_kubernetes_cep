# Docker

Docker es una empresa ([Docker Inc.](https://www.docker.com/)) que
desarrolla un software con el mismo nombre, de forma más concreta el software denominado ([docker
engine](https://www.docker.com/products/container-runtime)), que ha
supuesto una revolución en el desarrollo de software, muy ligado al
uso de contenedores de aplicaciones, a las aplicaciones web y al
desarrollo ágil.

Docker permite gestionar contenedores a alto nivel, proporcionando
todas las capas y funcionalidad adicional y, lo más importante de todo,
es que proporciona un nuevo paradigma en la forma de distribuir las
aplicaciones, ya que se crean imágenes en contenedores que se
distribuyen, de manera que el contenedor que se ha desarrollado es
idéntico al que se utiliza en producción y deja de instalarse la
aplicación de forma tradicional.

## Componentes de docker

Docker engine tiene los componentes que a *grosso modo* se presentan a
continuación:

<img src="https://github.com/iesgn/curso_kubernetes_cep/raw/main/modulo1/img/docker.png" alt="docker" />

En la imagen se han destacado los componentes que son relevantes desde
el punto de vista de este curso, ya que como veremos más adelante,
docker podría ser un componente esencial de Kubernetes, pero realmente
no lo es completo, solo containerd y los elementos que éste
proporciona lo son, ya que k8s utiliza su propia API, su propia línea
de comandos y gestiona el almacenamiento y las redes de forma
independiente a docker.

## Evolución del proyecto docker

Docker tuvo un enorme éxito y una gran repercusión, pero la empresa
que lo desarrolla siempre se ha movido en el dilema de cómo sacar
rendimiento económico a su software, que al ser desarrollado bajo
licencia libre, no proporciona beneficio como tal. Este dilema se ha
tratado de resolver con modificaciones en la licencia o con doble
licenciamiento (docker CE y docker EE en estos momentos), pero esto a
su vez ha propiciado que otras empresas desarrollasen alternativas a
docker para no depender en el futuro de una empresa sin un modelo de
negocio claro y ante posibles modificaciones de la licencia libre de
docker.

Los cambios más significativos que han ocurrido en docker se enumeran
a continuación:

* [Moby](https://github.com/moby/moby) Docker engine se desarrolla
  ahora como proyecto de software libre independiente de Docker Inc. denominándose Moby. De este proyecto se surten las distribuciones de
  linux para desarrollar los paquetes docker.io

* [Docker Engine](https://www.docker.com/products/container-runtime)
  Versión desarrollada por Docker Inc.

* [runC](https://github.com/opencontainers/runc) Componente que
  ejecuta los contenedores a bajo nivel. Actualmente desarrollado por
  OCI

* [containerd](https://github.com/containerd/containerd) Componente
  que ejecuta los contenedores e interactúa con las
  imágenes. Actualmente desarrollado por la CNCF.

## Limitaciones de docker (docker engine)

Docker (docker engine) gestiona completamente la ejecución de un
contenedor en un determinado nodo a partir de una imagen, pero no
proporciona toda la funcionalidad que necesitamos para ejecutar
aplicaciones en entornos en producción. 

Existen diferentes preguntas
que nos podemos hacer acerca de esto :

* ¿Qué hacemos con los cambios entre versiones?
* ¿Cómo hacemos los cambios en producción?
* ¿Cómo se balancea la carga entre múltiples contenedores iguales?
* ¿Cómo se conectan contenedores que se ejecuten en diferentes
demonios de docker?
* ¿Se puede hacer una actualización de una aplicación sin
interrupción?
* ¿Se puede variar a demanda el número de réplicas de un determinado
contenedor?
* ¿Es posible mover la carga entre diferentes nodos?

Las respuestas a estas preguntas no pueden venir de docker engine, ya
que no es un software desarrollado para eso, tiene que venir de algún software
que pueda utilizar docker o parte de él y que sea capaz de comunicar
múltiples nodos para proporcionar de forma coordinada estas
funcionalidades. Ese software se conoce de forma genérica como
**orquestador de contenedores**.

## Vídeo

[https://www.youtube.com/watch?v=UdPsknw30OE](https://www.youtube.com/watch?v=UdPsknw30OE)
