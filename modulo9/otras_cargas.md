# ¿Podemos usar un despliegue para todo?

Hasta ahora hemos visto con bastante detalle el uso de los despliegues
en Kubernetes. Los despliegues son una herramienta enormemente potente
ya que nos permite adecuar el número de pods a la demanda y garantiza
el funcionamiento continuo, tanto en el caso de que haya algún nodo
con problemas, como en el caso de actualizaciones que se pueden
realizar de forma continua. Sin embargo, no es posible utilizar
despliegues en todos los casos, hay determinadas situaciones en las
que hay cargas de trabajo (*workloads*) que no se ajustan
adecuadamente a un despliegue de Kubernetes, por lo que se han
desarrollado otros objetos para esas situaciones diferentes. Sí es
conveniente remarcar, que siempre que sea posible es mejor definir una
carga de trabajo como un despliegue en Kubernetes y limitar el uso de
las otras cargas de trabajo que vamos a ver a continuación para casos
específicos. Luego la respuesta a la pregunta con la que empezamos
este módulo es no, no podemos usar un despliegue para todo, pero sí
debemos usarlo prioritariamente siempre que sea posible.

## Aplicaciones con estado o sin estado
