SERVER_URL = "http://103.140.251.212"


OS_SYSTEM = {"Windows": "win","Darwin": "mac","Linux": "linux"}

# CAPTCHA
DEVICE_NAME = "cpu" # ["cpu","gpu"]

IMAP_DICT = {
    "outlook": {
        "server":"outlook.office365.com",
        "port": 993
    }
}

# PATH
CONFIG_PATH = "config.json"
FUNCAPTCHA_CROWD_OF_PEOPLE_AUDIO_PATH = "./Data/Weight/Funcaptcha_Audio/CROWD_OF_PEOPLE_AUDIO.pth"
FUNCAPTHCA_GALAXY_IMAGE_PATH = "./Data/Weight/Funcaptcha_Image/GALAXY.h5"
AUDIO_PROCCESED_PATH = "./Data/Audio_Proccesed"
TEMP_AUDIO_PATH = "./Data/Temp_Audio"
TEMP_IMAGE_PATH = "./Data/Temp_Image"
TEXTNOW_PATH = "./Data/Textnow"
HOTMAIL_PATH = "./Data/Hotmail"


# AMAZON
AMAZON_LIVE_URL = ["https://www.amazon.com/ref=nav_logo","https://www.amazon.com/?ref_=nav_signin&","https://www.amazon.com/?ref_=nav_ya_signin&","https://www.amazon.com/gp/css/homepage.html?ref_=nav_youraccount_btn"]
AMAZON_LOGIN_NON_CAPTCHA_URL = ["https://www.amazon.com/gp/cart/view.html?ref_=nav_cart","https://www.amazon.com/gp/css/homepage.html?ref_=nav_AccountFlyout_ya"]
AMAZON_LOCKED_URL = ["https://www.amazon.com/ap/account-status.amazon.com","https://www.amazon.com/ap/signin?arb=","https://www.amazon.com/ap/forgotpassword?arb="]


APPRVOAL_URL = "https://www.amazon.com/ap/cvf/transactionapproval?arb="

MESSAGES_OTP_DICT = {"AMAZON_GET_OTP": {"target_message":"is your Amazon OTP", "code_len": 6}, 
                    "AMAZON_RESET_PASSWORD": {"target_message":"reset your password","code_len": 6},
                    "AMAZON_2FA_OTP": {"target_message":"is your Amazon OTP","code_len": 6} 
                }


BANED_COUNTRY_LIST = ["India"]

AMAZON_HOMEPAGE_ACCOUNT_URL = "https://www.amazon.com/gp/css/homepage.html?ref_=nav_youraccount_btn"
AMAZON_ADDRESS_URL = "https://www.amazon.com/a/addresses?ref_=ya_d_l_addr"

AMAZON_WALLET_URL = "https://www.amazon.com/cpe/yourpayments/wallet?ref_=ya_d_l_pmt_mpo"
AMAZON_TRANSACTIONS_URL = "https://www.amazon.com/cpe/yourpayments/transactions?ref_=ya_d_l_pmt_mpo"