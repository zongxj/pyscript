import pymysql

#考虑注释是中文
# sys.setdefaultencoding('utf8')

conn = pymysql.connect(host='10.45.40.103',user='root',password='ztesoft@2020',database='saas_jianye')
cursor = conn.cursor()
cursor.execute("select table_name from information_schema.tables where table_schema='saas_jianye'")
tables = cursor.fetchall()

markdown_table_header = """### %s 
字段名 | 字段类型 | 默认值 | 注解
---- | ---- | ---- | ---- 
"""
markdown_table_row = """%s | %s | %s | %s
"""
#保存输出结果
f = open('markdown.out','w')
for table in tables:
    cursor.execute("select COLUMN_NAME,COLUMN_TYPE,COLUMN_DEFAULT,COLUMN_COMMENT from information_schema.COLUMNS where table_schema='数据库名' and table_name='%s'"% table)
    tmp_table = cursor.fetchall()
    p = markdown_table_header % table;
    for col in tmp_table:
        p += markdown_table_row % col
    #print p
    f.writelines(p)
f.close()