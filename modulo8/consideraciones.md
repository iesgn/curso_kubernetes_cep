# Consideraciones sobre el almacenamiento

Ya lo hemos comentando en anteriores módulos, pero es importente tener en cuenta que **los pods son efimeros**. Es decir cuando un pod se elimina se pierde toda la infromación que contengan. Evidentemente, cuando creamos un nuevo pod no contendrá ninguna información.

Podemos fijarnos en el [Ejemplo: Despliegue y acceso a WordPress + MariaDB](../modulo7/wordpress.md), y responder las siguientes preguntas:

1. ¿Qué pasa si eliminamos el despliegue de mariadb?, o, ¿se elimina el pod de mariadb y se crea uno nuevo?

    Evidentemente, toda la información guardada en la base de datos se perderá, por lo que al iniciar un nuevo despliegue, no tendremos información guardada, habremos perdido todo el contenedio de nuestra aplicación y empezaría de nuevo el proceso de instalación.

2. ¿Qué pasa si escalamos el despliegue de la base de datos y tenemos dos pods ofreciendo la base de datos?

    En este caso el pod más antiguo tendría la información de la base de datos, pero el nuevo pod creado al escalar el despliegue no tendría ninguna información. Como al acceder a l servicio de la base de datos se hace balanceo de carga, en unas ocaciones accederiamos al pod antiguo, y todo funcionaría correctamente, pero cuando accedieramos al pod nuevo, al no tener información, nos mostraría la pantalla de instalación de la aplicación. En definitiva, tendríamos dos bases de datos distintas a las que accederáimos indistitamente.

3. Si escribimos un post en el wordpress y subimos una imagen, ¿qué pasa con esta información en el pod?

    Esta calro, que cuando escribimos un post, esa información se guarda en la base de datos. Pero la imágen que hemos subido al post se guardaría en un directorio del servidor web (del pod de wordpress). Tendríamos los mismos problemas que con la base de datos, si eliminamos este pod se perderá todo el contendio estático de nuestro WordPress.

4. ¿Qué pasa si escalamos el despliegue de wordpress a dos pods?

    Pues la respuesta es similar a la anterior. En este caso, el pod antigüo tendría almacenada el contendio estáticos (las imágenes), pero el nuevo no tendría información. Como al acceder a la aplicación se balancea la carga, se mostraría la imagen según al pod que estuviéramos accediendo.


Por lo tanto es necesario usar un mecanismo que nos permita guardar la información con la que trabajan los pods para que no se pierda en caso de que el pod se elimne. Al sistema de almacenamiento que nos ofrece kubernetes lo llamamos **volumenes**. Con el uso de volúmenes vamos a conseguir varias cosas:

1. Si un pod guarda su información en un volumen, está no se perderá. Por lo que podemos eliminar el pod sin ningún problema y cuando volavamos a crearlo mantendrá la misma información.
2. Si usamos volumenes, y tenemos varios pods que están ofreciendo un servicio, estos pods tendrán la información compartida y por tanto todos podrán leer y escribir la misma información. 
3. También podemos usar los volúmenes dentro de un pod, para que los contenedores que forman parte de él puedan compartir información.

Por último, indicar que vamos a tener a nuestra disposición distintos tipos de volúmenes que podemos usar. Hay que tener en cuenta que si nuestro cluster tienes varios nodos y que los pods de una aplicación se reparten por estos nodos, necesitamos sitemas de almacenamiento que nos posibiliten compartir la información entre los nodos del cluster. Como en este curso estamos usando **minikube**, nuestro cluster tiene un solo nodo, por lo que vamos a usar un tipo de almacenmaiento que permita compartir la información dentro de este nodo (por ejemplo un directorio en el sistema de archivo del nodo), por lo tanto este tema lo vamos a simplificar al no tener la posibilidad de tener un cluster con varios nodos.