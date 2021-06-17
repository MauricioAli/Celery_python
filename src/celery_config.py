from celery import Celery


app = Celery('celery_config', broker='redis://172.17.0.1:6379/0',
             include=['tasks'])
