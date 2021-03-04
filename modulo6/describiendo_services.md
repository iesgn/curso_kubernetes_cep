# Describiendo Services

## Services NodePort

Suponemos que tenemos desplegado nginx usando el fichero yaml: [`nginx-deployment.yaml`](../modulo5/files/nginx-deployment.yaml):

    kubectl apply -f nginx-deployment.yaml
  
Por lo tanto tenemos dos pods ofreciendo el servidor web nginx, a los que queremos acceder desde el exterior y que se balancee la carga entre ellos.

Aunque podríamos crear un recurso Service desde la línea de comandos:

    kubectl expose deployment/nginx --port=80 --type=NodePort
    
Normalmente lo que hacemos es describir las características del Service en un fichero yaml:

```yaml
apiVersion: v1
kind: Service
metadata:
  name: nginx
spec:
  type: NodePort
  ports:
  - name: http
    port: 80
    targetPort: http
  selector:
    app: nginx
```
Veamos la descripción:

* Vamos a crear un recurso Service (parámetro `kind`) y lo nombramos como `nginx` (parámetro `name`). Este nombre será importante para la resolución dns.
* En la especificación del recurso indicamos el tipo de servicio (parámetro `type`)..........