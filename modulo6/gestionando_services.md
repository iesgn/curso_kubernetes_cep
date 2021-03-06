# Gestionando los Services

Para aprender cómo trabajamos con los servicios, vamos a trabajar con el despliegue de nginx ([`nginx-deployment.yaml`](../modulo5/files/nginx-deployment.yaml)) y el servicio NodePort ([`nginx-srv.yaml`](files/nginx-srv.yaml)) para acceder a los pods de este despliegue desde el exterior.

## Creamos el despliegue

El primer paso sería crear el despliegue de nginx:

    kubectl apply -f nginx-deployment.yaml

## Creamos el servicio

A continuación vamos a crear el servicio de tipo NodePort que nos permitirá acceder al servidor nginx.

    kubectl apply -f nginx-srv.yaml

Para ver los servicios que tenemos creado:

    kubectl get services
    
Recuerda que si usamos `kubectl get all` también se mostrarán los Services.

Antes de acceder a la aplicación podemos ver la información más detallada del servicio que acabamos de crear:

    kubectl describe service/nginx
    Name:                     nginx
    ...
    Selector:                 app=nginx
    Type:                     NodePort
    ...
    IP:                       10.110.81.74
    Port:                     service-http  80/TCP
    TargetPort:               http/TCP
    NodePort:                 service-http  32717/TCP
    Endpoints:                172.17.0.3:80,172.17.0.4:80
    ...

Podemos ver la etiqueta de los pods a los que accede (`Selector`). El tipo de Service (`Type`). La IP virtual que ha tomado (CLUSTER-IP) y que es accesible desde el cluster (`IP`). El puerto por el que ofrece el servicio (`Port`). El puerto de los pods a los que redirige el tráfico (`TargetPort`). Al ser un service de tipo NodePort no da información del puerto que se asignado para acceder a la aplicación (`NodePort`). Y por último, podemos las ip de los pods que ha seleccionado y sobre los que balanceará la carga (`Endpoints`).

## Accediendo a la aplicación

Vemos el servicio que hemos creado:

    kubectl get services
    ...
    nginx        NodePort    10.110.81.74   <none>        80:32717/TCP   32s

Y observamos que se ha asignado el puerto 32717 para el acceso, por lo tanto si desde un navegador accedemos a la ip del nodo master y a este puerto podremos ver la aplicación.

¿Cómo se la dirección ip del nodo master del cluster minikube? Podemos ejecutar:

    minikube ip
    192.168.39.222

Y ya podemos acceder desde un navegador web:

![Acceso a nginx](img/nginx.png)
