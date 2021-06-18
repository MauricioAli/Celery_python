from tasks import get_data_task, sql_task
from scraping import get_data, sql

url = ["http://google.co", "https://amazon.in",
       "https://facebook.com", "https://twitter.com", "https://alexa.com"]


get_data_task.delay(["http://127.0.0.1:8000/"])


for _ in range(0, 10):

    sql_task.delay()


for _ in range(0, 20):
    print("PROCESO2")
