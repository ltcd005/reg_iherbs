from Utils.utils import *
import requests


def get_fake_address(service="bestrandom",timeout=10):
    for _ in range(timeout):
        if service == "bestrandom":
            # get fake address from bestrandoms
            r = requests.get("https://www.bestrandoms.com/random-address")
            t = str(r.content).split("World Address Generator")[-1]
            address_info = [ cleanhtml(t) for t in t.split("<span>")[1:6]]
            if  len(address_info) > 0:
                return address_info
        else:
            # get fake address from server
            pass
    return []