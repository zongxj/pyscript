#!/usr/bin/python
# coding:utf-8
"""
# Author: zongxj
# Created Time : 2018-02-09 14:35:47
# File Name: testdb.py
# Description:
"""
import cx_Oracle as cx
user="cms6"
passwd="cms6yzdb"
host="32.110.0.53"
prot="1521"
sid="yz2nd"
#dsn=cx.makedsn(host,prot,sid)
conn=cx.connect('cmspro/sqrendacmspro@222.187.245.193:11521/ORCL')
#conn=cx.connect(user,passwd,dsn)
cursor=cx.Cursor(conn)
print("=============表空间使用率=================")
sql="select total.tablespace_name,round(total.MB, 2) as Total_MB, round(total.MB - free.MB, 2) as Used_MB, round((1 - free.MB / total.MB) * 100, 2) || '%' as Used_Pct from (select tablespace_name,sum(bytes) / 1024 / 1024 as MB from dba_free_space group by tablespace_name) free, (select tablespace_name,sum(bytes) / 1024 / 1024 as MB from dba_data_files group by tablespace_name) total where free.tablespace_name = total.tablespace_name order by used_pct desc"
sql1="select username,expiry_date from dba_users"
if True:
    cursor.execute(sql)
    for i in cursor:
        print(i)
print("============用户密码过期时间==============")
if True:
    cursor.execute(sql1)
    for j in cursor:
        print(j)
cursor.close()
conn.close()