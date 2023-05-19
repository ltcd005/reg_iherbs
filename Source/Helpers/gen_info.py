import requests
from Utils.utils import *
from Utils import constants
import os
import random

FIRST_NAMES =  read_file_helper(os.path.join(constants.NAME_PATH,"first_names.txt"))
LAST_NAMES =  read_file_helper(os.path.join(constants.NAME_PATH,"last_names.txt"))

def gen_full_name():
    first_name = random.choice(FIRST_NAMES)
    last_name = random.choice(LAST_NAMES)
    return first_name + " " + last_name


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
    head_phones = ["631","607","507","609","865","702","406","270"]
    return random.choice(head_phones) + str(random.randint(1000000,9999999))

def gen_address():
    pass
