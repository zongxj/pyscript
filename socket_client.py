#coding:utf-8
import socket
#创建socket对象
clientsocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#获取本地主机名
host = socket.gethostname()
#设置端口号
port = 9999
#连接服务，指定主机端口号
clientsocket.connect((host,port))
#接受小于1024字节的数据
msg = clientsocket.recv(1024)
#关闭连接
clientsocket.close()
print(msg.decode('utf-8'))