from playwright.sync_api import sync_playwright
from Helpers import multilogin
from time import sleep
import threading
from Helpers import gen_info
from random import randint
from Helpers import dolphin
from Utils.utils import *
DOLPHIN_TOKEN = read_file_helper("./Data/dolphin_anty_token.txt")[0]

options = {"token":DOLPHIN_TOKEN}
profile_name = "dolphin" + str(randint(1,10))
proxy_dict = None
dolphin_browser = dolphin.Dolphin(options)
with sync_playwright() as playwright:
    try:
        proxy = None
        params,profile_data,ua = dolphin_browser.create_new_profile(profile_name,proxy=proxy)
        print("start profile")
        dolphin_start_data = dolphin_browser.start()
        if dolphin_start_data["status"]:
                print("start profile successfully")
                print("Connect Playwright to dolphin profile")
                port = dolphin_start_data["data"]["automation"]["port"]
                wsEndpoint = dolphin_start_data["data"]["automation"]["wsEndpoint"]
                cdp_link = f"ws://127.0.0.1:{port}{wsEndpoint}"
        browser = playwright.chromium.connect_over_cdp(cdp_link)
        context = browser.contexts[0]
        page = context.pages[0]
        for _ in range(1000):
            page.wait_for_timeout(int(1)*1000)
    except Exception as e:
        print("LOL")
    finally:
        try:
            dolphin_browser.stop()
        except:
            pass
        try:
            dolphin_browser.delete_browser_profile()
        except:
            pass