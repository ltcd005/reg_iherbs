import requests
from Utils.utils import *
from Utils import constants
import os
import random

FIRST_NAMES =  read_file_helper(os.path.join(constants.NAME_PATH,"first_names.txt"))
LAST_NAMES =  read_file_helper(os.path.join(constants.NAME_PATH,"last_names.txt"))




def gen_mail():
    domains = ["@hotmail.com","@outlook.com","@gmail.com"]
    first_name = random.choice(FIRST_NAMES)
    last_name = random.choice(LAST_NAMES)
    domain = random.choice(domains)
    email = first_name + last_name + str(random.randint(10,10000)) + domain if randint(0,1) else last_name + first_name + str(random.randint(10,10000)) + domain
    return email.lower()

def get_password():
    return random_string_helper()

def gen_phone():
    pass

def gen_address():
    pass
