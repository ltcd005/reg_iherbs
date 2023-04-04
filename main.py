from playwright.sync_api import sync_playwright
from Helpers import multilogin
from time import sleep
import threading

proxy_dict = None
with sync_playwright() as playwright:
    multilogin_browser = multilogin.MultiLogin()
    multilogin_browser.create_profile(proxy=proxy_dict)
    cdp_link =multilogin_browser.start_profile(True)
    browser = playwright.chromium.connect_over_cdp(cdp_link)
    context = browser.contexts[0]
    page = context.pages[0]
    for _ in range(1000):
        page.wait_for_timeout(int(1)*1000)