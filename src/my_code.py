from tasks import get_data_task, sql_task


url = ["http://google.com", "https://amazon.in",
       "https://facebook.com", "https://twitter.com", "https://alexa.com"]


get_data_task.delay(url)

for _ in range(0, 100):

    sql_task.delay()


for _ in range(0, 20):
    print("PROCESO2")
