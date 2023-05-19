from Models import proxy_manager
from Utils.utils import *
from playwright.sync_api import sync_playwright
from Helpers import multilogin
from time import sleep
import threading
from Services import mobiehop_proxy,shifter_proxy,shoplike_proxy,tinsoft_proxy,tm_proxy,lunaproxy
from Controllers import register,set_address,check_fish
from Helpers import gologin
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

GOLOGIN_TOKEN = read_file_helper("./Data/gologin_token.txt")[0]


PROXIES_SITE = ["luna","shoplike","tmproxy","socks5","none"]
BROWSER_APPS = ["gologin","multilogin"]


def select_browser_apps(index,browser_app,proxy_dict):
    if browser_app == "multilogin":
        br = multilogin.MultiLogin()
        br.create_profile(proxy=proxy_dict)
        cdp_link = br.start_profile(True)
    elif browser_app == "gologin":
        br = gologin.GoLogin({
            "token": GOLOGIN_TOKEN,
            "port": 3500 + index
        })
        profile_id = br.createStdProfile(proxy_dict)
        print("profile_id :",profile_id)
        if profile_id != None:
            br.setProfileId(profile_id)
            for _ in range(5):
                try:
                    debugger_address = br.start()
                    print("debugger_address: ",debugger_address)
                    break
                except Exception as e:
                    print("Gologin Error: ",e)
            cdp_link = "http://" + debugger_address

    return br,cdp_link
def stop_and_delete_browser_apps(br,browser_app):
    try:
        if browser_app == "multilogin":
            br.stop_profile()
            br.delete_profile()
        elif browser_app == "gologin":
            br.stop()
            br.delete(br.profile_id)
    except:
        pass

IS_OUT_OF_DATA = False
def run(index,options):
    global IS_OUT_OF_DATA
    proxy_site = options.get('proxy_site')
    browser_app = options.get('browser_app')
    is_add_address = options.get('is_add_address')
    number_success = options.get('number_success')
    if proxy_site == "shoplike" or proxy_site == "tmproxy":
        proxy_key = shoplike_proxy.get_key() if proxy_site == "shoplike" else tm_proxy.get_key()
    else:
        proxy_key = None
    

    while True:
        if IS_OUT_OF_DATA:
            break
        state = {"is_out_of_data": False, "number_success": number_success}
        proxy_dict = proxy_manager.get_proxy(proxy_site=proxy_site,key=proxy_key,browser_app=browser_app)
        with sync_playwright() as plwt:
            try:
                br,cdp_link = select_browser_apps(index,browser_app=browser_app,proxy_dict=proxy_dict)
                debugger_address = cdp_link.split('http://')[-1]
                #print(debugger_address)
                browser = plwt.chromium.connect_over_cdp(cdp_link)
                context = browser.contexts[0]
                page = context.pages[0]
                #page.wait_for_timeout(5000)
                is_register,state = register.run(page,state)
                if is_register:
                    if is_add_address:
                        is_set_address,state = set_address.run(page,state)
                        if is_set_address:
                            is_check_fish,state = check_fish.run(page,state)
                        
                    print(state)
                browser.close()
                
            except Exception as e:
                print(e)
                print("LOL")
            finally:
                if state["is_out_of_data"]:
                    IS_OUT_OF_DATA = True
                if browser_app == "gologin":
                    try:
                        chrome_options = Options()
                        chrome_options.add_experimental_option("debuggerAddress", debugger_address)
                        driver = webdriver.Chrome(options=chrome_options)
                        driver.close()
                    except:
                        pass
                try:
                    stop_and_delete_browser_apps(br,browser_app)
                except:
                    pass

if __name__ == '__main__':
    n_thread = int(input('Nhập số luồng : '))
    number_success = int(input('Nhập số lượt check mỗi lần check : '))
    print("Proxy site: [1] -> 'lunaproxy', [2] -> 'shoplikeproxy', [3] -> 'tmproxy', [4] -> 'socks5',[5] -> 'None proxy'")
    proxy_index = int(input('Nhập số ở trên để chọn proxy: '))
    proxy_site = PROXIES_SITE[proxy_index - 1]
    print("Browser App: [1] -> 'Gologin', [2] -> 'Multilogin'")
    browser_index = int(input('Nhập số ở trên để chọn browser app: '))
    browser_app = BROWSER_APPS[browser_index - 1]
    #print("Add Address: [1] -> 'No', [2] -> 'Yes'")
    is_add_address = True#int(input('Enter number to add address: ')) == 2
    options = {"browser_index": browser_index,"browser_app": browser_app,"is_add_address": is_add_address,"proxy_site": proxy_site,"number_success": number_success}

    threads = []
    for index in range(n_thread):
        thread = threading.Thread(target=run,args=(index,options))
        threads.append(thread)
    for thread in threads:
        thread.setDaemon(True)
    for thread in threads:
        thread.start()
        sleep(1)
    for thread in threads:
        thread.join()
    input('Enter <ENTER> to exit.')