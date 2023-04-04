import requests
import threading
import time
from Helpers import check_proxy

with open('./Data/shoplikeproxy_key.txt', 'r') as f:
    keys = f.read().strip().split('\n')

locker = threading.Lock()

def get_key():
    global keys
    locker.acquire()
    if len(keys) > 0:
        key = keys.pop(0)
    else:
        key = ''
    locker.release()
    return key


def get(key,new=False):
    while True:
        r = requests.get(f'http://proxy.shoplike.vn/Api/getNewProxy?access_token={key}')
        # print(r.json())
        if r.json()['status'] == 'success':
            return r.json()['data']['proxy']
        if r.json()['mess'] == 'Key khong ton tai hoac da het han':
            return False
        if r.json()['status'] == 'error' and not new:
            r = requests.get(f'http://proxy.shoplike.vn/Api/getCurrentProxy?access_token={key}')
            if r.json()['status'] == 'success':
                return r.json()['data']['proxy']
            else:
                return False
        print('[INFO] waiting for get new proxy')
        time.sleep(7)

def get_with_check(key,new=False):
    while True:
        proxy = get(key,new)
        if isinstance(proxy, bool):
            return proxy
        if check_proxy.check(proxy):
            return proxy
        print('[ERORR] proxy can be used, trying to get new proxy')
        time.sleep(7)
