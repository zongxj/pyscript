# coding:utf-8
import socket
import sys
# 创建socket对象
clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 设置连接地址
host = "127.0.0.1"
# 设置端口号
port = 9999
# 连接服务，指定主机端口号
print((host, port.))
clientsocket.connect((host, port))
# 接受小于1024字节的数据
msg = clientsocket.recv(1024)
# 关闭连接
clientsocket.close()
print(msg.decode('utf-8'))
