# -*- coding: utf-8 -*-
#encoding=utf-8
"""
自动生成MySQL数据表的数据字典支持多个
代码直接配置数据库连接信息，免输入
author: gxcuizy
date: 2020-04-30
"""

import pymysql
import os
import time


def conndb():
    """脚本执行入口"""
    config = {
        'host': '10.45.40.103',
        'port': 3306,
        'user': 'root',
        'password': 'ztesoft@2020',
        'database': 'saas_gov',
        'charset': 'utf8mb4',
        'cursorclass': pymysql.cursors.Cursor,
    }
    try:
        # 创建一个连接
        print(**config)
        conn = pymysql.connect(**config)
        # 用cursor()创建一个游标对象
        cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
    except Exception:
        print('数据库连接失败，请检查连接配置！')
        exit(1)
    table_str =('activity_answer,activity_answer_value,activity_custom_option')
    table_list = table_str.split(',')
    for table_name in table_list:
        # 判断表是否存在
        sql = "SHOW TABLES LIKE '%s'" % (table_name,)
        cursor.execute(sql)
        result_count = cursor.rowcount
        if result_count == 0:
            print('%s数据库中%s表名不存在，无法生成……' % (self.db_name, table_name))
            continue
        # 表注释获取
        print('开始生成表%s的数据字典' % (table_name,))
        sql = "show table status WHERE Name = '%s'" % (table_name,)
        cursor.execute(sql)
        result = cursor.fetchone()
        table_comment = result['Comment']
        # 文件夹和文件处理
        file_path = self.folder_name + os.sep + 'saas_jianye.md'
        self.deal_file(file_path)
        # 打开文件，准备写入
        dict_file = open(file_path, 'a', encoding='UTF-8')
        dict_file.write('#### %s %s' % (table_name, table_comment))
        dict_file.write('\n| 字段名称 | 字段类型 | 默认值 | 字段注释 |')
        dict_file.write('\n| --- | --- | --- | --- |')
        # 表结构查询
        field_str = "COLUMN_NAME,COLUMN_TYPE,COLUMN_DEFAULT,COLUMN_COMMENT from information_schema.COLUMNS"
        sql = "select %s where table_schema='%s' and table_name='%s'" % (field_str, self.db_name, table_name)
        cursor.execute(sql)
        fields = cursor.fetchall()
        for field in fields:
            column_name = field['COLUMN_NAME']
            column_type = field['COLUMN_TYPE']
            column_default = str(field['COLUMN_DEFAULT'])
            column_comment = field['COLUMN_COMMENT']
            info = '| ' + column_name + ' | ' + column_type + ' | ' + column_default + ' | ' + column_comment + ' | '
            dict_file.write('\n' + info)
        # 关闭连接
        print('完成表%s的数据字典' % (table_name,))
        dict_file.close()
    cursor.close()
    conn.close()

def deal_file(self, file_name):
    """处理存储文件夹和文件"""
    # 不存在则创建文件夹
    if not os.path.exists(self.folder_name):
        os.mkdir(self.folder_name)
    # 删除已存在的文件
    if os.path.isfile(file_name):
        os.unlink(file_name)


# 程序执行入口
if __name__ == '__main__':
    # 输入数据表名称
    conndb()
    print('谢谢使用，再见……')
