#  

from Utils.utils import *
from Utils import constants
from Helpers import gen_info
from Helpers import playwright,get_fish

def select_address(page):
    page.wait_for_selector('#select-a-shipping-address-header', state='visible',timeout=10000)
    label_elements = page.query_selector_all('label')
    is_select_address_radio = False
    for label_element in label_elements:
        id_ = label_element.get_attribute('id')
        if "address-radio" in id_:
            label_element.click()
            is_select_address_radio = True
            break
    if is_select_address_radio:
        for _ in range(10):
            try:
                label_element.wait_for_selector("button",state='visible',timeout=1000).click()
                return True
            except Exception as e:
                print("Select address click button error: " + str(e))
        else:
            return False

def check_card(page):
    for index in range(10):
        if index >= 5:
            try:
                page.wait_for_selector('#add-payment-continue-button-CreditCard', state='visible',timeout=1000)
                return "card_die"
            except:
                print("Cannot find card die")
        try:
            page.wait_for_selector('//div[@data-testid="credit-card-panel"]', state='visible',timeout=1000).text_content()
            return "card_live"
        except:
            print("Cannot find card live")
    return "card_die"


def delete_card(page):
    page.wait_for_selector('#payment-method-toggle-button', state='visible',timeout=10000).click()
    page.wait_for_selector('#payment-delete-button', state='visible',timeout=10000).click()
    page.wait_for_selector('#delete-payment-modal-remove-button', state='visible',timeout=10000).click()



def set_card_number(page,card_number):
    iframe_selector = page.wait_for_selector('//*[@title="Iframe for secured card number"]', state='visible',timeout=10000)
    iframe = iframe_selector.content_frame()
    # get card number
    iframe.wait_for_selector("#encryptedCardNumber").fill(card_number)


def set_expiry_date(page,date):
    iframe_selector = page.wait_for_selector('//*[@title="Iframe for secured card expiry date"]', state='visible',timeout=10000)
    iframe = iframe_selector.content_frame()
    # get card number
    iframe.wait_for_selector("#encryptedExpiryDate").fill(date)


def set_cvv(page,cvv):
    iframe_selector = page.wait_for_selector('//*[@title="Iframe for secured card security code"]', state='visible',timeout=10000)
    iframe = iframe_selector.content_frame()
    # get card number
    iframe.wait_for_selector("#encryptedSecurityCode").fill(cvv)




def run(page,state):
    # waite shipping address
    is_select_address = select_address(page)
    count_success = 0
    if is_select_address:
        for _ in range(10000):
            if count_success >= state["number_success"]:
                return "Success",state
                

            page.wait_for_selector('#add-payment-radio-CreditCard', state='visible',timeout=20000)
            # waite add payment frame
            card_number, month, year = get_fish.get()
            if card_number == "None":
                state["is_out_of_data"] = True
                return "Sucesss",state
            month = "0" + month
            month = month[-2:]
            date = f'{month[-2:]}/{year[-2:]}'
            cvv = "111"
            
            page.wait_for_selector('//input[@value="saveCreditCard"]', state='visible',timeout=10000).click()
            set_card_number(page,card_number)
            set_expiry_date(page,date)
            set_cvv(page,cvv)
            page.wait_for_timeout(1000)
            page.wait_for_selector('#add-payment-continue-button-CreditCard', state='visible',timeout=10000).click()
            count_success += 1
            result_check_card = check_card(page)
            if result_check_card == "card_live":
                write_file_helper("./Data/Card/cc_live.txt",f"{card_number}|{month}|{year}")
                page.wait_for_timeout(1000)
                delete_card(page)
            elif result_check_card == "card_die":
                write_file_helper("./Data/Card/cc_die.txt",f"{card_number}|{month}|{year}")
            elif result_check_card == "card_unknow":
                write_file_helper("./Data/Card/cc_unknow.txt",f"{card_number}|{month}|{year}")

        


        



