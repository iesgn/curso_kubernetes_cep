# Curso Kubernetes

## Título del curso

Introducción a Kubernetes

## Descripción

En los últimos años se ha ido extendiendo el uso de contenedores como
elementos esenciales para el uso de aplicaciones en entornos en
producción, tanto más cuanto más variable sea la demanda, la
frecuencia con la que se actualizan o la necesidad de que funcionen de
forma ininterrumpida.

Gestionar una aplicación sobre contenedores, que pueda actualizarse
rápidamente, que sea escalable o tolerante a fallos, es una tarea
compleja que se realiza mediante un software específico que recibe el
nombre de orquestador de contenedores.

Kubernetes es un software de orquestación de contenedores desarrollado
inicialmente por Google, pero que hoy en día es un proyecto libre
independiente utilizado en gran cantidad de entornos diferentes y que
se ha convertido en muchos casos en la solución preferida para
orquestar aplicaciones basadas en contenedores en entornos en
producción.

En este curso conoceremos las principales características de
Kubernetes y de las aplicaciones más adecuadas para poner en este
entorno y comprobaremos de forma práctica la tolerancia a fallos, la
escalabilidad de una aplicación o la gestión del versionado y los
diferentes enfoques a la hora de hacerlo en entornos en producción,
con o sin interrupciones.

## Destinatarios

El curso va dirigido a docentes que impartan docencia en ciclos
pertenecientes a la familia profesional de informática y que tengan
conocimientos previos sobre el manejo de aplicaciones en
contenedores.

## Requisitos

Este curso es la continuación del curso "Iniciación a los contenedores
Docker para el Desarrollo" por lo que en caso de no haber cursado
dicho curso, es necesario tener conocimiento de la herramienta docker
y comprender las principales características del uso de aplicaciones
en contenedores.

### Objetivos

El principal objetivo de este curso es conocer la herramienta
Kubernetes, el software más extendido actualmente para la puesta en
producción de aplicaciones sobre contenedores, haciendo énfasis en la
arquitectura de la aplicación, la actualización de versiones, la
escalabilidad, etc.

De forma más concreta estos objetivos se pueden enumerar en:

* Conocer las diferencias entre aplicaciones en función de su
  arquitectura
* Conocer Kubernetes y los elementos principales que nos permiten
  gestionar una aplicación en un entorno en producción
* Realizar despliegues de aplicaciones sobre Kubernetes utilizando la
  herramienta kubectl

### Contenidos

1. Introducción a Kubernetes
    * [Implantación de aplicaciones web en contenedores](modulo1/implantacion-aplic-web.md)
    * [Docker](modulo1/docker.md)
    * [Orquestadores de contenedores](modulo1/orquestadores.md)
    * [El proyecto Kubernetes](modulo1/proyecto-kubernetes.md)
    * [Arquitectura básica de Kubernetes](modulo1/arquitectura.md)
1. Instalación de Kubernetes
    * [Alternativas para instalación simple de k8s](modulo2/alternativas.md)
    * [Introducción a la instalación de minikube](modulo2/instalacion-minikube.md)
    * [Instalación de minikube en linux + KVM/VirtualBox](modulo2/instalacion-minikube-linux.md)
    * [Instalación de minikube en Windows + VirtualBox](modulo2/instalacion-minikube-windows.md)
    * [Instalación y configuración de kubectl en linux](modulo2/instalacion-kubectl-linux.md)
    * [Instalación y configuración de kubectl en windows](modulo2/instalacion-kubectl-windows.md)
    * [Despliegues de aplicaciones en Kubernetes](modulo2/despliegues-k8s.md)
        * [Actividad 2.1: Instalación y configuración de minikube y kubectl (OBLIGATORIA)](modulo2/actividad1.md)
1. Contenedores en Kubernetes: Pods
    * [Pod](modulo3/pods.md)
    * [Describiendo un Pod](modulo3/describiendo_pod.md)
	* [Gestionando los Pods](modulo3/gestionando_pod.md)
        * [Actividad 3.1: Trabajando con Pods (OBLIGATORIA)](modulo3/actividad1.md)
        * [Actividad 3.2: Trabajando con un Pod multicontenedor (VOLUNTARIA)](modulo3/actividad2.md)
1. Tolerancia y escalabilidad: ReplicaSets
	* [ReplicaSet](modulo4/replicaset.md)
	* [Describiendo un ReplicaSet](modulo4/describiendo_replicaset.md)
    * [Gestionando los ReplicaSet](modulo4/gestionando_replicaset.md)
        * [Actividad 4.1: Trabajando con ReplicaSet (OBLIGATORIA)](modulo4/actividad1.md)
1. Despliegues
    * [Deployment](modulo5/deployment.md)
    * [Describiendo un Deployment](modulo5/describiendo_deployment.md)
    * [Gestión básica de un Deployment](modulo5/gestionando_deployment.md)
    * [Actualización y desactualización de un Deployment](modulo5/actualizacion_deployment.md)
        * [Actividad 5.1: Trabajando con Deployments (OBLIGATORIA)](modulo5/actividad1.md)
        * [Actividad 5.2: Actualización y desactualización de nuestra aplicación (OBLIGATORIA)](modulo5/actividad2.md)
        * [Actividad 5.3: Despliegue de la aplicación GuestBook (OBLIGATORIA)](modulo5/actividad3.md)
1. Acceso a las aplicaciones
    * [Services. Tipos de Services](modulo6/services.md)
    * [Describiendo Services](modulo6/describiendo_services.md)
    * [Gestionando los Services](modulo6/gestionando_services.md)
    * [Servicio DNS en Kubernetes](modulo6/dns.md)
    * [Ingress Controller](modulo6/ingress.md)
    * [Ejemplo completo: Desplegando y accediendo a la aplicación Temperaturas](modulo6/temperaturas.md)
        * [Actividad 6.1: Acceso de la aplicación GuestBook (OBLIGATORIA)](modulo6/actividad1.md)
        * [Actividad 6.2: Despliegue y acceso de la Aplicación Lets-Chat (VOLUNTARIA)](modulo6/actividad2.md)
1. Despliegues parametrizados
    * [Variables de entorno](modulo7/variables_entorno.md)
	* [ConfigMaps](modulo7/configmaps.md)
	* [Secrets](modulo7/secrets.md)
    * [Ejemplo completo: Despliegue y acceso a Wordpress + MariaDB](modulo7/wordpress.md)
        * [Actividad 7.1: Configurando nuestra aplicación Temperaturas (OBLIGATORIA)](modulo7/actividad1.md)
        * [Actividad 7.2: Despliegue y acceso de la aplicación Nextcloud (VOLUNTARIA)](modulo7/actividad2.md)
1. Almacenamiento en Kubernetes
    * [Consideraciones sobre el almacenamiento](modulo8/consideraciones.md)
    * [Volúmenes en Kubernetes](modulo8/volumenes.md)
    * [Aprovisionamiento de volúmenes](modulo8/aprovisionamiento.md)
    * [Solicitud de volúmenes](modulo8/solicitud.md)
    * [Uso de volúmenes](modulo8/uso.md)
    * [Ejemplo 1: Gestión estática de volúmenes](modulo8/ejemplo1.md)
    * [Ejemplo 2: Gestión dinámica de volúmenes](modulo8/ejemplo2.md)
    * [Ejemplo 3: Wordpress con almacenamiento persistente](modulo8/wordpress.md)
        * [Actividad 8.1: Desplegando un servidor web persistente (OBLIGATORIA)](modulo8/actividad1.md)
        * [Actividad 8.2: Haciendo persistente la aplicación GuestBook (OBLIGATORIA)](modulo8/actividad2.md)
        * [Actividad 8.3: Haciendo persistente la aplicación Nextcloud (VOLUNTARIA)](modulo8/actividad3.md)
1. Otras cargas de trabajo
    * [¿Podemos usar un despliegue para todo?](modulo9/otras_cargas.md)
    * [StatefulSets](modulo9/statefulsets.md)
	* [Ejemplo: Despliegue de un cluster de MySQL](modulo9/ejemplo2.md)
	* [DaemonSets](modulo9/daemonsets.md)
	* [Jobs y CronJobs](modulo9/jobs.md)
        * [Actividad 9.1: Creando un cluster de MySQL (VOLUNTARIA)](modulo9/actividad1.md)
1. Instalación de aplicaciones en Kubernetes con Helm
    * [Despliegue de aplicaciones con Helm](modulo10/helm.md   )
    * [Instalación de Helm](modulo10/instalacion.md)
    * [Gestión de charts y despliegue de aplicaciones](modulo10/ejemplo.md)
        * [Actividad 10.1: Instalación de un CMS con Helm (OBLIGATORIA)](modulo10/actividad1.md)

## Agenda

Con objeto que los participantes en el curso puedan planificar sus
sesiones de trabajo, a modo orientativo se elabora la siguiente
Agenda. En la columna “Actividad” se indicará el nombre de la
misma. Además, si dicha actividad necesita la revisión del tutor o
tutora, se pondrá (T). Bajo la columna "Horas" encontrará el tiempo
aproximado que estimamos le llevará realizar cada actividad. La
columna "Semana" indica la semana del curso en que debería estar
trabajando en la actividad, teniendo en cuenta que se valoran
aproximadamente 5-6 horas por semana.

| MÓDULO | ACTIVIDAD | HORAS | SEMANA |
| :----: | :-------- | :---: | :----: |
| INICIO | 0.1. Guía del curso | 30' | 1ª |
| INICIO | 0.2. Ayuda para conocer el Aula Virtual | 1 h | 1ª |
| INICIO | 0.3. Nos presentamos (T) | 30' | 1ª |
| MÓD 1 | 1.1. **Teoría**. Introducción a kubernetes |  | 1ª |
| MÓD 2 | 2.1. **Teoría**. Instalación de kubernetes |  | 2ª |
| MÓD 2 | 2.2. **Tarea**. Instalación y configuración de minikube y kubectl |  | 2ª |
| MÓD 3 | 3.1. **Teoría**. Contenedores en Kubernetes: Pods  |  | 3ª |
| MÓD 3 | 3.2. **Tarea**. Trabajando con Pods  |  | 3ª |
| MÓD 3 | 3.3. **Tarea**. Trabajando con un Pod multicontenedor (VOLUNTARIA)  | --- | 3ª |
| MÓD 4 | 4.1. **Teoría**. Tolerancia y escalabilidad: ReplicaSets |  | 4ª |
| MÓD 4 | 4.2. **Tarea**. Trabajando con ReplicaSet |  | 4ª |
| MÓD 5 | 5.1. **Teoría**. Despliegues: Deployments |  | 4ª |
| MÓD 5 | 5.2. **Tarea**. Trabajando con Deployments | | 4ª |
| MÓD 5 | 5.3. **Tarea**. Actualización y desactualización de nuestra aplicación  |  | 4ª |
| MÓD 5 | 5.4. **Tarea**. Despliegue de la aplicación GuestBook   |  | 5ª |
| MÓD 6 | 6.1. **Teoría**. Acceso a las aplicaciones: Services  |  | 5ª |
| MÓD 6 | 6.2. **Tarea**. Acceso de la aplicación GuestBook  |  | 5ª |
| MÓD 6 | 6.3. **Tarea**. Despliegue y acceso de la Aplicación Lets-Chat (VOLUNTARIA) | --- | 5ª |
| MÓD 7 | 7.1. **Teoría**. Despliegues parametrizados | | 6ª |
| MÓD 7 | 7.2. **Tarea**. Configurando nuestra aplicación Temperaturas | | 6ª |
| MÓD 7 | 7.3. **Tarea**. Despliegue y acceso de la aplicación Nextcloud (VOLUNTARIA) | --- | 6ª |
| MÓD 8 | 8.1. **Teoría**. Almacenamiento en Kubernetes | | 7ª |
| MÓD 8 | 8.2. **Tarea**. Desplegando un servidor web persistente |  | 7ª |
| MÓD 8 | 8.3. **Tarea**. Haciendo persistente la aplicación GuestBook |  | 7ª |
| MÓD 8 | 8.4. **Tarea**. Haciendo persistente la aplicación Nextcloud (VOLUNTARIA) | --- | 7ª |
| MÓD 9 | 9.1. **Teoría**. Otras cargas de trabajo  |  | 8ª |
| MÓD 9 | 9.2. **Tarea**. Creando un cluster de MySQL (VOLUNTARIA) | --- | 8ª |
| MÓD 10 | 10.1. **Teoría**. Despliegue de aplicaciones con Helm  |  | 8ª |
| MÓD 10 | 10.2. **Tarea**. Instalación de un CMS con Helm |  | 8ª |

El RESTO DE LAS HORAS HASTA LAS 45 HORAS DEL CURSO DEBEN DEDICARSE A
LA LECTURA DE LOS MATERIALES Y AL VISIONADO DE LOS VIDEOTUTORIALES
INCLUIDOS.

## Metodología

El curso está pensado como una secuencia de complejidad creciente, en
la que se irán introduciendo los diferentes elementos de Kubernetes,
hasta llegar a poder gestionar completamente el ciclo de vida de una
aplicación en un entorno en producción.

En la sesión inicial se realizará la introducción del curso en una
sesión de asistencia obligatoria y se explicarán los contenidos del
primer módulo, que es más conceptual.

El resto de módulos contarán con al menos los siguiente materiales:

* Materiales en HTML con explicaciones detalladas y directas sobre las
distintas operaciones que estemos llevando a cabo.
* Una colección de vídeos donde los autores mostrarán las distintas
operaciones funcionando.
* Enlaces a materiales adicionales.

Podemos distinguir las siguientes partes en el curso:

1. Una primera parte más conceptual en la que veremos las
   características de la arquitectura de una aplicación y por qué es
   necesario un software como Kubernetes. También veremos las
   características principales de este software y lo instalaremos en
   una máquina virtual para poder realizar el curso.
1. En la segunda parte del curso, que está formado por la mayor parte
   de módulos, iremos viendo de forma progresiva los diferentes
   elementos de Kubernetes y como nos ayudan a gestionar el despliegue
   y puesta en producción de una aplicación.
1. Finalmente veremos en el último módulo la aplicación Helm, que es
   un sistema de empaquetado para Kubernetes

En todo momento contarás con la ayuda de un tutor o tutora que te
facilitará tu paso por la actividad formativa y se fomentará la
participación a través de los foros para compartir dudas y cualquier
otra cuestión.

## Licencia

Materiales desarrollados por Alberto Molina Coballes y José Domingo
Muñoz Rodríguez para el curso "Introducción a Kubernetes"
organizado por la [Consejería de Educación y Deporte de la Junta de
Andalucía](https://www.juntadeandalucia.es/educacion/portals/web/ced)
y dirigido a profesorado de secundaria de Andalucía.

Toda la documentación es libre y puede compartirse y modificarse bajo
las limitaciones de la licencia Creative Commons
[BY-NC-SA](https://creativecommons.org/licenses/by-nc-sa/4.0/deed.es).
