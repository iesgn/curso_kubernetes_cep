# El proyecto Kubernetes

El proyecto Kubernetes lo inicia Google en 2014 como un software
(libre) para orquestar contenedores. En aquel momento había varios
proyectos de software que querían extender las posibilidades del uso
de contenedores de aplicaciones tipo docker a entornos en producción,
lo que de forma genérica se conoce como orquestadores de
contenedores. A diferencia del resto, Kubernetes no es un proyecto que
se desarrolla desde cero, sino que aprovecha todo el conocimiento que
tenía Google con el uso de la herramienta interna
[Borg](https://kubernetes.io/blog/2015/04/borg-predecessor-to-kubernetes/),
de manera que cuando se hace pública la primera versión de Kubernetes,
la [0.2](https://github.com/kubernetes/kubernetes/releases/tag/v0.2)
ya era un software con muchas funcionalidades.

Un proyecto se convierte en software libre cuando utiliza una
[licencia libre](https://opensource.org/licenses/category), pero otro
aspecto importante es la gobernanza del proyecto, es decir, si el
desarrollo es abierto o no, si las decisiones sobre las nuevas
funcionalidades las toma una empresa o se consensúan, etc. Si un
proyecto de software libre lo inicia una única empresa, siempre existe
la desconfianza de que ese proyecto vaya a ir encaminado a beneficiar
a esa empresa. En este caso, la empresa en cuestión era un gigante
como Google, por lo que aunque el proyecto era muy interesante,
existía cierto recelo de gran parte del sector inicialmente. Para
conseguir que una parte importante del sector se sumase al proyecto,
Google tomó la decisión de desvincularse del mismo y ceder el control
a la [Cloud Native Compute Foundation (CNCF)](https://www.cncf.io/),
por lo que Kubernetes es un proyecto de software libre de fundación,
en la que se admiten contribuciones de forma abierta y las reglas de
la gobernanza recaen sobre los [miembros de la
fundación](https://www.cncf.io/about/members/), normalmente un
conjunto amplio de grandes empresas del sector. Es decir, aunque hoy
en día hay quien habla de Kubernetes como el software de orquestación
de contenedores de Google, esto es un error, es un proyecto que
gestiona desde hace años la CNCF, a la que ni siquiera pertenece
Google.

## ¿Qué es Kubernetes?

Kubernetes es un software pensado para gestionar completamente el
despliegue de aplicaciones sobre contenedores, realizando este
despliegue de forma completamente automática y poniendo un gran
énfasis en la escalabilidad de la aplicación, así como el control
total del ciclo de vida. Por destacar algunos de los puntos más
importantes de Kubernetes, podríamos decir:

* Despliega aplicaciones rápidamente
* Escala las aplicaciones al vuelo
* Integra cambios sin interrupciones
* Permite limitar los recursos a utilizar

Kubernetes está centrado en la puesta en **producción** de
contenedores y por tanto indicada su gestión para administradores de
sistemas y personal de equipos de operaciones. Por otra parte, afecta
a los desarrolladores, ya que las aplicaciones deben adaptarse para
poder desplegarse en kubernetes.

## Características principales

<img src="https://raw.githubusercontent.com/kubernetes/kubernetes/master/logo/logo.png" alt="k8s-logo" width="150" />

Kubernetes surge como un software para desplegar aplicaciones sobre
contenedores que utilicen infraestructura en nube (pública, privada o
híbrida). Aunque puede desplegarse también en entornos más
tradicionales como servidores físicos o virtuales, no es su "entorno
natural".

Kubernetes es extensible, por lo que cuenta con gran cantidad de
módulos, plugins, etc.

El nombre del proyecto proviene de una palabra de griego antiguo que
significa timonel y habitualmente se escribe de forma abreviada como
k8s.

## El ecosistema

De entre todas las opciones de orquestadores de contenedores
disponibles, hoy se considera que la opción preferida en la mayor
parte de los casos es k8s y se ha desarrollado un enorme ecosistema de
aplicaciones alrededor que proporcionan algunas funcionalidades que no
tiene k8s o que de alguna forma utiliza o se pueden integrar de
diferente forma con k8s. Este ecosistema de aplicaciones está
actualmente en plena "ebullición" y es posible que en unos años
algunos de esos proyectos se estabilicen y otros desaparezcan, ya que
en muchos casos solapan unos con otros.

[https://landscape.cncf.io/](https://landscape.cncf.io/)
