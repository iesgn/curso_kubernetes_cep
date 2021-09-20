# Job

El objeto [Job](https://kubernetes.io/docs/concepts/workloads/controllers/job/)
 se utiliza cuando queremos ejecutar una tarea puntual,
para lo que se define el objeto y se crean todos los objetos
necesarios para realizarla, principalmente creando uno o varios Pods
hasta que se finaliza la tarea.
Una vez se termina la tarea y de forma general, los pods permanecerán
creados y no se borrarán hasta que se elimine el Job que los creó.

Un ejemplo de Job tendría el siguiente aspecto:

```yaml
apiVersion: batch/v1
kind: Job
metadata:
  name: pi
spec:
  template:
    spec:
      containers:
      - name: pi
        image: perl
        command: ["perl",  "-Mbignum=bpi", "-wle", "print bpi(2000)"]
      restartPolicy: Never
  backoffLimit: 4
```

En el ejemplo anterior se lanza un contenedor de la imagen perl y
realiza el cálculo de Pi con una precisión de 2000 decimales
utilizando este lenguaje.

Una vez lanzada la tarea, podremos ver que se crea tanto un objeto Job
como un Pod, el primero aparece sin finalizar y el Pod aparece
ejecutándose:

```
NAME           READY   STATUS    RESTARTS   AGE
pod/pi-jbt4r   1/1     Running   0          4s

...

NAME           COMPLETIONS   DURATION   AGE
job.batch/pi   0/1           4s         4s
```

Sin embargo, una vez que la tarea del contenedor finaliza, en este
caso cuando se consigue el número Pi con dos mil decimales de
precisión, el Pod se para y la tarea se marca como completada:

```
NAME           READY   STATUS      RESTARTS   AGE
pod/pi-jbt4r   0/1     Completed   0          10s

....

NAME           COMPLETIONS   DURATION   AGE
job.batch/pi   1/1           9s         10s
```

Podemos ver que no se borra el Pod, ya que lo necesitamos en muchas
ocasiones para ver el resultado de la tarea. En este caso para ver el
número Pi con la precisión solicitada, veríamos los logs del pod:

```
kubectl logs pi-jbt4r
3.1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679821480865132823066470938446095505822317253594081284811174502841027019385211055596446229489549303819644288109756659334461284756482337867831652712019091456485669234603486104543266482133936072602491412737245870066063155881748815209209628292540917153643678925903600113305305488204665213841469519415116094330572703657595919530921861173819326117931051185480744623799627495673518857527248912279381830119491298336733624406566430860213949463952247371907021798609437027705392171762931767523846748184676694051320005681271452635608277857713427577896091736371787214684409012249534301465495853710507922796892589235420199561121290219608640344181598136297747713099605187072113499999983729780499510597317328160963185950244594553469083026425223082533446850352619311881710100031378387528865875332083814206171776691473035982534904287554687311595628638823537875937519577818577805321712268066130019278766111959092164201989380952572010654858632788659361533818279682303019520353018529689957736225994138912497217752834791315155748572424541506959508295331168617278558890750983817546374649393192550604009277016711390098488240128583616035637076601047101819429555961989467678374494482553797747268471040475346462080466842590694912933136770289891521047521620569660240580381501935112533824300355876402474964732639141992726042699227967823547816360093417216412199245863150302861829745557067498385054945885869269956909272107975093029553211653449872027559602364806654991198818347977535663698074265425278625518184175746728909777727938000816470600161452491921732172147723501414419735685481613611573525521334757418494684385233239073941433345477624168625189835694855620992192221842725502542568876717904946016534668049886272327917860857843838279679766814541009538837863609506800642251252051173929848960841284886269456042419652850222106611863067442786220391949450471237137869609563643719172874677646575739624138908658326459958133904780275901
```

## Para seguir aprendiendo
* Para más información acerca de los Jobs puedes leer la
[documentación de la API](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.20/#job-v1-batch).

# CronJob

En el caso de que la tarea que tengamos que realizar no sea puntual,
sino que se tenga que repetir cada cierto tiempo conforme a un patrón,
k8s ofrece el objeto [CronJob](https://kubernetes.io/docs/concepts/workloads/controllers/cron-jobs/), que creará tareas conforme a la
periodicidad que se indique.

En el siguiente ejemplo de CronJob, ejecutamos una tarea cada minuto,
en la que se muestra la fecha y hora junto al texto "Curso del CEP":

```yaml
apiVersion: batch/v1
kind: CronJob
metadata:
  name: hello
spec:
  schedule: "*/1 * * * *"
  jobTemplate:
    spec:
      template:
        spec:
          containers:
          - name: hello
            image: busybox
            imagePullPolicy: IfNotPresent
            command:
            - /bin/sh
            - -c
            - date; echo Curso del CEP
          restartPolicy: OnFailure
```

Para la definición del objeto CronJob debe especificarse un nombre y
el patrón de repetición conforme al cron de UNIX, además de incluir en
jobTemplate la definición del objeto Job que se desea ejecutar.

## Para seguir aprendiendo
* Para más información acerca de los CronJobs puedes leer la
[documentación de la API](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.20/#cronjob-v1beta1-batch).
