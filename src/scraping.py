import requests
import time


def get_data(urls: list) -> str:

    for url in urls:
        resp = requests.get(url)
        return resp.status_code


def sql():
    time.sleep(1)
    return "delay"
