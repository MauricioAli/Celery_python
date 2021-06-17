from celery_config import app
from scraping import get_data, sql


@app.task()
def get_data_task(url):

    return get_data(url)


@app.task()
def sql_task():

    return sql()
