#!/usr/bin/env python

import json
import requests
from requests.auth import HTTPBasicAuth

if __name__ == "__main__":

    auth = HTTPBasicAuth('cisco', 'cisco')
    headers = {
        'Accept': 'application/json',
        'Content-Type': 'application/json'
    }

    url = "https://asav/api/interfaces/physical/GigabitEthernet0_API_SLASH_0"

    body = {
        "kind": "object#GigabitInterface",
        "interfaceDesc": "Configured by Python"
    }

    requests.packages.urllib3.disable_warnings()
    response = requests.patch(url, data=json.dumps(body), auth=auth, headers=headers, verify=False)




