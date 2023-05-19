import threading
from Utils.utils import *
ccn_locker = threading.Lock()

def get():
    ccn_locker.acquire()
    ccn_data = read_file_helper("./Data/Card/cc_data.txt")
    try:
        ccn_data_used = read_file_helper("./Data/Card/cc_data_used.txt")
    except:
        ccn_data_used = []
    for value in ccn_data:
        if not value in ccn_data_used:
            write_file_helper("./Data/Card/cc_data_used.txt",value)
            value_split = value.split("|")
            ccn_locker.release()
            return value_split[0],value_split[1],value_split[2]
    ccn_locker.release()
    return "None","None","None"

