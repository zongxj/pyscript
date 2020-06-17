import pymysql


class MysqlToDateDict(object):
    def __init__(self):
        self.conn = pymysql.connect(
            host='10.45.40.103',
            port=3306,
            user='root',
            password='ztesoft@2020',
            charset='utf8',
            database='saas_jianye',
        )
        self.filename = 'saas_jianye.md'

    def close_conndb(self):
        try:
            if self.conn:
                self.conn.close()
        except pymysql.Error as e:
            print(e)

    def check_conndb(self):
        try:
            sql = 'select version()'
            cursor = self.conn.cursor()
            cursor.execute(sql)
            res = cursor.fetchone()
            return res
        except pymysql.Error as e:
            print(e)

    def get_tables(self):
        try:
            sql = 'show tables'
            cursor = self.conn.cursor()
            cursor.execute(sql)
            res = cursor.fetchall()
            return res
        except pymysql.Error as e:
            print(e)

    def get_table(self, tables):
        list1 = []
        for (row,) in tables:
            list1.append(row)
        return list1

    def to_dict(self, table):
        try:
            sql = "select COLUMN_NAME,COLUMN_TYPE,COLUMN_DEFAULT,COLUMN_COMMENT from information_schema.COLUMNS where table_schema='saas_jianye' and table_name='%s'" % table
            cursor = self.conn.cursor()
            cursor.execute(sql)
            res = cursor.fetchall()
            return res
        except pymysql.Error as e:
            print(e)


if __name__ == '__main__':
    todict = MysqlToDateDict()
    tables = todict.get_tables()
    for table_name in todict.get_table(tables):
        dict_file = open(todict.filename, 'a', encoding='UTF-8')
        if "act" in table_name:
            continue
        dict_file.write("\n---")
        dict_file.write("\n###表名：" + table_name)
        dict_file.write("\n---")
        dict_file.write('\n| 字段名称 | 字段类型 | 默认值 | 字段注释 |')
        dict_file.write('\n| ------------ | ------------ | ------------ | ------------ |')
        result = todict.to_dict(table_name)
        result_list = list(result)
        for column in result_list:
            result_list[result_list.index(column)] = list(column)
            dict_file.write("\n|" + column[0] + "|" + column[1] + "|" + str(column[2]) + "|" + column[3] + "|")
        dict_file.write("\r")
    todict.close_conndb()


