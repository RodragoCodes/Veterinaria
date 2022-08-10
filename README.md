#Proyecto Veterinaria

Este proyecto es para un desafio entregable en CODERHOUSE.

Orden logico de procesos a correr:

1) Correr el servidor con el comando 'python .\manage.py runserver'.
2) Una vez en la url ejecutar el path "/inicio" para acceder la pagina principal.
3) En la pagina principal puedes navegar en las diferentes pestañas sin problemas (pestañas de procedimientos, cliente y mascotas).
4) Si accedes a la pestaña Clientes se mostrara una lista con los ultimos clientes atendidos por la clinica.
5) Si accedes a la pestaña mascotas se mostraran los nombres de las mascotas atendidas, el tipo y su edad.
6) Si accedes a la pestaña procedimientos se mostraran todos los procedimientos que realiza la clinica veterinaria y sus diferentes costos en dolares.
7) Cabe destacar que cada pestaña tiene relacion con un modelo de datos (3 modelos diferentes "cliente", "mascotas" y "procedimientos").
8) Tambien se puede insertar datos a cada uno de los modelos anteriormente descritos.
9) Para insertar datos al modelo "cliente" se debe hacer a traves del path "/clientes/crear".
10) Para insertar datos al modelo "mascotas" se debe hacer a traves del path "/mascota/crear".
11) Para insertar datos al modelo "procedimientos" se debe hacer a traves del path "/procedimiento/crear".
12) Y por ultimo se puede acceder a buscar diferentes clientes por su nombre en el path "/buscar".