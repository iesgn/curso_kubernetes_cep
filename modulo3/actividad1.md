# ACTIVIDAD Nº 1

## TÍTULO DE LA ACTIVIDAD: Trabajando con Pods

## TEXTO DE LA ACTIVIDAD

Vamos a crear nuestro primer Pod, y para ellos vamos a desplegar una
imagen que nos ofrece un servidor web con una página estática. Para
ello realiza los siguientes pasos:

1. Crea un fichero yaml con la descripción del recurso Pod, teniendo en cuenta los siguientes aspectos:
    * Indica nombres distintos para el Pod y para el contenedor.
    * La imagen que debes desplegar es `iesgn/test_web:latest`.
    * Indica una etiqueta en la descripción del Pod.
2. Crea el Pod.
3. Comprueba que el Pod se ha creado y está corriendo.
4. Obtén información detallada del Pod creado.
5. Accede de forma interactiva al Pod y comprueba los ficheros que están en el DocumentRoot (`usr/local/apache2/htdocs/`).
6. Crea una redirección con `kubectl port-forward` utilizando el puerto de localhost 8888 y sabiendo que el Pod ofrece el servicio en el puerto 80. Accede a la aplicación desde un navegador.
7. Muestra los logs del Pod y comprueba que se visualizan los logs de los accesos que hemos realizado en el punto anterior.
8. Elimina el Pod, y comprueba que ha sido eliminado.

Para superar la actividad deberás entregar en un fichero comprimido los siguientes pantallazos:

1. Pantallazo del fichero yaml que has creado con la definición del Pod (**pantallazo1.jpg**).
2. Pantallazo donde se comprueba que el Pod ha sido creado (**pantallazo2.jpg**).
3. Pantallazo donde se ve la información detallada del Pod (**pantallazo3.jpg**).
4. Pantallazo donde se ve el fichero `index.html` del DocumentRoot (**pantallazo4.jpg**).
5. Pantallazo del navegador accediendo a la aplicación con el `port-forward` (**pantallazo5.jpg**).
6. Pantallazo donde se ve los logs de acceso del Pod (**pantallazo6.jpg**).

## RECURSOS

* Conexión a Internet

## ¿ES OBLIGATORIO HACER ESTA ACTIVIDAD PARA SUPERAR EL CURSO? (S/N)

Sí

## ¿ES UNA ACTIVIDAD INDIVIDUAL O DE GRUPO?

Individual

## ¿ES UNA ACTIVIDAD CALIFICABLE?

Sí

### ¿Tiene que ser calificada por el tutor/a? (S/N)

Sí

### ¿Es de calificación automática?

No

### ¿Es calificada por el resto de compañeros/as del curso? (S/N)

No

## EVALUACIÓN

* Se entregan los documentos, contienen lo solicitado y los contenidos son originales.

## ¿ES NECESARIO TENER TERMINADA ALGUNA ACTIVIDAD O RECURSO ANTERIOR? Indique cuáles.

No

## TIEMPO ESTIMADO PARA REALIZAR LA ACTIVIDAD

1 hora
