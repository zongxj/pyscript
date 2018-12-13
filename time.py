# coding:utf-8
import time

a = time.localtime()

now_time = time.strftime('%Y-%m-%d %H:%M:%S',a)
print(now_time)
