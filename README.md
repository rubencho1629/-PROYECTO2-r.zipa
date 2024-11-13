# Proyecto Heladería

Este proyecto es una aplicación de gestión de una heladería construida con Flask y SQLAlchemy. La aplicación permite manejar productos e ingredientes, realizar ventas y calcular rentabilidad, y se conecta a una base de datos MySQL para el almacenamiento de datos.

## Tabla de Contenidos
- [Instalación](#instalación)
- [Configuración](#configuración)
- [Ejecución](#ejecución)
- [Estructura del Proyecto](#estructura-del-proyecto)
- [Uso](#uso)
- [Dependencias](#dependencias)
- [Contribuciones](#contribuciones)
- [Licencia](#licencia)

## Instalación

1. Clona este repositorio:

    ```bash
    git clone https://github.com/tu-usuario/proyecto-heladeria.git
    cd proyecto-heladeria
    ```

2. Crea y activa un entorno virtual (recomendado):

    ```bash
    python -m venv .venv
    source .venv/bin/activate  # En Windows: .venv\Scripts\activate
    ```

3. Instala las dependencias:

    ```bash
    pip install -r requirements.txt
    ```

## Configuración

1. Crea un archivo `.env` en la raíz del proyecto con las siguientes variables de entorno para configurar la conexión a la base de datos MySQL:

    ```plaintext
    USER_DB=tu_usuario
    PASS_DB=tu_contraseña
    URL_DB=localhost
    NAME_DB=heladeria
    ```

2. Configura otros detalles de la aplicación en el archivo `config.py` si es necesario.

## Ejecución

1. Inicializa la base de datos (asegúrate de que MySQL esté en ejecución):

    ```python
    from app import db
    db.create_all()
    ```

2. Ejecuta la aplicación:

    ```bash
    flask run
    ```

3. Accede a la aplicación en tu navegador en `http://127.0.0.1:5000/heladeria/page`.

## Estructura del Proyecto

```plaintext
proyecto-heladeria/
│
├── app/
│   ├── controllers/        # Controladores de la aplicación (lógica de negocio)
│   ├── models/             # Modelos de datos de SQLAlchemy
│   ├── services/           # Servicios adicionales y lógica de negocio
│   ├── static/             # Archivos estáticos (CSS, JS)
│   └── templates/          # Plantillas HTML de la aplicación
│
├── .env                    # Archivo de configuración de variables de entorno
├── .gitignore              # Archivos y carpetas ignorados en git
├── app.py                  # Punto de entrada principal de la aplicación Flask
├── config.py               # Configuración de la aplicación y base de datos
└── requirements.txt        # Lista de dependencias del proyecto
