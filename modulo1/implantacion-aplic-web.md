# Implantación de aplicaciones web

El protocolo http, o su extensión https, ha ido convirtiéndose poco a
poco en el "superprotocolo" de Internet y ha ido desplazando
paulatinamente el uso de otros protocolos. De igual forma, la mayor
parte del software que se consume hoy en día se podría denominar de
forma genérica como aplicaciones web, aunque hay diferencias
importantes sobre la forma de presentarse, ya que no es lo mismo que
acceda a una aplicación una persona a través de un navegador, a través
de una aplicación móvil o que quien acceda a la aplicación sea una
máquina. En este curso no podemos entrar en detalle sobre las
características de estas aplicaciones web, pero sí en las
características que deben tener los sistemas que las ofrecen para que
cumplan con los requisitos esperados.

## Requisitos habituales de las aplicaciones web

Pensemos inicialmente en el caso de una aplicación interna de una
empresa que está instalada localmente y que los únicos usuarios que
tiene son la plantilla de empleados de la empresa. En ese caso, es
fácil determinar los recursos necesarios para que la aplicación
funcione de forma adecuada, porque ni el uso de la aplicación se
dispara en unos instantes, ni el número de empleados de una empresa
varía de forma abrupta. Por otra parte, las actualizaciones se pueden
hacer en momentos en los que el uso es mínimo y si es necesario una
interrupción del servicio, se puede programar para un momento
determinado en que tenga muy poco impacto. Las aplicaciones de este
tipo no se suelen modificar habitualmente, sino que lo hacen de forma
bastante espaciada en el tiempo, por lo que los cambios entre una
versión y otra son significativos. Esto, que podríamos llamar
informática tradicional, también tiene un impacto importante en la
forma de desarrollar las aplicaciones que funcionan bajo este
esquema.

Por otra parte, una aplicación web que esté disponible en Internet,
tiene miles de millones de potenciales usuarios, que la pueden usar
las 24 horas del día y cualquier día del año. Esto tiene unas
consecuencias muy importantes, ya que es muy difícil determinar los
recursos necesarios para prestar servicios a una demanda muy variable
e idealmente el servicio no puede interrumpirse nunca. Pero, ¿esto
cómo se hace?¿Es posible que el mismo sistema se ajuste a una demanda
que puede variar de un usuario a un millón?, ¿es posible tener un
sistema siempre actualizado y que a la vez no se pare?, ¿cómo se
aplican las actualizaciones de software? ¿poco a poco o con grandes
saltos? Durante este curso, veremos que precisamente esto es lo que
trata de proporcionar Kubernetes.

## Componentes auxiliares de un servicio web

El componente esencial para servir una aplicación web es un servidor
web, pero vamos a ver a continuación, que para poder proporcionar el
servicio con los requisitos anteriores, debe apoyarse en un número
importante de componentes auxiliares. En los siguientes apartados
vamos a ir viendo paso a paso la forma de ir incluyendo diferentes
componentes auxiliares y cómo va a ir cambiando la arquitectura de los
sistemas que proporcionan el servicio.

### Punto de partida

Supongamos que nuestra organización proporciona tres aplicaciones web
diferentes que son accesibles a través de las URL:

https://example.com/app1
https://example.com/app2
https://example.com/app3

Estas aplicaciones pueden estar desarrolladas en el mismo lenguaje o
en uno diferente (Python, Java, PHP, etc.), pueden utilizar una base
de datos, almacenamiento auxiliar y como se sirven a través de https,
es necesario gestionar los certificados x509.

El esquema inicial que pensaríamos para proporcionar estas tres
aplicaciones sería una máquina (física o virtual) en la que
instalaríamos el servidor web, los servidores de aplicaciones (php,
java, ...), el servidor de bases de datos, etc. tal como aparece en la
siguiente imagen:

<img src="https://github.com/iesgn/curso_kubernetes_cep/raw/main/modulo1/img/paso1.png" alt="paso1" />

### Paso 2. Servidor de bases de datos separado

Desde un punto de vista de seguridad, ubicar el servidor de bases de
datos en el mismo equipo que el servidor web es totalmente inadecuado,
ya que el servidor web, por su propia naturaleza debe permitir que
cualquier usuario acceda desde Internet y una vulnerabilidad en este
equipo podría exponer los datos que se ubican en las bases de datos a
un potencial atacante. Además, desde el punto de vista del rendimiento
y la disponibilidad, separar los servicios en diferentes equipos hace
que no haya interacciones entre ellos y no compitan por los mismos
recursos.

<img src="https://github.com/iesgn/curso_kubernetes_cep/raw/main/modulo1/img/paso2.png" alt="paso2" />

