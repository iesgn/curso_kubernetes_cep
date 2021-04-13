# Curso Kubernetes

## Título del curso

Introducción a Kubernetes

## Descripción

En los últimos años se ha ido extendiendo el uso de contendores como
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
kubernetes y de las aplicaciones más adecuadas para poner en este
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
kubernetes, el software más extendido actualmente para la puesta en
producción de aplicaciones sobre contenedores, haciendo énfasis en la
arquitectura de la aplicación, la actualización de versiones, la
escalabilidad, etc.

De forma más concreta estos objetivos se pueden enumerar en:

* Conocer las diferencias entre aplicaciones en función de su
  arquitectura
* Conocer kubernetes y los elementos principales que nos permiten
  gestionar una aplicación en un entorno en producción
* Realizar despliegues de aplicaciones sobre kubernetes utilizando la
  herramienta kubectl

### Contenidos

1. Introducción a Kubernetes
    * Implantación de aplicaciones web en contenedores
    * Limitaciones de Docker
    * Orquestadores de contenedores
    * El proyecto kubernetes
    * Arquitectura básica de kubernetes
1. Instalación de Kubernetes
    * [Alternativas para instalación simple de k8s](modulo2/alternativas.md)
    * Instalación de minikube
    * Instalación y configuración de kubectl
    * Despliegues de aplicaciones en Kubernetes
1. Contenedores en kubernetes: Pods
    * [Pod](modulo3/pods.md)
    * [Describiendo un pod](modulo3/describiendo_pod.md)
	* [Gestionando los pods](modulo3/gestionando_pod.md)
        * [Actividad 3.1: Trabajando con pods (OBLIGATORIA)](modulo3/actividad1.md)
        * [Actividad 3.2: Trabajando con un pod multicontenedor (VOLUNTARIA)](modulo3/actividad2.md)
1. Tolerancia y escalabilidad: ReplicaSets
	* [ReplicaSet](modulo4/replicaset.md)
	* [Describiendo un ReplicaSet](modulo4/describiendo_replicaset.md)
    * [Gestionando los ReplicaSet](modulo4/gestionando_replicaset.md)
        * [Actividad 4.1: Trabajando con ReplicaSet (OBLIGATORIA)](modulo4/actividad1.md)
1. Despliegues
    * [Deployment](modulo5/deployment.md)
    * [Describiendo un Deployment](modulo5/describiendo_deployment.md)
    * [Gestión básica de Deployment](modulo5/gestionando_deployment.md)
    * [Actualización y rollout de Deployment](modulo5/actualizacion_deployment.md)
        * [Actividad 5.1: Trabajando con Deployments (OBLIGATORIA)](modulo5/actividad1.md)
        * [Actividad 5.2: Actualización y rollout de nuestra aplicación (OBLIGATORIA)](modulo5/actividad2.md)
        * [Actividad 5.3: Despliegue de la aplicación GuestBook (VOLUNTARIA)](modulo5/actividad3.md)
1. Acceso a las aplicaciones
    * [Services. Tipos de servicios](modulo6/services.md)
    * [Describiendo Services](modulo6/describiendo_services.md)
    * [Gestionando los Services](modulo6/gestionando_services.md)
    * [Servicio DNS en Kubernetes](modulo6/dns.md)
    * [Ingress Controller](modulo6/ingress.md)
    * [Ejemplo completo: Desplegando y accediendo a la aplicación Temperaturas](modulo6/temperaturas.md)
        * [Actividad 6.1: Despliegue y acceso de la aplicación GuestBook (OBLIGATORIA)](modulo6/actividad1.md)
        * [Actividad 6.2: Despliegue y acceso de la Aplicación Lets-Chat (VOLUNTARIA)](modulo6/actividad2.md)
1. Despliegues parametrizados
    * [Variables de entorno](modulo7/variables_entorno.md)
	* [ConfigMaps](modulo7/configmaps.md)
	* [Secrets](modulo7/secrets.md)
    * [Ejemplo completo: Despliegue y acceso a WordPress + MariaDB](modulo7/wordpress.md)
        * [Actividad 7.1: Configurando nuestra aplicación Temperaturas (OBLIGATORIA)](modulo7/actividad1.md)
        * [Actividad 7.2: Despliegue y acceso de la aplicación Nextcloud (VOLUNTARIA)](modulo7/actividad2.md)
1. Almacenamiento en Kubernetes
    * [Consideraciones sobre el almacenamiento](modulo8/consideraciones.md)
    * [Volúmenes en Kubernetes](modulo8/volumenes.md)
    * Aprovisionamiento de volúmenes
    
        * Actividad 8.1: Haciendo persistente nuestra aplicación Temperaturas (OBLIGATORIA)
        * Actividad 8.2: Haciendo persistente la aplicación Nextcloud (VOLUNTARIA)
1. Otras cargas de trabajo
    * StatefulSets
	* DaemonSets
	* Jobs y cronjobs
        * Actividad 9.1: Creando un cluster de mysql (VOLUNTARIA)
1. Instalación de aplicaciones en Kubernetes con Helm
    * Instalación de helm
    * Búsquedas de charts
        * Actividad 10.1: Instalación de un CMS con Helm (OBLIGATORIA)

## Agenda

Pendiente de hacer cuando estén definidas las actividades

## Metodología

El curso está pensado como una secuencia de complejidad creciente, en
la que se irán introduciendo los diferentes elementos de kubernetes,
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
   necesario un software como kubernetes. También veremos las
   características principales de este software y lo instalaremos en
   una máquina virtual para poder realizar el curso.
1. En la segunda parte del curso, que está formado por la mayor parte
   de módulos, iremos viendo de forma progresiva los diferentes
   elementos de kubernetes y como nos ayudan a gestionar el despliegue
   y puesta en producción de una aplicación.
1. Finalmente veremos en el último módulo la aplicacion Helm, que es
   un sistema de empaquetado para kubernetes
   
En todo momento contarás con la ayuda de un tutor o tutora que te
facilitará tu paso por la actividad formativa y se fomentará la
participación a través de los foros para compartir dudas y cualquier
otra cuestión.
