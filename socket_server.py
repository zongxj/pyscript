# coding:utf-8
import socket
# 创建socket对象
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 获取本地主机名
host = "127.0.0.1"
port = 9999
# 绑定端口号
serversocket.bind((host, port))
# 设置最大连接数，超出排队
serversocket.listen(5)
while True:
    # 建立客户端连接
    clientsocket, addr = serversocket.accept()
    print("连接地址: %s" % str(addr))
    msg = '连接成功！！！' + "\r\n"
    clientsocket.send(msg.encode('utf-8'))
    clientsocket.close()
