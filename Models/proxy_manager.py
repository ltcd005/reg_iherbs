from Services import mobiehop_proxy,shifter_proxy,shoplike_proxy,tinsoft_proxy,tm_proxy,lunaproxy

def get_proxy(proxy_site = "luna",key=None,browser_app="multilogin"):
    proxy_dict = {"type":"","host": "", "port": "", "username": "", "password": ""}
    if proxy_site  == "luna":
        proxy = lunaproxy.get_proxy()
        proxy_dict["type"] = "SOCKS" if browser_app == "multilogin" else "http"
    elif proxy_site == "shoplike":
        proxy = shoplike_proxy.get_with_check(key)
        proxy_dict["type"] = "HTTP" if browser_app == "multilogin" else "http"
    elif proxy_site == "tmproxy":
        proxy = tm_proxy.get_with_check(key)
        proxy_dict["type"] = "HTTP" if browser_app == "multilogin" else "http"

    host = proxy.split(":")[0]
    port = proxy.split(":")[1]
    proxy_dict["host"] = host
    proxy_dict["port"] = port
    print()
    return proxy_dict
        

    