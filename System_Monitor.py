# coding:utf-8
import psutil
import time

# 获取当前时间
now_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
print(now_time+'\n')
###############################
#         CPU信息
###############################
# 查看cpu所有信息
Cpu_Time_1 = psutil.cpu_times()
print(Cpu_Time_1)
# 显示cpu所有逻辑信息
Cpu_Time_2 = psutil.cpu_times(percpu=False)
print(Cpu_Time_2)
# 查看用户的cpu时间
Cpu_Time_3 = psutil.cpu_times().user
print(Cpu_Time_3)
# 查看cpu逻辑个数
Cpu_Count_1 = psutil.cpu_count()
print(Cpu_Count_1)
# 查看cpu物理个数
Cpu_Count_2 = psutil.cpu_count(logical=False)
print(Cpu_Count_2)
###############################
#         内存信息
###############################
# 查看系统内存
Mem = psutil.virtual_memory()
print(Mem)
# 获取swap内存信息
Mem = psutil.swap_memory()
print(Mem)
###############################
#         硬盘信息
###############################
# 磁盘I/O信息
Disk = psutil.disk_io_counters()
print(Disk)
# 获取单个分区I/O信息
Disk = psutil.disk_io_counters(perdisk=True)
print(Disk)
# 获取磁盘的完整信息
Disk = psutil.disk_partitions()
print(Disk)
# 获取分区使用信息
Disk = psutil.disk_usage('/')
print(Disk)
###############################
#         网络信息
###############################
# 获取网络总I/O信息
Net = psutil.net_io_counters()
print(Net)
# 输出网络每个接口信息
Net = psutil.net_io_counters(pernic=True)
print(Net)
# 获取网络连接信息 #netstat -anlt
Net = psutil.net_connections()
print(Net)
# 获取本地网卡信息 #ifconfig
Net = psutil.net_if_addrs()
print(Net)
# 获取本地网卡信息
Net = psutil.net_if_stats()
print(Net)
###############################
#         系统信息
###############################
# 获取当前系统用户登录信息
user = psutil.users()
print(user)
# 获取开机时间
boot_time = psutil.boot_time()
started_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(boot_time))
print(started_time)
# 查看系统全部进程
pid = psutil.pids()
print(pid)
