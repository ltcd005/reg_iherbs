from playwright.sync_api import sync_playwright
from Helpers import multilogin
from time import sleep
import threading
from Helpers import gen_info
from Controllers import register,set_address
from Helpers import playwright,fake_address
from Models import proxy_manager
from Utils.utils import *


proxy_dict = None #proxy_manager.get_proxy()
with sync_playwright() as plwt:
    state = {}
    try:
        multilogin_browser = multilogin.MultiLogin()
        multilogin_browser.create_profile(proxy=proxy_dict)
        cdp_link =multilogin_browser.start_profile(True)
        browser = plwt.chromium.connect_over_cdp(cdp_link)
        context = browser.contexts[0]
        page = context.pages[0]
        is_register,state = register.run(page,state)
        if is_register:
            is_set_address,state = set_address.run(page,state)
            if is_set_address:
                print(state)
                write_file_helper(f"Account_REGISTERED.txt",f"{state['email']}|{state['password']}|{state['full_name']}|{state['address']}|{state['phone_number']}")
            else:
                write_file_helper(f"Account_REGISTERED.txt",f"{state['email']}|{state['password']}")
    except Exception as e:
        print(e)
        print("LOL")
    finally:
        multilogin_browser.stop_profile()
        multilogin_browser.delete_profile()

        print("LOL")
        