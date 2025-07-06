# Ejercicio 2 (Teoria de inventarios)

## Terminologia

- Centro de datos: Ubicacion fisica en la cual se almacenan y ejecutan multiples servidores.
- On-Site: Centro de datos propio, implica el control total y responsabilidad no compartida de las maquinas.
- Infraestructura: Conjunto de servicios y recursos necesarios para que una aplicacion de software funcione correctamente.
- Servicios en nube: Servicios ofrecidos por un proveedor de nube, los servicios ofrecidos dependen del proveedor pero en general suelen ser servicios computacionales, se puede pensar como alquilar servidores (sobresimplificado).

- Base de datos: Servicio de almacenamiento de datos, permite guardar datos para luego acceder a ellos.
- Servidor de aplicacion: Servidor (computador) especializado para la ejecucion de aplicaciones.
- Cola de mensajeria: Cola que almacena mensajes para enviarlos a una maquina y que esta los procese.
- Instanciacion: Creacion de un recurso

- Resiliencia: Capacidad de manejo de errores inesperados de una aplicacion.
- Disponibilidad: Capacidad de acceso a una aplicacion por parte de un usuario final.

- Almacenamiento conectado a la red (NAS): Almacenamiento disponible para multiples maquinas dentro de una red.
- Almacenamiento de objetos: Almacenamiento disponible globalmente ofrecido por un proveedor de nube.

## Enunciado

La Bolsa Mercantil de Colombia cuenta con dos aplicaciones que disponibiliza a sus empleados y clientes, puesto que se trata de una entidad financiera auditada por entidades reguladoras, se requiere que el negocio actualice sus equipos anualmente para garantizar el correcto funcionamiento de los aplicativos que el negocio maneja y evitar problemas de ciberseguridad.

Dado que pronto el negocio tendra que actualizar sus maquinas, se desea evaluar si es rentable hacer una migracion a la nube y ha determinado que desea usar una de dos opciones Amazon Web Services o Microsoft Azure.

Usted fue contratado por la Bolsa Mercantil de Colombia como arquitecto de nube para agilizar y garantizar una correcta transicion de una infraestructura On-Site a una infraestructura en la nube.

Dado que se desea hacer una migracion, se busca tener alternativas que correspondan uno a uno con la infraestructura actual que se posee.

Actualmente el negocio cuenta con los siguientes recursos:

- 6 bases de datos (1 para dev, qa y prod respectivamente)
- 2 servidores de aplicacion (en cada servidor corren tres entornos, dev, qa, prod)
- 1 servidor para cola de mensajeria 
- 4 almacenamientos conectados a la red (NAS)

Se cuentan con las siguientes alternativas de nube:

- 1 instancias de bases de datos equivalen a 3 base de datos On-Site
- 3 contenedores equivalen a 1 servidor On-Site
- 2 colas de mensajeria equivalen a un servidor para cola de mensajeria On-Site
- 1 almacenamiento de objetos equivale a 1 almacenamiento conectado a la red (NAS)

El negocio necesita que se cumpla como minimo con la infraestructura original, por lo cual no es admisible que se presente ningun faltante, pero tambien desea hacer una mejoria en cuanto a la resiliencia y disponibilidad de la aplicacion, por lo que desean contar con mas recursos que puedan suplir necesidades para usuarios nuevos

El costo de adquisicion y mantenimeinto actual de los equipos es como sigue:

- 1 base de datos cuesta 100.000 COP anual por mantenimiento y 500.000 COP una unica ocasion por adquisicion
- 1 servidor de aplicacion cuesta 125.000 COP anual por mantenimiento y 1.000.000 COP una unica ocasion por adquisicion
- 1 servidor de cola de mensajeria cuesta 50.000 COP anual por mantenimiento 750.000 COP por adquisicion
- 1 almacenamiento conectado a la red (NAS) cuesta 25.000 COP anual por mantenimiento y 250.000 COP por adquisicion

El costo de migracion a nube de Amazon Web Services los equipos es como sigue:

- 1 instancia de base de datos cuesta 2.000.000 COP anual por mantenimiento y 100.000 COP una unica ocasion por instanciacion
- 1 contenedor cuesta 250.000 COP anual por mantenimiento y 0 COP una unica ocasion por instanciacion
- 1 cola de mensajeria cuesta 500.000 COP anual por mantenimiento y 0 COP una unica ocasion por instanciacion
- 1 almacenamiento de objetos cuesta 100.000 COP anual por mantenimiento y 20.000 COP una unica ocasion por instanciacion

El costo de migracion a nube de Microsoft Azure los equipos es como sigue:

- 1 instancia de base de datos cuesta 1.500.000 COP anual por mantenimiento y 200.000 COP una unica ocasion por instanciacion
- 1 contenedor cuesta 500.000 COP anual por mantenimiento y 0 COP una unica ocasion por instanciacion
- 1 cola de mensajeria cuesta 375.000 COP anual por mantenimiento y 10.000 COP por unica ocasion por instanciacion
- 1 almacenamiento de objetos cuesta 125.000 COP anual por mantenimeinto y 15.000 COP por unica ocasion por instanciacion

Dado que con un proveedor de nube no se debe realizar ninguna tarea logistica puesto que los servidores se encuentran en el centro de datos del proveedor, hacer pedidos a el proveedor de nube NO tiene costo de pedido. Sin embargo, para el caso de los recursos On-Site se debe pagar por el transporte de los mismos al centro de datos del negocio, el cual tiene un costo de 100.000 COP por pedido.

Se le solicita evaluar para cada alternativa (On-Site, Amazon Web Services, Microsoft Azure) lo siguiente:

- Cuantos recursos en promedio se tendrian?
- Que tantos recursos se deberia solicitar anualmente?
- Que alternativa optimizaria los costos para el negocio, sin afectar al funcionamiento de las aplicaciones?

