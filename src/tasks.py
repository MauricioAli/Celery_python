from celery_config import app
from celery import shared_task
from scraping import get_data, sql, get_data2


@app.task(bind=True, autoretry_for=(Exception,), retry_kwargs={'max_retries': 10, 'countdown': 2, 'retry_backoff': True})
def get_data_task(self, url):
    a = get_data(url)
    if a == "1000":
        raise Exception("fail")
    return "ok"


@app.task()
def sql_task():

    return sql()
