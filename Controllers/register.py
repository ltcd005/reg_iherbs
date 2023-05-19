from Utils.utils import *
from Utils import constants
from Helpers import gen_info
from Helpers import playwright

def create_account(page,email,password):
    try:
        username_input = page.wait_for_selector('#username_input', state='visible',timeout=3000)
        username_input.fill("")
        playwright.typing(page,username_input,email)
        
        password_input = page.wait_for_selector('#password_input', state='visible',timeout=3000)
        password_input.fill("")
        playwright.typing(page,password_input,password)
        page.wait_for_timeout(randint(1,3)*1000)
        page.wait_for_selector('#create_account_btn', state='visible',timeout=3000).click()
        
        for _ in range(60):
            try:
                error_message = page.wait_for_selector('.s-form-error-message-container ', state='visible',timeout=1000).text_content()
                if "Google reCAPTCHA" in error_message:
                    return "Captcha failed"
            except Exception as e:
                print("Cannot find captcha")
                
            try:
                if playwright.wait_for_url_helper(page,"transactions",1):
                    return "Success"
            except:
                pass
        return "Failed"
    except:
        return "Captcha failed"

def run(page,state):
    for _ in range(3):
        try:
            page.goto("https://iherb.com/",timeout=120000)
            # wait search
            page.wait_for_selector('#txtSearch', state='visible',timeout=30000)
            products = page.query_selector_all('.product-card.product.ga-product')
            products[randint(0,5)].click()
            # click checkout button
            page.wait_for_selector('.checkout-button', state='visible',timeout=20000).click()
            page.wait_for_timeout(randint(1,3)*1000)
            # click proccess checkout button
            

            page.wait_for_selector('//a[@href="/transactions/checkout"]', state='visible',timeout=20000).click()
            page.wait_for_timeout(randint(1,3)*1000)

            # create account
            page.wait_for_selector('//a[@data-ga-event-label="Create Account"]', state='visible',timeout=20000).click()
            email = gen_info.gen_mail()
            password = gen_info.get_password()
            state["email"] = email
            state["password"] = password
            for _ in range(3):
                
                result = create_account(page,email,password)
                print("Result: ",result)
                if result == "Success":
                    return True,state
                elif result == "Failed":
                    return False,state
                elif result == "Captcha failed":
                    page.reload()
                    page.wait_for_selector('#username_input', state='visible',timeout=30000)
                    page.wait_for_timeout(randint(2,5)*1000)
            return False,state
        except Exception as e:
            print("Register Error: ",e)
    return False,state



    