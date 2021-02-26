# Deployment

El [Deployment](https://kubernetes.io/docs/concepts/workloads/controllers/deployment/) es la unidad de más alto nivel que podemos gestionar en Kubernetes.

En los módulos anteriores hemos estudiado los Pods y los ReplicaSet, sin embargo cuando queramos desplegar una aplicación en kubernetes vamos a crear un recurso *Deployment*. ¿Qué ocurre cuando creamos un nuevo recurso *Deployment*?

* La creación de un *Deployment* conlleva la creación de un *ReplicaSet* que controlará un conjunto de pods creado a partir de la versión de la imagen que se ha indicado. 
* Si modificamos la versión de la imagen (es decir, si hemos desarrollado una nueva versión de la aplicación y hemos creado una nueva imagen con la nueva versión) en el *Deployment* se creará un nuevo *ReplicaSet* que controlará un nuevo conjunto de pods creado a a partir de la nueva versión de la imagen (habremos desplegado una nueva versión de la aplicación).
* Por lo tanto podemos decir que un *Deployment* va guardando un historial con los *ReplicaSet* que se van creando al ir cambiado la versión de la imagen. El *ReplicaSet* que esté activo ente momento será el responsable de crear los pods con la versión actual de la aplicación.
* Si tenemos un historial de *ReplicaSet* según las distintas versiones de la imagen que estamos utilizando, podemos de una manera sencilla volver a una versión anterior de la aplicación (Rollback).

Por la manera de trabajar de un *Deployment*, podemos indicar las funciones que nos aporta:

* Control de réplicas
* Escabilidad de pods
* Actualizaciones continuas
* Despliegues automáticos
* Rollback a versiones anteriores