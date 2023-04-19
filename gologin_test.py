import random
import time
import asyncio
from sys import platform
import string
from Helpers import gologin
from playwright.sync_api import sync_playwright
from Utils.utils import *
GOLOGIN_TOKEN = read_file_helper("./Data/gologin_token.txt")[0]





gl = gologin.GoLogin({
    "token": GOLOGIN_TOKEN,
})

proxy = {"type": "http","host": "171.236.82.141","port":"5018","username": "", "password": ""}
profile_id = gl.createStdProfile(proxy)
if profile_id != None:
    gl.setProfileId(profile_id)
    debugger_address = gl.start()
    
    with sync_playwright() as playwright:
        try:
            browser = playwright.chromium.connect_over_cdp("http://" + debugger_address)
            context = browser.contexts[0]
            page = context.pages[0]
            print("DONE")
            for _ in range(1000):
                page.wait_for_timeout(int(1)*1000)
        except Exception as e:
            print("LOL")
    