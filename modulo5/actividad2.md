# ACTIVIDAD Nº 2

## TÍTULO DE LA ACTIVIDAD: Actualización y rollout de nuestra aplicación

## TEXTO DE LA ACTIVIDAD

El equipo de desarrollo ha creado una primera versión preliminar de una aplicación web y ha creado una imagen de contenedor con el siguiente nombre: `iesgn/test_web:version1`.

Vamos a desplegar esta primera versión de la aplicación. para ello:

1. Crea un fichero yaml (puedes usar el de la actividad anterior) para desplegar la imagen: `iesgn/test_web:version1`.
2. Crea el Deployment, recuerda la opción que nos permite registrar los comando que vamos a ejecutar a continuación para ir actualizando el despliegue.
3. Crea un una redirección utilizando el `port-forward` para acceder a la aplicación, sabiendo que la aplicación ofrece el servicio en el puerto 80, y accede a la aplicación con un navegador web.

Nuestro equipo de desarrollo ha seguido trabajando y ya tiene lista la versión 2 de nuestra aplicación, han creado una imagen que se llama: `iesgn/test_web:version2`, vamos a actualizar nuestro despliegue con la nueva versión, para ello:

1. Realiza la actualización del despliegue utilizando la nueva imagen.
2. Comprueba que los recursos que se han creado: Deployment, ReplicaSet y Pods.
3. Visualiza el historial de actualizaciones.
4. Crea un una redirección utilizando el `port-forward` para acceder a la aplicación, sabiendo que la aplicación ofrece el servicio en el puerto 80, y accede a la aplicación con un navegador web.

Finalmente después de un trabajo muy duro, el equipo de desarrollo ha creado la imagen `iesgn/test_web:version3` con la última versión de nuestra aplicación, la vamos a poner en producción, para llo:

1. Realiza la actualización del despliegue utilizando la nueva imagen.
2. Comprueba que los recursos que se han creado: Deployment, ReplicaSet y Pods.
3. Visualiza el historial de actualizaciones.
4. Crea un una redirección utilizando el `port-forward` para acceder a la aplicación, sabiendo que la aplicación ofrece el servicio en el puerto 80, y accede a la aplicación con un navegador web.

Vaya!!!, parece que esta versión tiene un fallo, y no se ve de forma adecuada la hoja de estilo, tenemos que volver a la versión anterior:

1. Ejecuta la instrucción que nos permite hacer un rollout de nuestro despliegue.
2. Comprueba que los recursos que se han creado: Deployment, ReplicaSet y Pods.
3. Visualiza el historial de actualizaciones.
4. Crea un una redirección utilizando el `port-forward` para acceder a la aplicación, sabiendo que la aplicación ofrece el servicio en el puerto 80, y accede a la aplicación con un navegador web.

Para superar la actividad deberás entregar en un fichero comprimido los siguientes pantallazos:

1. Pantallazo donde se vea el acceso desde un navegador web a la version 1 de la aplicación aplicación.
2. Pantallazo donde se vea el acceso desde un navegador web a la version 2 de la aplicación aplicación.
3. Pantallazo donde se visualice el historial de actualización del despliegue después de actualizar a la versión 2.
4. Pantallazo donde se vea el acceso desde un navegador web a la version 3 de la aplicación aplicación (No se visualiza bien la hoja de estilos!!!).
5. Pantallazo donde se visualice el historial de actualización después de realizar el rollout del despliegue.
6. Pantallazo donde se vea el acceso desde un navegador web a la version de la aplicación que queda después de hacer el rollout.

## RECURSOS

* Conexión a internet

## ¿ES OBLIGATORIO HACER ESTA ACTIVIDAD PARA SUPERAR EL CURSO? (S/N)

Si

## ¿ES UNA ACTIVIDAD INDIVIDUAL O DE GRUPO?

Individual

## ¿ES UNA ACTIVIDAD CALIFICABLE?

Si

### ¿Tiene que ser calificada por el tutor/a? (S/N) 

Si

### ¿Es de calificación automática?

No

### ¿Es calificada por el resto de compañeros/as del curso? (S/N)

No

## EVALUACIÓN

* Se entregan los documentos; contienen lo solicitado y los contenidos son originales.

## ¿ES NECESARIO TENER TERMINADA ALGUNA ACTIVIDAD O RECURSO ANTERIOR? Indique cuáles.

No

## TIEMPO ESTIMADO PARA REALIZAR LA ACTIVIDAD

1 hora
