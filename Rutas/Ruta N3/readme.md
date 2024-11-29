Pre Entrega de Proyecto:
   1. Crear un menú interactivo
   Crear un menú interactivo utilizando bucles while y condicionales if-elif-else: 
      ● El menú debe permitir al usuario seleccionar entre diferentes opciones relacionadas con la gestión de productos. 
      ● Entre las opciones, deben incluirse: agregar productos al inventario y mostrar los productos registrados
   2. Agregar productos al inventario
   Implementar la funcionalidad para agregar productos a una lista: 
      ● Cada producto debe ser almacenado en una lista, y debe tener al menos un nombre y una cantidad asociada.
   3. Mostrar el inventario
   Mostrar los productos ingresados: 
      ● Al seleccionar la opción correspondiente, el sistema debe permitir visualizar los productos almacenados hasta el 
      momento

En esta última etapa, te introducirás a los conceptos clave de bases de datos y SQL, esenciales para gestionar grandes volúmenes de datos. Aprenderás a crear y 
administrar bases de datos con SQLite, integrada con Python, y explorarás consultas SQL básicas como SELECT, INSERT, UPDATE y DELETE. 
Este módulo te proporcionará habilidades prácticas para gestionar bases de datos y realizar operaciones esenciales en tus aplicaciones Python.


src/
│
├── main.py                          # Punto de entrada de la aplicación
├── controllers/
│   └── product_controller.py        # Controlador para manejar la lógica del CRUD
├── models/
│   └── product_model.py             # Modelo que interactúa con SQLite
├── services/
│   └── product_service.py           # Lógica de negocio
├── utils/
│   ├── validate_input_product.py    # Validaciones de entradas
│   ├── messages.py                  # Mensajes comunes
│   └── db_connection.py             # Manejo de conexión a SQLite
└── data/
    └── database.db                  # Base de datos SQLite