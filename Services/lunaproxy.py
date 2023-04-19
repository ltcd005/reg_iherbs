from Utils.utils import *
from Utils import constants
import os
import threading

LUNA_API_LINK = read_file_helper(os.path.join(constants.DATA_PATH,"luna_api_link.txt"))[0]

def get_new_proxy():
    r = requests.get(LUNA_API_LINK)
    if r.status_code == 200:
        return [v.strip() for v in r.text.split("\n")[:-1]]
    return []
        

total_proxies = get_new_proxy()
locker = threading.Lock()
def get_proxy():
    global total_proxies
    print("Total proxies: ",total_proxies)
    locker.acquire()
    if len(total_proxies) == 0:
        total_proxies = get_new_proxy()
    proxy = total_proxies.pop()
    locker.release()
    return proxy



