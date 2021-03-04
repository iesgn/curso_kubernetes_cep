# Describiendo Services

## Services NodePort

Suponemos que tenemos desplegado nginx usando el fichero yaml: [`nginx-deployment.yaml`](../modulo5/files/nginx-deployment.yaml):

    kubectl apply -f nginx-deployment.yaml
  
Por lo tanto tenemos dos pods ofreciendo el servidor web nginx, a los que queremos acceder desde el exterior y que se balacee la carga entre ellos.

Aunque podríamos crear un recurso Service desde la línea de comandos:

    kubectl expose deployment/nginx --port=80 --type=NodePort
    
Normalmente lo que hacemos es descrbir las características del Service en un fichero yaml:

```yaml

```
