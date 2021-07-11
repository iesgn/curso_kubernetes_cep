# ACTIVIDAD Nº 1

## TÍTULO DE LA ACTIVIDAD: Configurando nuestra aplicación Temperaturas 

## TEXTO DE LA ACTIVIDAD

En un ejemplo del módulo anterior: [Ejemplo completo: Desplegando y accediendo a la aplicación Temperaturas](../modulo6/temperaturas.md) habíamos desplegado una aplicación formada por dos microservicios que nos permitía visualizar las temperaturas de municipios.

Recordamos que el componente `frontend` hace peticiones al componente `backend` utilizando el nombre `temperaturas-backend`, que es el nombre que asignamos al Service ClusterIP para el acceso al `backend`.

Vamos a cambiar la configuración de la aplicación para indicar otro nombre.

Podemos configurar el nombre del servidor `backend` al que vamos acceder desde el `frontend` modificando la variable de entorno **TEMP_SERVER** a la hora de crear el despliegue del `frontend`.

Por defecto el valor de esa variable es:

```yaml
TEMP_SERVER temperaturas-backend:5000
```

Vamos a modificar esta variable en el despliegue del `frontend` y cambiaremos el nombre del Service del `backend` para que coincidan, para ello realiza los siguientes pasos:

1. Crea un recurso `ConfigMap` con un dato que tenga como clave `SERVIDOR_TEMPERATURAS` y como contenido `servidor-temperaturas:5000`.
2. Modifica el fichero de despliegue del `frontend`: [`frontend-deployment.yaml`](../modulo6/files/temperaturas/frontend-deployment.yaml) para añadir la modificación de la variable `TEMP_SERVER` con el valor que hemos guardado en el `ConfigMap`.
3. Realiza el despliegue y crea el Service para acceder al `frontend`.
4. Despliega el microservicio `backend`.
5. Modifica el fichero [`backend-srv.yaml`](../modulo6/files/temperaturas/backend-srv.yaml) para cambiar el nombre del Service por `servidor-temperaturas` y crea el Service.
6. Accede a la aplicación usando el puerto asignado al Service NodePort del `frontend` o creando el recurso `Ingress`.

Para superar la actividad deberás entregar en un fichero comprimido los siguientes pantallazos:

1. Pantallazo donde se vea la definición del recurso `ConfigMap` (**pantallazo1.jpg**).
2. Pantallazo donde se vea la modificación del fichero `frontend-deployment.yaml` (**pantallazo2.jpg**).
3. Pantallazo donde se vea la modificación del fichero `backend-srv.yaml` (**pantallazo3.jpg**).
4. Pantallazo donde se compruebe que la aplicación está funcionando (**pantallazo4.jpg**).

## RECURSOS

* Conexión a internet
* Los ficheros del [Ejemplo completo: Desplegando y accediendo a la aplicación Temperaturas](../modulo6/temperaturas.md) del módulo 6.

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

* Se entregan los documentos, contienen lo solicitado y los contenidos son originales.

## ¿ES NECESARIO TENER TERMINADA ALGUNA ACTIVIDAD O RECURSO ANTERIOR? Indique cuáles.

No

## TIEMPO ESTIMADO PARA REALIZAR LA ACTIVIDAD

1 hora
