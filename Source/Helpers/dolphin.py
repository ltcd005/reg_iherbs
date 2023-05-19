import requests
from random import randint
import json
from Utils import constants 



class Dolphin:
    def __init__(self,options):
        self.__username = options.get('username')
        self.__password = options.get('password')
        self.__token = options.get('token')
        self.profile_id = options.get('profile_id')
        self.__dolphin_anty_base_url = constants.DOLPHIN_ANTI_BASE_URL
        self.__dolphin_anty_automation_base_url = constants.DOLPHIN_ANTI_AUTOMATION_BASE_URL
    
    def get_dolphin_api_token(self):
        if self.__token != None:
            payload = {
                "username": self.__username,
                "password": self.__password
            }
            r = requests.post(self.__dolphin_anty_base_url + "/auth/login",data=payload)
            if r.status_code == 200:
                self.__token = r.json()["token"]
        return self.__token

    def start(self,profile_id = None):
        profile = self.profile_id if profile_id == None else profile_id
        start_automation_dolphin_browser_profiles_url = f"{self.__dolphin_anty_automation_base_url}/{profile}/start?automation=1"
        r = requests.get(start_automation_dolphin_browser_profiles_url)
        if r.status_code == 200:
            return {"status": True, "data": r.json()}
        return {"status": False, "data": {"success": False}}
    
    def stop(self,profile_id = None):
        profile = self.profile_id if profile_id == None else profile_id
        stop_automation_dolphin_browser_profiles_url = f"{self.__dolphin_anty_automation_base_url}/{profile}/stop"
        r = requests.get(stop_automation_dolphin_browser_profiles_url)
        if r.status_code == 200:
            return {"status": True, "data": r.json()}
        return {"status": False, "data": {"success": False}}


    def get_username(self):
        return self.__username

    def set_username(self,username):
        self.__username = username

    def get_password(self):
        return self.__password

    def set_password(self,password):
        self.__password = password

    def set_dolphin_api_token(self,token):
        self.__token = token

    def execute_request(self,url,method,params,is_payload = False):
        if self.__token == None:
            self.get_dolphin_api_token()
        headers = {
            'Content-Type': 'application/json',
            "Authorization": f"Bearer {self.__token}"
        }
        
        r = requests.request(method,url=f"{self.__dolphin_anty_base_url}/{url}",params=params,headers=headers) if not is_payload else requests.request(method,url=f"{self.__dolphin_anty_base_url}/{url}",data=params,headers=headers)
        #print(r.json())
        if r.status_code == 200:
            return {"status": True, "data": r.json()}
        return {"status": False, "data": None}

    def get_new_useragent(self,platform = "macos",browser_version = "97",browser_type = "anty"):
        params = {
            "browser_type": browser_type,
            "browser_version": browser_version,
            "platform": platform
        }
        res = self.execute_request(url = "fingerprints/useragent",method = "GET",params = params)
        if res["status"]:
            return res["data"]["data"]
        return None

    def get_new_fingerprint(self,platform = "macos",browser_version = "97",browser_type = "anty"):
        params = {
            "browser_type": browser_type,
            "browser_version": browser_version,
            "platform": platform
        }
        res = self.execute_request(url = "fingerprints/fingerprint",method = "GET",params = params)
        if res["status"]:
            return res["data"]
        return None

    def update_profile(self,profile_id = None,proxy = {"type":None,"host":None,"port":None}):
        profile = self.profile_id if profile_id == None else profile_id
        params = {}
        params["proxy[type]"] = proxy["type"]
        params["proxy[host]"] = proxy["host"]
        params["proxy[port]"] = proxy["port"]
        if "login" in proxy.keys():
            if proxy["login"] != None:
                params["proxy[login]"] = proxy["login"]
                params["proxy[password]"] = proxy["password"]
        return self.execute_request(url = f"browser_profiles/{profile}", method="PATCH", params=params)

    def delete_browser_profile(self,profile_id = None):
        profile = self.profile_id if profile_id == None else profile_id
        params = {}
        return self.execute_request(url = f"browser_profiles/{profile}", method="DELETE", params=params)

    def get_browser_profiles(self,profile_id = None):
        profile = self.profile_id if profile_id == None else profile_id
        params = {}
        return self.execute_request(url = "browser_profiles" if profile == None else f"browser_profiles/{profile}" ,method = "GET",params=params)


    def import_cookies(self,profile_id,cookie):
        profile = self.profile_id if profile_id == None else profile_id
        url = f"https://sync.anty-api.com/?actionType=importCookies&browserProfileId={profile}"
        data = {
            "cookies": cookie
        }
        headers = {
            "Authorization": f"Bearer {self.__token}"
        }
        r = requests.post(url,headers=headers,data=json.dumps(data))
        if r.status_code == 200:
            return r.json()
        return {"success": False}

        

    def create_new_profile(self,profile_name,platforms = ["macos","linux","windows"],browser_versions = [102,107],proxy = None):
        platform = platforms[randint(0,len(platforms) - 1)] if type(platforms) == list else platforms
        browser_version = str(randint(browser_versions[0],browser_versions[1] + 1)) if type(browser_versions) == list else browser_versions

        fingerprint = self.get_new_fingerprint(platform=platform,browser_version=browser_version)
        useragent = self.get_new_useragent(platform=platform,browser_version=browser_version)

        memory = int(fingerprint["deviceMemory"])
        memory = memory + 1 if memory == 0 else memory

        cpu = int(fingerprint["hardwareConcurrency"])
        cpu = cpu + 1 if cpu == 0 else cpu
        screen_width = fingerprint["screen"]["width"]
        screen_height = fingerprint["screen"]["height"]
        params = {
        "name": profile_name,
        "tags": [],
        "platform": platform,
        "browserType": "anty",
        "mainWebsite": "",
        "useragent": {
            "mode": "manual",
            "value": useragent
        },
        "webrtc": {
            "mode": "altered",
            "ipAddress": None
        },
        "canvas": {
            "mode": "real"
        },
        "webgl": {
            "mode": "real"
        },
        "webglInfo": {
            "mode": "manual",
            "vendor": fingerprint["webgl"]["unmaskedVendor"],
            "renderer": fingerprint["webgl"]["unmaskedRenderer"]
        },
        "clientRect": {
            "mode": "real"
        },
        "notes": {
            "content": None,
            "color": "blue",
            "style": "text",
            "icon": "info"
        },
        "timezone": {
            "mode": "auto",
            "value": None
        },
        "locale": {
            "mode": "auto",
            "value": None
        },
        "proxy": None,
        "statusId": 0,
        "geolocation": {
            "mode": "auto",
            "latitude": None,
            "longitude": None,
            "accuracy": None
        },
        "cpu": {
            "mode": "manual",
            "value": cpu
        },
        "memory": {
            "mode": "manual",
            "value": memory
        },
        "screen": {
            "mode": "real",
            "resolution":  f"{screen_width}x{screen_height}"
        },
        "audio": {
            "mode": "real"
        },
        "mediaDevices": {
            "mode": "real",
            "audioInputs": None,
            "videoInputs": None,
            "audioOutputs": None
        },
        "ports": {
            "mode": "protect",
            "blacklist": "3389,5900,5800,7070,6568,5938"
        },
        "doNotTrack": False,
        "args": [],
        "platformVersion": fingerprint["platformVersion"],
        "uaFullVersion": fingerprint["uaFullVersion"],
        "login": "",
        "password": "",
        "appCodeName": fingerprint["appCodeName"],
        "platformName": fingerprint["platform"],
        "connectionDownlink": fingerprint["connection"]["downlink"],
        "connectionEffectiveType": str(fingerprint["connection"]["downlink"]),
        "connectionRtt": fingerprint["connection"]["rtt"],
        "connectionSaveData": fingerprint["connection"]["saveData"],
        "cpuArchitecture": fingerprint["cpu"]["architecture"],
        "osVersion": fingerprint["os"]["version"],
        "vendorSub": fingerprint["vendorSub"],
        "productSub": fingerprint["productSub"],
        "vendor": fingerprint["vendor"],
        "product": fingerprint["product"]
        }
        if proxy != None:
            params["proxy"] = {
                "type": proxy["type"],
                "host": proxy["host"],
                "port": proxy["port"]
            }
            if "login" in proxy.keys():
                if proxy["login"] != None:
                    params["proxy"].update({"login": proxy["username"],"password": proxy["password"]})

            
        
    

        payload = json.dumps(params)
        self.profile_data = self.execute_request(url="browser_profiles",method ="POST",params=payload,is_payload=True)
        if self.profile_data["status"]:
            self.profile_id = self.profile_data["data"]["browserProfileId"]
            #print(self.profile_data)
            return params,self.profile_data,useragent
        raise Exception("create_new_profile Error")



