# Servicio DNS en Kubernetes

Existe un componente de Kubernetes llamado CoreDNS, que ofrece un servidor DNS para que los pods puedan resolver diferentes nombres de recursos (servicios, pods, ...) a direcciones IP.

Cada vez que se crea un nuevo servicio se crea un registro de tipo A con el nombre: 

    <nombre_servicio>.<nombre_namespace>.svc.cluster.local.

## Comprobemos el servidor DNS

Partimos del punto anterior donde tenemos creados los dos servicios:

    kubectl get services
    mariadb      ClusterIP   10.106.60.233   <none>        3306/TCP       
    nginx        NodePort    10.110.81.74    <none>        80:32717/TCP   

Para comprobar el servidor DNS de nuestro cluster y de que podemos resolver los nombres de los distintos servicios, vamos a usar un pod ((`busybox.yaml`)[files/busybox.yaml]) creado desde una imagen `busybox`.  Es una imagen muy pequeña pero con algunas utilidades que nos vienen muy bien:

    kubectl apply -f busybox.yaml

¿Qué servidor DNS está configurado en los pods que estamos creando? Podemos ejecutar la siguiente instrucción para comprobarlo:

    kubectl exec -it busybox -- cat /etc/resolv.conf
    nameserver 10.96.0.10
    search default.svc.cluster.local svc.cluster.local cluster.local

* El servidor DNS (componente coreDNS) teien asignado la IP del cluster 10.96.0.10.
* Podemos utilizar el nombre corto del servicio, porque buscará el nombre del host totalmente cualificado usando los dominios indicados en el parámetro `search`. Como vemos el primer nombre de dominio es que se crea con los servicios: `default.svc.cluster.local` (recuerda que el *namespace* que estamos usando es `default`).

Vamos a comprobar que realmente se han creado dos registros A para cad uno de los servicio, haciendo consultas DNS:

    kubectl exec -it busybox -- nslookup nginx
    Server:		10.96.0.10
    Address:	10.96.0.10:53

    Name:	nginx.default.svc.cluster.local
    Address: 10.110.81.74

Vemos que ha hecho la resolución del nombre `nginx` con la IP correspondiente a su servicio. Y con el servicio mariadb también lo podemos hacer:

    kubectl exec -it busybox -- nslookup mariadb
    Server:		10.96.0.10
    Address:	10.96.0.10:53

    Name:	mariadb.default.svc.cluster.local
    Address: 10.106.60.233

También podemos comprobar que usando el nombre podemos acceder al servicio:

    kubectl exec -it busybox -- wget http://nginx
    Connecting to nginx (10.110.81.74:80)
    saving to 'index.html'
    ...
    
Podemos concluir, que cuando necesitemos desde alguna aplicación deplegada en nuestro cluster acceder a otro servicio ofrecido por otro despliegue, **utilizaremos el nombre que hemos asignado a su service de acceso**. Por ejemplo si desplegamos un WordPress y un servidor de base de datos mariadb, y creamos dos servicios: uno de tipo NodePort para acceder desde el exterior al CMS, y otro, que llamamos `mariadb` de tipo ClusterIP para acceder ala base de datos, cuando tengamos que configurar el WordPress para indicar la dirección de la base de datos, pondremos `mariadb`.





