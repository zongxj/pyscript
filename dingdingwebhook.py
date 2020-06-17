# coding=utf-8
import time
import hmac
import hashlib
import base64
import requests
import urllib
import json

timestamp = str(round(time.time() * 1000))
secret = 'SECb337866d6fc7902e66dc45864351dbef6cca876fc0f5aeecb470887b83b1870a'
secret_enc = secret.encode('utf-8')
string_to_sign = '{}\n{}'.format(timestamp, secret)
string_to_sign_enc = string_to_sign.encode('utf-8')
hmac_code = hmac.new(secret_enc, string_to_sign_enc, digestmod=hashlib.sha256).digest()
sign = urllib.parse.quote_plus(base64.b64encode(hmac_code))
print(timestamp)
print(sign)

url = 'https://oapi.dingtalk.com/robot/send?access_token=3cdf2891a504a0714a57dbbae83de7bc24b4c65c7bb9eaa73e71be864ea90be5&timestamp=%s&sign=%s'%(timestamp,sign)

print(url)
headers = {"Content-Type": "application/json"}
#1：失败告警    2：成功提示
if sys.argv[1] = 1:
    data = {
     "msgtype": "markdown",
     "markdown": {
         "title":"提示信息",
         "text": "#### 提示信息\n> %s> ![screenshot](https://img.alicdn.com/tfs/TB1NwmBEL9TBuNjy1zbXXXpepXa-2400-1218.png)\n>"%(sys.argv[2])
     },
    }
    else:
    data = {
     "msgtype": "markdown",
     "markdown": {
         "title":"提示信息",
         "text": "#### 提示信息\n> %s> ![screenshot](https://img.alicdn.com/tfs/TB1NwmBEL9TBuNjy1zbXXXpepXa-2400-1218.png)\n>"%(sys.argv[2])
     },
    }
r = requests.post(url=url, data=json.dumps(data), headers=headers)



print(r.content)
