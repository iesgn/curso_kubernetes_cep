# Consideraciones sobre el almacenamiento

Ya lo hemos comentando en anteriores módulos, pero es importante tener en cuenta que **los Pods son efímeros**, es decir, cuando un Pod se elimina se pierde toda la información que tenía. Evidentemente, cuando creamos un nuevo Pod no contendrá ninguna información adicional a la propia aplicación.

Podemos fijarnos en el [Ejemplo: Despliegue y acceso a Wordpress + MariaDB](../modulo7/wordpress.md), y responder las siguientes preguntas:

1. ¿Qué pasa si eliminamos el despliegue de mariadb?, o, ¿se elimina el Pod de mariadb y se crea uno nuevo?

    Evidentemente, toda la información guardada en la base de datos se perderá, por lo que al iniciar un nuevo despliegue, no tendremos información guardada, habremos perdido todo el contenido de nuestra aplicación y empezaría de nuevo el proceso de instalación.

2. ¿Qué pasa si escalamos el despliegue de la base de datos y tenemos dos Pods ofreciendo la base de datos?

    En este caso el Pod más antiguo tendría la información de la base de datos, pero el nuevo Pod creado al escalar el despliegue no tendría ninguna información. Como al acceder al Service de la base de datos se hace balanceo de carga, en unas ocasiones accederíamos al Pod antiguo, y todo funcionaría correctamente, pero cuando accederíamos al Pod nuevo, al no tener información, nos mostraría la pantalla de instalación de la aplicación. En definitiva, tendríamos dos bases de datos distintas a las que accederíamos indistintamente.

3. Si escribimos un post en el Wordpress y subimos una imagen, ¿qué pasa con esta información en el Pod?

    Está claro que cuando escribimos un post esa información se guarda en la base de datos. Pero la imagen que hemos subido al post se guardaría en un directorio del servidor web (del Pod de Wordpress). Tendríamos los mismos problemas que con la base de datos, si eliminamos este Pod se perderá todo el contenido estático de nuestro Wordpress.

4. ¿Qué pasa si escalamos el despliegue de Wordpress a dos Pods?

    Pues la respuesta es similar a la anterior. En este caso, el Pod antiguo tendría almacenada el contenido estático (la imagen), pero el nuevo no tendría esa información. Como al acceder a la aplicación se balancea la carga, se mostraría la imagen diferente en función del Pod que estuviéramos accediendo.


Por lo tanto, es necesario usar un mecanismo que nos permita guardar la información con la que trabajan los Pods para que no se pierda en caso de que el Pod se elimine. Al sistema de almacenamiento persistente que nos ofrece Kubernetes lo llamamos **volúmenes**. Con el uso de dichos volúmenes vamos a conseguir varias cosas:

1. Si un Pod guarda su información en un volumen, está no se perderá. Por lo que podemos eliminar el Pod sin ningún problema y cuando volvamos a crearlo mantendrá la misma información. En definitiva, los volúmenes proporcionan almacenamiento adicional o secundario al disco que define la imagen.
2. Si usamos volúmenes, y tenemos varios Pods que están ofreciendo un servicio, estos Pods tendrán la información compartida y por tanto todos podrán leer y escribir la misma información.
3. También podemos usar los volúmenes dentro de un Pod, para que los contenedores que forman parte de él puedan compartir información.

Por último, indicar que vamos a tener a nuestra disposición distintos tipos de volúmenes para usar. Hay que tener en cuenta que si nuestro cluster tiene varios nodos y los Pods de una aplicación se reparten por estos nodos, necesitamos sistemas de almacenamiento que nos posibiliten compartir la información entre los nodos del cluster. Como en este curso estamos usando **minikube**, nuestro cluster tiene un solo nodo, por lo que vamos a usar un tipo de almacenamiento que permita compartir la información dentro de este nodo (por ejemplo un directorio en el sistema de archivos del nodo), por lo tanto este tema lo vamos a simplificar al no tener la posibilidad de tener un cluster con varios nodos.
