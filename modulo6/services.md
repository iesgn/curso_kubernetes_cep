# Services. Tipos de servicios

Los servicios ([services](https://kubernetes.io/docs/concepts/services-networking/service/)) nos permiten acceder a nuestra aplicaciones.

* Un servicio es una abstracción que **nos permite acceder a un conjunto de pods** (que se han creado a partir de un Deployment) que implementan una aplicación (Por ejemplo: acceder a un servidor web, a una servidor de base de datos, a un microservicio que forma parte de una aplicación,...).
* A los Pods se le asignan una IP a la que no se puede acceder directamente, por lo tanto necesitamos un service que nos ofrece **una dirección virtual (CLUSTER-IP) y un nombre** que identifica al conjunto de pods que representa, al cual nos podemos conectar.
* La conexión al servicio se puede realizar **desde otros pods o desde el exterior** (mediante la generación aleatoria de un puerto). Por ejemplo, si tenemos una aplicación formada por dos servicios: servidor web y servidor de base de datos, querremos acceder desde el exterior al servidor web, y acceder al servidor de base de datos desde el servidor web. de principio no será necesario acceder al servidor de base de datos desde el exterior.
* Si el despliegue que hemos creado tiene más de un pod asociado, el servicio que representa el acceso a esta aplicación **balanceará la carga** entre los Pods con una política Round Robin.
* En el cluster existirá un componente que nos ofrece un **servicio DNS**. Cada vez que creamos un services se actualizará el DNS para resolver el nombre que hemos asignado al servicio con la IP virtual (CLUSTER-IP) que se le ha asignado.
 
