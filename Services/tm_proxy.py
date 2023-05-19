import threading
import requests
import time
from Utils.utils import check_proxy

with open('./Data/tmproxy_key.txt', 'r') as f:
    tm_keys = f.read().strip().split('\n')

tm_locker = threading.Lock()

def get_key():
    global tm_keys
    tm_locker.acquire()
    if len(tm_keys) > 0:
        key = tm_keys.pop(0)
    else:
        key = ''
    tm_locker.release()
    return key

def get_with_check(key):
    print('run get proxy')
    while True:
        proxy = get_proxy(key)
        if check_proxy(proxy):
            return proxy
        time.sleep(6)

def get_proxy(key):
    while True:
        headers = {
            'accept': 'application/json',
        }
        json_data = {
            'api_key': key,
        }
        print('get proxy:', key)
        response = requests.post('https://tmproxy.com/api/proxy/get-new-proxy', headers=headers, json=json_data)
        json = response.json()
        print(json)
        proxy = json['data']['https']
        if proxy == '':
            # print('get new proxy:', key)
            # time.sleep(6)
            # continue
            response = requests.post('https://tmproxy.com/api/proxy/get-current-proxy', headers=headers, json=json_data)
            proxy = response.json()['data']['https']
            return proxy
        # save log
        return proxy