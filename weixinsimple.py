#coding:utf-8

msg = sys.argv[3]
Corpid = 'wxe339a3188552fe9f'
Secret = 'KpgNm4OqbFlNdaT5BwcZfgo43jH6jUCMM3GUBsIr_GM'
Geturl = "https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid="+Corpid+"&corpsecret="+Secret+""
response = urllib.request.urlopen(Geturl).read()
token = (json.loads(response)['access_token'])
connAT = "https://qyapi.weixin.qq.com/cgi-bin/message/send?access_token="+token+""
#msg = "python群发测试"
ATcontent = """{
    "touser" : "touser" ,
    "toparty":"2",
    "msgtype":"text",
    "agentid":"1",
    "text":{
        "content":"%s"
    },
    "safe":"0"
    }""" %(str(msg))
data = json.loads(ATcontent)
post = requests.post(connAT,ATcontent)
print(post)