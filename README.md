# Celery_python

Para correr este ejemplo de como ocupar tareas asincronas con python usando celery + redis es necesario levantar un contenedor con redis.
# 1 Levantamos un contenedor con redis 
````
docker run -p 6379:6379 --name python-redis -d redis
````
# 2 Copiamos y creamos el entorno virtual

````
git clone https://github.com/MauricioAli/Celery_python
cd Celery_python
python3.8 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

````
## Nota: para poder visualizar todo estos comandos debe correrlos en 2 terminales separadas con el entorno virtual del      proyecto iniciado

# 3 Activamos el worker
````
cd src
celery worker -A celery_config --loglevel=info
````
# 4 Activamos la interfaz grafica para ver las tareas
````
flower -A celery_config --port=5555
````
