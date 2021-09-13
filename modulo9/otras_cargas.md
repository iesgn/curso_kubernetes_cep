# ¿Podemos usar un despliegue para todo?

Hasta ahora hemos visto con bastante detalle el uso de los despliegues (Deployments)
en Kubernetes. Los despliegues son una herramienta enormemente potente
ya que nos permiten adecuar el número de pods a la demanda y garantizan
el funcionamiento continuo, tanto en el caso de que haya algún nodo
con problemas, como en el caso de actualizaciones que se pueden
realizar de forma continua. Sin embargo, no es posible utilizar
despliegues en todos los casos, hay determinadas situaciones en las
que hay cargas de trabajo (*workloads*) que no se ajustan
adecuadamente a un despliegue de Kubernetes, por lo que se han
desarrollado otros objetos para esas situaciones diferentes. 

Sí es
conveniente remarcar, que siempre que sea posible es mejor definir una
carga de trabajo como un despliegue en Kubernetes y limitar el uso de
las otras cargas de trabajo que vamos a ver a continuación para casos
específicos. Luego la respuesta a la pregunta con la que empezamos
este módulo es no, no podemos usar un despliegue para todo, pero sí
debemos usarlo prioritariamente siempre que sea posible.

## Aplicaciones con estado o sin estado

Una característica de una aplicación que es muy importante para
Kubernetes es si se trata de una aplicación con estado (*stateful*) o
sin estado (*stateless*). Una aplicación sin estado es aquella en la
que las peticiones son totalmente independientes unas de otras y no
necesita ninguna referencia de una petición anterior. Un ejemplo de
una aplicación sin estado sería un servicio DNS, en el que cada vez
que se realiza una petición es totalmente independiente de las
anteriores o posteriores que se hagan. Las aplicaciones sin estado son
perfectas para desplegarse el Kubernetes, ya que se ajustan
perfectamente a un Deployment y se pueden escalar y balancear sin
problemas, ya que cada pod responderá a las peticiones que reciba de
forma independiente al resto.

Por contra, las aplicaciones con estado son aquellas en las que una
petición puede verse afectada por el resultado de las anteriores y a
su vez puede afectar a las posteriores (por eso se dice que tiene
estado). Una base de datos sería el paradigma de una aplicación con
estado, puesto que cada modificación que hagamos a la base de datos 
puede afectar a las consultas posteriores. Una aplicación con estado
no se ajusta bien a un Deployment de Kubernetes, ya que de forma
general, un cluster de pods independientes no puede tener en cuenta el
estado de la aplicación correctamente.

Esto enlaza con el modelo de desarrollo de las aplicaciones, ya que si
pensamos en la mayoría de las aplicaciones que utilizamos hoy en día,
se trata de aplicaciones con estado, lo que inicialmente podría
limitar su uso en Kubernetes. Sin embargo, si descomponemos estas
aplicaciones en muchos y pequeños servicios que se intercomuniquen
entre sí, bastantes de ellos se podrán gestionar como aplicaciones sin
estado, mientras que otros tendrán que ser aplicaciones con
estado. Éste es uno de los enfoques más utilizados hoy en día para
desplegar aplicaciones en Kubernetes, hacer que la aplicación se
ajuste al modelo de microservicios, para utilizar Deployments en todos
los microservicios sin estado que se pueda y utilizar otras cargas de
trabajo para el resto de componentes. En esta unidad veremos una
pequeña introducción a estas otras cargas de trabajo.
