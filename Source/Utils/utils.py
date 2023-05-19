from Utils import constants
import base64
import random
import string
from random import randint
import re
import platform
import requests



def get_platform_system():
    return platform.system()

def check_proxy(proxy):
    try:
        proxies = {
            'http': 'http://' + proxy,
            'https': 'http://' + proxy
        }
        r = requests.get('https://api.ipify.org?format=json', proxies=proxies)
        return 'ip' in r.json().keys()
    except:
        return False


def random_string_helper():
    return ''.join(random.choice(string.ascii_uppercase if randint(0,1) else string.ascii_lowercase + string.digits) for _ in range(randint(10,15)))

def get_number_from_string(s):
    number = "0123456789"
    result = []
    for v in s:
        if v in number:
            result.append(v)
    return "".join(result)

def cleanhtml(raw_html):
    CLEANR = re.compile('<.*?>')
    cleantext = re.sub(CLEANR, '', raw_html)
    return cleantext.replace(",","").replace("\\t","").replace("\\n","").replace("\\r","").strip()

def download_file(filepath,url):
    response = requests.get(url)
    open(filepath, "wb").write(response.content)

import threading

write_file_lock = threading.Lock()

def write_file_helper(file_path,value):
    write_file_lock.acquire()
    f = open(file_path, 'a',encoding="utf-8")
    f.write(value + "\n")
    f.close()
    write_file_lock.release()

    

def read_file_helper(file_path):
    #f = open(file_path, 'r',encoding="utf-8")
    f = open(file_path, 'r',encoding="ISO-8859-1")
    data = [line.strip() for line in f.readlines()]
    f.close()
    return data

def get_cvv(card_number):
    return "1111" if card_number[0] == "3" else "111"
