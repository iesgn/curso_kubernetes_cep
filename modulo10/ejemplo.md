# Gestión de charts y despliegue de aplicaciones

## Gestión de repositorios

Como hemos visto anteriormente, por defecto, tenemos instalado un repositorio:

```bash
helm repo list
NAME  	URL                          
stable	https://charts.helm.sh/stable
```

Podemos buscar más repositorios de charts buscando en la página [Artifact Hub](https://artifacthub.io/), por ejemplo podemos añadir el repositorio de charts de Bitnami de la siguiente manera:

```bash
helm repo add bitnami https://charts.bitnami.com/bitnami
"bitnami" has been added to your repositories
```

Y podemos comprobar que hemos añadido un nuevo repositorio:

```bash
helm repo list
NAME   	URL                               
stable 	https://charts.helm.sh/stable     
bitnami	https://charts.bitnami.com/bitnami
```

Si queremos actualizar la lista de charts ofrecidos por los repositorios:

```bash
helm repo update
Hang tight while we grab the latest from your chart repositories...
...Successfully got an update from the "stable" chart repository
...Successfully got an update from the "bitnami" chart repository
Update Complete. ⎈Happy Helming!⎈
```

## Buscar charts

Como hemos comentado anteriormente, los charts los podemos buscar en la página [Artifact Hub](https://artifacthub.io/) o los podemos buscar desde la línea de comandos, por ejemplo si queremos buscar un chart relacionado con `nginx`:

```bash
helm search repo nginx
NAME                            	CHART VERSION	APP VERSION	DESCRIPTION                                       
bitnami/nginx                   	9.3.0        	1.21.0     	Chart for the nginx server                        
bitnami/nginx-ingress-controller	7.6.12       	0.47.0     	Chart for the nginx Ingress controller            
stable/nginx-ingress            	1.41.3       	v0.34.1    	DEPRECATED! An nginx Ingress controller that us...
stable/nginx-ldapauth-proxy     	0.1.6        	1.13.5     	DEPRECATED - nginx proxy with ldapauth            
...
```

Para obtener información sobre el chart `bitnami/nginx` podemos buscar en [Artifact Hub](https://artifacthub.io/).

Todos los ficheros yaml que forman parte de un chart están parametrizados, es decir cada propiedad tiene un valor por defecto, pero a la hora de instalarlo se puede cambiar. Por ejemplo, ¿qué tipo de Service se creará al instalar el chart `bitnami/nginx`? Por defecto, el parámetro `service.type` tiene como valor `LoadBalancer`, pero si queremos un Service de tipo `NodePort`, podremos redefinir este parámetro a la hora de instalar el chart.

¿Y cómo sabemos los parámetros que tiene definido cada chart y sus valores por defecto?. Estudiando la documentación del chart en [Artifact Hub](https://artifacthub.io/). En concreto para el chart con el que estamos trabajando, accediendo a la url [https://artifacthub.io/packages/helm/bitnami/nginx](https://artifacthub.io/packages/helm/bitnami/nginx). También podemos obtener esta información ejecutando el siguiente comando:

```bash
helm show all bitnami/nginx
```

## Instalación del chart

Para instalar el chart ejecutamos la siguiente instrucción:

```bash
helm install serverweb bitnami/nginx --set service.type=NodePort
```

Como vemos hemos nombrado el chart desplegado (`serverweb`), indicado el chart (`bitnami/nginx`) y, en este caso, hemos redefinido el parámetro `service.type`.

Cuando se despliega el chart se nos ofrece información que nos muestra cómo acceder a la aplicación:

```
NOTES:
** Please be patient while the chart is being deployed **

NGINX can be accessed through the following DNS name from within your cluster:

    serverweb-nginx.default.svc.cluster.local (port 80)

To access NGINX from outside the cluster, follow the steps below:

1. Get the NGINX URL by running these commands:

    export NODE_PORT=$(kubectl get --namespace default -o jsonpath="{.spec.ports[0].nodePort}" services serverweb-nginx)
    export NODE_IP=$(kubectl get nodes --namespace default -o jsonpath="{.items[0].status.addresses[0].address}")
    echo "http://${NODE_IP}:${NODE_PORT}"
```

Si queremos acceder a la aplicación desde el exterior debemos ejecutar las tres últimas instrucciones, que nos muestran la ip de nuestro cluster y el puerto asignado al Service NodePort.

Siempre podemos volver a ver esta información ejecutando la siguiente instrucción:

```bash
helm status serverweb
```

Podemos comprobar los Deployments que hemos realizado con Helm, ejecutando:

```bash
helm ls
NAME     	NAMESPACE	REVISION	UPDATED                                 	STATUS  	CHART      	APP VERSION
serverweb	default  	1       	2021-06-29 19:11:15.975016119 +0200 CEST	deployed	nginx-9.3.0	1.21.0   
```

Y podemos comprobar también los recursos que se han creado en el cluster:

```bash
kubectl get all
NAME                                   READY   STATUS    RESTARTS   AGE
pod/serverweb-nginx-7b7f75d476-kxq8j   1/1     Running   0          56s

NAME                      TYPE        CLUSTER-IP     EXTERNAL-IP   PORT(S)        AGE
service/kubernetes        ClusterIP   10.96.0.1      <none>        443/TCP        5m14s
service/serverweb-nginx   NodePort    10.99.80.141   <none>        80:30137/TCP   56s

NAME                              READY   UP-TO-DATE   AVAILABLE   AGE
deployment.apps/serverweb-nginx   1/1     1            1           56s

NAME                                         DESIRED   CURRENT   READY   AGE
replicaset.apps/serverweb-nginx-7b7f75d476   1         1         1       56s
```

Por último, para desinstalar una aplicación completa, ejecutamos:

```bash
helm delete serverweb
release "serverweb" uninstalled
```

Aunque no entra en el ámbito de este curso, hay que indicar que si nosotros desarrollamos una aplicación podemos empaquetarla para instalarla con Helm, creando nuestros propios charts. Para más información puedes entrar en la [documentación oficial](https://helm.sh/docs/chart_template_guide/#the-chart-template-developer-s-guide).

## Vídeo

[https://www.youtube.com/watch?v=UlkXAFHvrkw](https://www.youtube.com/watch?v=UlkXAFHvrkw)
