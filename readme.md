## Requisitos Previos

- Python 3.11 o superior
- pip (gestor de paquetes de Python)
- Google Chrome
- ChromeDriver (asegúrate de que la versión coincida con tu versión de Chrome)
- apache-maven-3.9.8

## Configuración del Entorno

1. Clona este repositorio:

 - git clone <URL_DEL_REPOSITORIO>
 - cd <NOMBRE_DEL_DIRECTORIO>

2. Crea un entorno virtual (opcional, pero recomendado):

 - python -m venv venv
 - source venv/bin/activate  # En Windows usa venv\Scripts\activate

3. Instala las dependencias:

 - python -m venv venv
 - source venv/bin/activate  # En Windows usa venv\Scripts\activate

3. Instala las dependencias:

 - pip install -r requirements.txt

4. Asegúrate de que ChromeDriver esté en tu PATH o especifica su ubicación en `environment.py`.

## Ejecución de las Pruebas

1. Para ejecutar todas las pruebas:

 - mvn test

## Resultados de las Pruebas

- Los logs se guardan en el directorio `logs/` con un timestamp único para cada ejecución.
- Las capturas de pantalla de los pasos fallidos se guardan en el directorio `screenshots/` con el nombre del paso y un timestamp.
- Los resultados de las pruebas se muestran en la consola y se registran en el archivo de log.

## Mantenimiento

- Actualiza `search_page.py` si cambian los selectores o la estructura de la página.
- Modifica `search.feature` para añadir o modificar escenarios de prueba.
- Actualiza `search_step.py` si necesitas cambiar la lógica de los pasos de prueba.

## Contribución

Si deseas contribuir a este proyecto, por favor:

1. Haz un fork del repositorio
2. Crea una nueva rama (`git checkout -b "{ID_Userstory}" - "{Description_Userstory}"`)
3. Haz commit de tus cambios (`git commit -m '{branch_name} - Descripcion de los cambios'`)
4. Push a la rama (`git push`)
5. Abre un Pull Request

## Contacto

Jose Manuel Barroso de la Rosa - barroso.josemanuel94@gmail.com

URL del proyecto: (https://github.com/JoseManuel1994/Alten-Web/)
