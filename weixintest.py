#coding:utf-8
import urllib.request
import json
import sys
import requests

class weixin_zabbix(object):

    def get_AT(self, Corpid, Secret):
        Geturl = "https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid=" + Corpid + "&corpsecret=" + Secret + ""
        token = (json.loads(urllib.request.urlopen(Geturl).read())['access_token'])
        connAT = "https://qyapi.weixin.qq.com/cgi-bin/message/send?access_token=" + token + ""
        return connAT

    def get_msg(self, content):
        content = {
            "touser" : "touser" ,
            "toparty":"2",
            "msgtype":"text",
            "agentid":"1",
            "text":{
                "content":content
            },
            "safe":"0"
            }
        ATcontent = json.dumps(content,ensure_ascii=False).encode('utf-8')
        return ATcontent

    def post_msg(self, connAT, msg):
        post = requests.post(connAT, data=msg)
        return post.text

if __name__ == '__main__':
    content = sys.argv[3]
    Corpid = 'wxe339a3188552fe9f'
    Secret = 'KpgNm4OqbFlNdaT5BwcZfgo43jH6jUCMM3GUBsIr_GM'
    obj_zabbix = weixin_zabbix()
    connAT = obj_zabbix.get_AT(Corpid,Secret)
    msg = obj_zabbix.get_msg(content)
    response = obj_zabbix.post_msg(connAT,msg)
    print(response)