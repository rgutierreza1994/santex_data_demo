## INSTALAR Python 3.10+ 
#### https://www.python.org/downloads/release/python-31010/


## Instrucciones
#### Para correr el ETL ejecutar el notebook hasta la celda que indica experimental


## Si se desea probar la parte de base de datos:
- Instalar Docker 
- https://www.docker.com/get-started/ en el boton dowload docker desktop ( Seleccionar su plataforma de CPU )
- En su terminal ejecutar el siguiente comando
  - docker compose up -d

## Si se desea probar la parte de API.
- dentro de la terminal ejecutar:
  - fastapi dev api.py
- Entrar a la siguiente direccion 
  - http://127.0.0.1:8000/docs

  - Ejecutar /get-incoming-age-gender desde swagger y validar que la data sea la misma que la DB