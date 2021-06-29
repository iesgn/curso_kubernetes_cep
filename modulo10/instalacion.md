# Instalación de helm

Helm se distribuye como un único binario que podemos instalar de distintas formas. La última versión del programa lo podemos encontrar en esta [página](https://github.com/helm/helm/releases/) y podemos ver los distintos métodos de instalación en la [documentación oficial](https://helm.sh/docs/intro/install/).

Una vez instalado podemos ver la versión de helm que tenemos instalada:

```bash
$ helm version
```

Por defecto, tenemos instalado un repositorio llamado `kubernetes-charts.storage.googleapis.com`, que como se nos advierte, está obsoleto:

```bash
$ helm repo list
WARNING: "kubernetes-charts.storage.googleapis.com" is deprecated for "stable" and will be deleted Nov. 13, 2020.
WARNING: You should switch to "https://charts.helm.sh/stable" via:
WARNING: helm repo add "stable" "https://charts.helm.sh/stable" --force-update
NAME  	URL                                             
stable	https://kubernetes-charts.storage.googleapis.com
```

Así, que actualizamos a `https://charts.helm.sh/stable`, tal como se recomienda:

```bash
$ helm repo add "stable" "https://charts.helm.sh/stable" --force-update
```

Y ahora el repositorio `stable` corresponde a `charts.helm.sh/stable`:

```bash
helm repo list
NAME  	URL                          
stable	https://charts.helm.sh/stable
```
