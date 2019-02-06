
import requests
import json
import threading
import time

url = "http://dev.clever-api-fin.local/proxycharge/pendingcharges"
def link ():

    response = requests.get(url)
    print(response.content)
    
while 1:
    for i in range(1001):
        t = threading.Thread(target=link)
        t.start()
    time.sleep(1)