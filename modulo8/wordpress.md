# Ejemplo 3: WordPress con almacenamiento persistente

kubectl get all,pv,pvc
NAME                                        READY   STATUS    RESTARTS   AGE
pod/mariadb-deployment-666cf54b68-dbplz     1/1     Running   0          10s
pod/wordpress-deployment-7768598bf8-v9mnb   1/1     Running   0          10s

NAME                        TYPE        CLUSTER-IP       EXTERNAL-IP   PORT(S)                      AGE
service/kubernetes          ClusterIP   10.96.0.1        <none>        443/TCP                      46d
service/mariadb-service     ClusterIP   10.103.146.225   <none>        3306/TCP                     10s
service/wordpress-service   NodePort    10.98.149.222    <none>        80:30072/TCP,443:32349/TCP   10s

NAME                                   READY   UP-TO-DATE   AVAILABLE   AGE
deployment.apps/mariadb-deployment     1/1     1            1           10s
deployment.apps/wordpress-deployment   1/1     1            1           10s

NAME                                              DESIRED   CURRENT   READY   AGE
replicaset.apps/mariadb-deployment-666cf54b68     1         1         1       10s
replicaset.apps/wordpress-deployment-7768598bf8   1         1         1       10s

NAME                                                        CAPACITY   ACCESS MODES   RECLAIM POLICY   STATUS   CLAIM                   STORAGECLASS   REASON   AGE
persistentvolume/pvc-01ed3c4c-a542-4161-93a9-b9d5ea2bf6d1   5Gi        RWX            Delete           Bound    default/wordpress-pvc   standard                10s
persistentvolume/pvc-78acc14b-71da-4cf0-861d-0ab7780bca4f   5Gi        RWX            Delete           Bound    default/mariadb-pvc     standard                10s

NAME                                  STATUS   VOLUME                                     CAPACITY   ACCESS MODES   STORAGECLASS   AGE
persistentvolumeclaim/mariadb-pvc     Bound    pvc-78acc14b-71da-4cf0-861d-0ab7780bca4f   5Gi        RWX            standard       10s
persistentvolumeclaim/wordpress-pvc   Bound    pvc-01ed3c4c-a542-4161-93a9-b9d5ea2bf6d1   5Gi        RWX            standard       10s


NAME                                          CLASS    HOSTS                  ADDRESS          PORTS   AGE
ingress.networking.k8s.io/wordpress-ingress   <none>   www.miwordpress.org    192.168.39.222   80      10s
