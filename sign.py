# coding=utf-8
import time
import hmac
import hashlib
import base64
import requests
import urllib
import json
import sys

timestamp = long(round(time.time() * 1000))
access_token = '3d80f175058463248ef36fb460dd8e2a0136a15d9efc18d86290d3d466bb3eda'
secret = 'SEC62c7511b1590e7d5cfaf5dd413c04902bbaadda910a8cd4744f7a28ce59ab751'
secret_enc = bytes(secret).encode('utf-8')
string_to_sign = '{}\n{}'.format(timestamp, secret)
string_to_sign_enc = bytes(string_to_sign).encode('utf-8')
hmac_code = hmac.new(secret_enc, string_to_sign_enc, digestmod=hashlib.sha256).digest()
sign = urllib.quote_plus(base64.b64encode(hmac_code))
url = 'https://oapi.dingtalk.com/robot/send?access_token=%s&timestamp=%s&sign=%s'%(access_token,timestamp,sign)
headers = {"Content-Type": "application/json"}
data = {
    "msgtype": "text",
    "text": {
        "content": sys.argv[1]
    },
    "at": {
        "atMobiles": [
            "18012041890",
	    "13921948563",
	    "15161885512"
        ],
        "isAtAll": "false"
    }
}
r = requests.post(url=url, data=json.dumps(data), headers=headers)

print(r.content)
