# Despliegues parametrizados: Secrets

Cuando en un variable de entorno indicamos una información sensible, como por ejemplo una contraseña, una clave ssh,... solemos utilizar un nuevo recurso de kubernetes llamado **secret**.

Los [Secrets](https://kubernetes.io/docs/concepts/configuration/secret/) nos permiten guardar información sensible que será **codificada**. 

Hay distinto tipos de Secret, en este curso vamos a usar los genéricos y lo vamos a crear a partir de un literal, por ejemplo para guardar la contraseña del usuario root de una base de datos, crearíamos un secret de la siguiente manera:

    kubectl create secret generic mariadb --from-literal=password=my-password

Podemos obtener información de los secret que hemos creado con las instrucciones:

    kubectl get secret
    kubectl describe secret mariadb

Veamos a continuación como quedaría un despliegue que usa el valor de un Secret para inicializar una variable de entorno. Vamos a usar el fichero [`mariadb-deployment-secret.yaml`](files/mariadb-deployment-secret.yaml) y el fragmento donde definimos las variables de entorno quedaría:

```yaml
...
    spec:
      containers:
        - name: mariadb
          image: mariadb
          ports:
            - containerPort: 3306
              name: db-port
          env:
            - name: MYSQL_ROOT_PASSWORD
              valueFrom:
                secretKeyRef:
                  name: mariadb
                  key: password
```
Donde observamos como al indicar las variables de entorno (sección `env`) seguimos indicado el nombre (`name`) pero el valor se indica con un valor de un Secret (`valueFrom: - secretKeyRef:`), indicando el nombre del Secret (`name`) y la clave correspondiente. (`key`).