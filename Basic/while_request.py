
import requests
import json
import threading
import time

url = "http://10.8.17.26:23"
def link ():

    response = requests.get(url)
    print(response)

while 1:
    for i in range(1001):
        t = threading.Thread(target=link)
        t.start()
        print(url)
        time.sleep(1)
