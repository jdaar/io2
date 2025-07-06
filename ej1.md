# Ejercicio 1 (Teoria de colas)

## Enunciado

Asuma que es usted un desarrollador de software al cual le fue asignada la tarea de orquestrar la comunicacion entre diversos servicios bancarios, la gerencia de tecnologia de la compañia ha decidido que dichos servicios sean ejecutados en maquinas diferentes para garantizar la resiliencia del sistema.

Se le indica que existen tres servicios diferentes cada uno con su respectiva carga, la carga de cada servicio es diferente, pues se necesita una capacidad computacional diferente para poder cumplir con todas las reglas de negocio:

La carga se mide en hilos usados por minuto

- Creacion de cuenta bancaria (1 hilo por minuto de carga)
- Transferencia de dinero a otra cuenta bancaria (2 hilos por minuto de carga)
- Cashout (2 hilos por minuto de carga)

Usted cuenta con una cola de mensajeria a la cual estan suscritos todos los servidores, que en el momento son 4, se le indican las siguientes condiciones de cada servidor:

- Cada servidor tiene 8 hilos
- Despues de un analisis del equipo de TI de la compañia, se asegura que cada servicio se ejecuta en maximo un minuto
- Para evitar fallas de seguridad, todas las transacciones le responden al usuario unicamente al pasar el minuto maximo de procesamiento (para evitar timing attacks), esto implica que TODAS las transacciones duran el mismo tiempo
- Un servidor NO puede aceptar la ejecucion de un servicio si no cuenta con los hilos de carga necesarios para el correcto funcionamiento
- Un servidor puede aceptar la ejecucion de servicios paralelamente

Recientemente por parte de la gerencia de TI se ha notado un aumento significativo en el uso de los servicios por parte de los clientes, por lo que se ha recolectado datos de uso para actualizar los equipos de manera que puedan gestionar correctamente la carga de los clientes

El comportamiento evidenciado es el siguiente

- Creacion de cuenta bancaria (5 usuarios por minuto)
- Transferencia de dinero a otra cuenta bancaria (20 usuarios por minuto)
- Cashout (15 usuarios por minuto)

Dado el aumento de uso por parte de los usuarios, se le solicita analizar el comportamiento de cada maquina para validar si es necesaria una actualizacion de las mismas.

En caso de que las maquinas actuales sean suficientes para manejar la nueva carga se le solicita encontrar el limite de carga que pueden aceptar.

En el caso contrario, se le solicita evaluar dos opciones, realizar un escalado horizontal (añadir nuevas maquinas) o un escalado vertical (mejorar la capacidad en hilos de cada maquina). Dada la naturaleza de cada escalado, el escalado vertical es mas costoso que el escalado horizontal, puesto que es necesario hacer el reemplazo de todas las maquinas actuales. La empresa presupuesto 50 millones de COP para realizar cualquiera de los dos escalados (solo uno de ellos), se le solicita determinar cual de los dos escalados es mas optimo dadas las siguientes cotizaciones:

- La compra de una maquina cuesta 8 millones de COP
- La actualizacion de una maquina para que esta cuente con 16 hilos cuesta 5 millones de COP


## Posibles diagramas

### Diagrama de flujo

```md
flowchart TD
    %% Nodes Definitions
    subgraph Arrivals [Llegadas de Usuarios]
        A1("Creación de Cuenta (5/min)")
        A2("Transferencia (20/min)")
        A3("Cashout (15/min)")
    end

    Q([Cola de Mensajería])

    subgraph Cluster [Clúster de Servidores]
        direction TB
        S1("Servidor 1 (8 hilos)")
        S2("Servidor 2 (8 hilos)")
        S3("...")
        S10("Servidor 10 (8 hilos)")
    end

    R((Respuestas a Usuarios))

    %% Flow Definitions
    A1 -- "Carga: 5 hilos/min" --> Q
    A2 -- "Carga: 40 hilos/min" --> Q
    A3 -- "Carga: 30 hilos/min" --> Q

    Q -- "Total: 75 hilos/min" --> Cluster
    Cluster -- "Procesamiento (μ=1 min)" --> R

    %% Styling
    classDef queue fill:#f9f,stroke:#333,stroke-width:2px;
    class Q queue;
```


