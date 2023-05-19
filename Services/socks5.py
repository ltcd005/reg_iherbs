from Utils.utils import *
from Utils import constants
import os
import threading
import random

total_proxies = read_file_helper(os.path.join(constants.DATA_PATH,"socks5.txt"))
total_proxies_ = total_proxies.copy()


locker = threading.Lock()
def get_proxy():
    global total_proxies_
    locker.acquire()
    if len(total_proxies_) == 0:
        random.shuffle(total_proxies)
        total_proxies_ = total_proxies.copy()
    proxy = total_proxies_.pop()
    locker.release()
    return proxy