# Milton Project API

Este repositorio contiene el código fuente de la API de Django para el proyecto "Milton Project". La API está diseñada para facilitar la gestión de 
productos, categorías, órdenes, calificaciones y clientes a través de endpoints RESTful.

## Características

- **Modelos**:
  - **Productos**: Representa los productos disponibles en el sistema, asociados a categorías específicas.
  - **Categorias**: Define las diferentes categorías a las que pueden pertenecer los productos.
  - **Ordenes**: Gestiona las órdenes realizadas por los clientes, incluyendo el estado de la orden y los productos solicitados.
  - **Calificación**: Permite a los clientes calificar los productos y añadir comentarios.
  - **Clientes**: Almacena la información de los clientes, como dirección, correo electrónico y teléfono.

- **Endpoints**: Lista de los endpoints disponibles y sus funcionalidades.
- **Autenticación**: Método utilizado para autenticar las solicitudes a la API (por ejemplo, JWT, OAuth2).

## Requisitos

Antes de instalar y ejecutar este proyecto, asegúrate de tener instalado:

- Python 3.10.12

## Instalación

crear entorno virtual(linux):

python3 -m venv env

ingresar entorno virtual(linux):

source env/bin/activate

Para instalar las dependencias del proyecto, ejecuta:

pip install -r requirements.txt

## Uso

Para iniciar el servidor de desarrollo de Django, ejecuta:
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser (seguir las indicaciones) este paso es para poder ingresar al menú administrador de django
python manage.py runserver
La API ahora debería estar accesible en `http://localhost:8000`.

## Endpoints

Aquí se describen algunos de los endpoints principales disponibles en la API:

- **GET /api/productos/**: Obtiene todos los productos.
- **POST /api/productos/**: Crea un nuevo producto.
- **GET /api/categorias/**: Obtiene todas las categorías.
- **POST /api/categorias/**: Crea una nueva categoría.
- **GET /api/ordenes/**: Obtiene todas las órdenes.
- **POST /api/ordenes/**: Crea una nueva orden.
- **GET /api/clientes/**: Obtiene todos los clientes.
- **POST /api/clientes/**: Crea un nuevo cliente.

## Modelos

### Modelo Productos

- **Campos**:
  - `id`: Identificador único del producto.
  - `nombre`: Nombre del producto.
  - `descripcion`: Descripción detallada del producto.
  - `precio`: Precio del producto.
  - `categorias_id`: Relación con el modelo Categorias.

### Modelo Categorias

- **Campos**:
  - `id`: Identificador único de la categoría.
  - `nombre`: Nombre de la categoría.

### Modelo Ordenes

- **Campos**:
  - `id`: Identificador único de la orden.
  - `fecha`: Fecha de la orden.
  - `clientes_id`: Relación con el modelo Clientes.
  - `cantidad`: Cantidad de productos en la orden.
  - `estado`: Estado de la orden (Pendiente, Aprobada, Rechazada).
  - `Productos_id`: Relación con el modelo Productos.

### Modelo Calificación

- **Campos**:
  - `id`: Identificador único de la calificación.
  - `Clientes_id`: Relación con el modelo Clientes.
  - `Productos_id`: Relación con el modelo Productos.
  - `calificacion`: Valor de la calificación.
  - `contenido`: Comentario adicional de la calificación.
  - `fecha`: Fecha de la calificación.

### Modelo Clientes

- **Campos**:
  - `id`: Identificador único del cliente.
  - `nombre`: Nombre del cliente.
  - `direccion`: Dirección del cliente.
  - `correo`: Correo electrónico del cliente.
  - `telefono`: Teléfono del cliente.

## Contribuciones

Las contribuciones son bienvenidas. Por favor, abre un issue o un pull request antes de enviar cualquier cambio.

## Licencia

Este proyecto está licenciado bajo la Licencia MIT.
