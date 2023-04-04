import requests
import time
import json
from Utils import constants
from Utils.utils import *


username = "tbt "
port = 35000
group = "4e5bb4e6-4342-4018-ae2d-dff922900c40"

class MultiLogin:

    def create_profile(self,proxy = None):
        url = f"http://localhost.multiloginapp.com:{port}/api/v2/profile"

        # TODO
        raw_payload = { 
            "name": f"{username} ih",
            #"group": group,
            "browser": "mimic",
            "os": constants.OS_SYSTEM[get_platform_system()],
        }
        if proxy != None:
            raw_payload["network"] = { 
                "proxy": { 
                    "type": proxy["type"], 
                    "host": proxy["host"], 
                    "port": proxy["port"], 
                } 
            }
            if proxy["username"] != None:
                raw_payload["network"]["proxy"]["username"] = proxy["username"]
                raw_payload["network"]["proxy"]["password"] = proxy["password"]
             

        payload = json.dumps(raw_payload)
        headers = {
        'Content-Type': 'application/json'
        }

        response = requests.request("POST", url, headers=headers, data=payload)
        self.uuid = response.json()['uuid']
        return self.uuid

    def start_profile(self,isWS = False):
        while True:
            try:
                url = f"http://localhost.multiloginapp.com:{port}/api/v1/profile/start?automation=true&profileId={self.uuid}"
                if isWS:
                    url = f"http://localhost.multiloginapp.com:{port}/api/v1/profile/start?automation=true&puppeteer=true&profileId={self.uuid}"
                payload={}
                headers = {}

                response = requests.request("GET", url, headers=headers, data=payload)
                if response.json()['status'] == 'OK':
                    self.url = response.json()['value']
                    return self.url
            except Exception as e:
                print(e)
            finally:
                time.sleep(3)
        return False
    
    def check_activte(self):
        url = f"http://localhost.multiloginapp.com:{port}/api/v1/profile/active?profileId={self.uuid}"
        payload={}
        headers = {}
        response = requests.request("GET", url, headers=headers, data=payload)
        if response.json()['status'] == 'OK':
            return response.json()['value']
        return False

    def stop_profile(self):
        while self.check_activte():
            try:
                url = f"http://localhost.multiloginapp.com:{port}/api/v1/profile/stop?automation=true&profileId={self.uuid}"

                payload={}
                headers = {}
                response = requests.request("GET", url, headers=headers, data=payload)
                print(url)
                print(response.text)
                # if response.json()['status'] == 'OK':
                #     return True
            except Exception as e:
                print('[ERROR] ',e)
            finally:
                time.sleep(3)
        return True


    def delete_profile(self):
        url = f"http://localhost.multiloginapp.com:{port}/api/v2/profile/{self.uuid}"
        payload={}
        headers = {}
        response = requests.request("DELETE", url, headers=headers, data=payload)


        