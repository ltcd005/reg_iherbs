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

def check(proxy):
    try:
        proxies = {
            'http': 'http://' + proxy,
            'https': 'http://' + proxy
        }
        r = requests.get('https://api.ipify.org?format=json', proxies=proxies)
        return 'ip' in r.json().keys()
    except:
        return False

def is_gmail_live(email):
    url = "https://mmo69.com/_check_live_email/api.php?email={}".format(email)
    headers = {
        "cookie": "ga=GA1.2.1468552017.1678631716; __gads=ID=dca8affd33542af9-2278a697f5db0001:T=1678631714:RT=1678631714:S=ALNI_Ma8362NPSS8aRZtgr8bVb4_FZuxyw; __gpi=UID=00000bd7d458b8d9:T=1678631714:RT=1679370522:S=ALNI_MZGEUsMpjNs4OfvjoTocUg2mqr7tg; PHPSESSID=a647s6lsnnnvj9d4vhlu80edho; _gid=GA1.2.637710615.1680443002; _gat_gtag_UA_107077881_1=1",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36",
        "Referer": "https://mmo69.com/_check_live_email/index.php"
    }
    r = requests.get(url=url, headers=headers)
    return "LIVE" in r.text



def is_exist_amazon_account(value,is_email=True):
    url = "https://www.amazon.com/ap/signin"
    payload = {
        "appActionToken":"9CNsOwzGTIG7mYj2FgGDPOF92ZVp4j3D",
        "appAction":"SIGNIN_PWD_COLLECT",
        "subPageType":"SignInClaimCollect",
        "openid.return_to":"ape:aHR0cHM6Ly93d3cuYW1hem9uLmNvbS8/cmVmXz1uYXZfc2lnbmlu",
        "prevRID":"ape:N0tBM1haS0dCWVZaUkVYWlZWSDg=",
        "workflowState":"eyJ6aXAiOiJERUYiLCJlbmMiOiJBMjU2R0NNIiwiYWxnIjoiQTI1NktXIn0.C1lbUsPQEuINAXirnle9SRzsOOAZu9mSVKRw2J9DuIfjtesD-23VZg.7OGua85x6DM0OouF.qbty5sozZznLQVkW_WvpqPsPSuTgOXpciPL5u31KYtOnGcqF321z0kIhHDI3sCATf9Iwo1iyKN6hhGaXwd1lwDKJLo2h6GFMnfMakMrn5Ve9tyYSO0l7TM7tChMATG2mBjkNG97ejR4i4VVgA3Zy7B8VzfxbTCPIjJZs7XRcjQmcj539eLHSXX6pCyHeD13_pRHGTUtm9SALRx8ljuu71_smqVBVqjtcNm8JGjuIO9goAmvdqj0uPNHmdosavLhcx0933nILBNgmL1brrgbdV_UkU71n3JICZ6q71Dys-hTNIs4yKASgs6BTjp-RZK01kj3u._Zva4wsuJsYfvu2KSgPl2Q",
        "email":f"{value}" if is_email else f"+1{value}",
        "password":"",
        "create":"0",
        "metadata1":"ECdITeCs:aZasVCE3k8e2/FnEdwuqC7aGqFmwiDdSldcyYPUo8lt1IPLldccNmlRDuNpG2DyBGh6kdC+6cDouakHGH1/5X1HzAZ8iTKvT0/Ip0g3tiPgFwZUy5VqAdMBUsmrRt5hMozhT7Cgs9UAeHmAcFLUp0qrlSVypOQvsZ10AGYGslMkGsUe6m4sHxj3vJRf3UQQ0aqAm1+UM/BDam6GaU7Ua8mvO9KjZkFGFT09F0axxXJb1vf2Sixi0iP/dSp+w/a6+PCj/5rKdsp+2TR+cEFb6Mox/y7GCacUF0P6RE3ILA3/mA+GzLKBrbSRHH93PtX7N0cyx2H7J0gNWh/wtTo6+pqY9EKxYh2fkHQcKYmvTfAPIkcVhCvaSpRE0uzAI4ng/zpv4dk3LhKmKCEVjW4ah719syq0DO20dXgEgpybiCoI6GfH2/VDDVDVbGUfIPr7SAfw4QEwDzTJsdhbp+cuNRp5LhPIGrE3U4aN1QflpOiNH87DomjQ57P…Dx7fb71Sk+/5x63AweZsmfpgC1zF6UVxM/qGjWF09Em5CTpW1yZtGySw8Atk1tX2c8jNAJ9FC7Q0lQicB8ah0TSdb6xFCpvlbdwjiaFQF1+xGN173FQpgDjLRiaCzJfQIkebgLzy6TPaTQ0wgG34RJWKsR+g1g4K1YNR22bOdwUVXNKWSdR8COsRf8T0cJ0kGOrjxCzG978zs++bEelY/yuA/3A20vG0YRb02i3i62S4LHSKK3aXgDaM3pExo/le33oFA7000ykRDspjKkfNyHDyiPS/IyNLxQuW7+cThtb4d35UUNKAE6AkpZxWihRTKPBmUxX6ntie+r6p9H9A8LAynACMFFKLTESzrWFNuHYu6qnI8jPsHOIpe0i91mBMaioimKVcTqrJv8jvIdB/rlRT14cNdUVmn8OpnmEFdOfTJLmovxAA6QLRo49zD4pFDKxFJeMUvTcMTZ3y61b3zOJpL1q3CnItUBRJ35f8Qg/rBiE/dxT0BYZIesKg=="
    }

    headers = {
        "Host": "www.amazon.com",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:96.0) Gecko/20100101 Firefox/96.0",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
        "Accept-Language": "en-US,en;q=0.5",
        "Accept-Encoding": "gzip, deflate, br",
        "Content-Type": "application/x-www-form-urlencoded",
        "Content-Length": "9382",
        "Origin": "https://www.amazon.com",
        "DNT": "1",
        "Connection": "keep-alive",
        "Referer": "https://www.amazon.com/ap/signin?openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.com%2F%3Fref_%3Dnav_signin&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=usflex&openid.mode=checkid_setup&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0&",
        "Cookie": 'session-id=144-5622164-4674153; session-id-time=2274713856l; i18n-prefs=USD; sp-cdn="L5Z9:VN"; skin=noskin; csm-hit=tb:B7266FDCACJPYJWEMPK6+s-7KA3XZKGBYVZREXZVVH8|1643993862911&t:1643993862911&adb:adblk_no; ubid-main=135-7170776-6706308; session-token=Ur/ZB9rCxaZYThob47XRhIzGid1HsBWT/qd7UBkvQPOch/qCMO1LfIkCVE7dZ6pSxdPGn1u686qEh3nMLip2FMkz7EwUUdIuRjMe2j19OqVUqMd2K2mRUcRXzwXgdsDMgFQvFfqw+jtwr2UESCCbBp74emdiXb0xcYsQrygryShWwyVb4ET+wAtMYDfW+zyB',
        "Upgrade-Insecure-Requests": "1",
        "Sec-Fetch-Dest": "document",
        "Sec-Fetch-Mode": "navigate",
        "Sec-Fetch-Site": "same-origin",
        "Sec-Fetch-User": "?1",
        "TE": "trailers"
    }
    
    r = requests.post(url,headers=headers,data=payload)
    if r.status_code == 200:
        text = r.text
        if "Password" in text:
            print("Exist",value)
            return True
        elif "Incorrect" in text:
            print("KHONG",value)
            return False
    print("Not exist",value)
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
