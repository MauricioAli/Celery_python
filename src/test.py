import requests

try:
    resp = requests.get('http://google.c')
except requests.ConnectionError as c:
    print(c)
