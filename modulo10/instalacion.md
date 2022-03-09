# Instalación de helm

Helm se distribuye como un único binario que podemos instalar de distintas formas. La última versión del programa la podemos encontrar en esta [página](https://github.com/helm/helm/releases/) y podemos ver los distintos métodos de instalación en la [documentación oficial](https://helm.sh/docs/intro/install/).

Una vez instalado podemos ver la versión de Helm que tenemos instalada:

```bash
helm version
```

Los siguiente es indicar un repositorio para que podamos empezar a trabajar con helm, para ello:

```bash
helm repo add "stable" "https://charts.helm.sh/stable" --force-update
```

Y ahora el repositorio `stable` corresponde a `charts.helm.sh/stable`:

```bash
helm repo list
NAME  	URL
stable	https://charts.helm.sh/stable
```

## Vídeo

[https://www.youtube.com/watch?v=tRBCdOYOfnU](https://www.youtube.com/watch?v=tRBCdOYOfnU)
