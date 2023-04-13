from Utils.utils import *
from Utils import constants
from Helpers import gen_info
from Helpers import playwright

def run(page):

    
    page.goto("https://iherb.com/")

    # wait search
    page.wait_for_selector('#txtSearch', state='visible',timeout=30000)
    products = page.query_selector_all('.product-card.product.ga-product')

    # click checkout button
    page.wait_for_selector('.checkout-button', state='visible',timeout=3000).click()

    # click proccess checkout button
    

    page.wait_for_selector('//a[@href="/transactions/checkout"]', state='visible',timeout=3000).click()


    # create account
    page.wait_for_selector('//a[@data-ga-event-label="Create Account"]', state='visible',timeout=3000).click()
    

    # user name
    email = gen_info.get_email()
    password = gen_info.get_password()

    username_input = page.wait_for_selector('#username_input', state='visible',timeout=3000)
    playwright.typing(page,username_input,email)
    

    # password

    password_input = page.wait_for_selector('#password_input', state='visible',timeout=3000)
    playwright.typing(page,password_input,password)

    password_input



    create_account_btn
    username_input