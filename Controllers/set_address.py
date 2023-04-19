from Utils.utils import *
from Utils import constants
from Helpers import gen_info
from Helpers import playwright,fake_address


def run(page,state):
    
    full_name = gen_info.gen_full_name()
    state["full_name"] = full_name
    page.wait_for_selector('#FirstName', state='visible',timeout=30000).fill(full_name)
    

    address = fake_address.get_fake_address()
    page.wait_for_timeout(randint(1,3)*1000)
    state["address"] = "|".join(address[1:])
    
    for _ in range(5):
        try:
            # select the country
            page.wait_for_selector('#select-address-country', state='visible',timeout=5000).click()
            page.wait_for_selector('//div[@data-val="US"]', state='visible',timeout=5000).click()
            page.wait_for_timeout(randint(4,8)*1000)
            break
        except Exception as e:
            print("Select country failed :",e)
    else:
        return
    page.wait_for_timeout(randint(2,3)*1000)
    page.wait_for_selector('#AddressLine1', state='visible',timeout=3000).fill(address[1])
    page.wait_for_timeout(randint(2,3)*1000)
    page.wait_for_selector('#City', state='visible',timeout=5000).fill(address[2])
    page.wait_for_timeout(1000)
    short_state = address[3].split("(")[-1].split(")")[0]

    page.wait_for_selector('#RegionName', state='visible',timeout=3000).select_option(short_state)
    page.wait_for_timeout(1000)
    page.wait_for_selector('#PostalCode', state='visible',timeout=3000).fill(address[-1])
    phone_number = gen_info.gen_phone()
    state["phone_number"] = phone_number
    page.wait_for_timeout(1000)
    page.wait_for_selector('#TelNumber', state='visible',timeout=3000).fill(phone_number)
    page.wait_for_timeout(1000)
    page.wait_for_selector('//*[@name="addrsave"]', state='visible',timeout=10000).click()

    for _ in range(10):
        try:
            page.wait_for_selector('//button[@data-mdc-dialog-action="accept"]', state='visible',timeout=1000).click()
        except:
            pass
        try:
            if playwright.wait_for_url_helper(page,"scd?correlationId=",30):
                return True,state
        except:
            pass
    return False,state
    # correlationId

