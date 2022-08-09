# -*- coding: utf-8 -*-
import pymysql

import random

class MysqlDB:

    def __init__(self, host="127.0.0.1", port=3306, user="root", password="",
                 database="amz"):
        try:
            self.conn = pymysql.connect(
                host=host,  # 连接名称，默认127.0.0.1
                user=user,  # 用户名
                passwd=password,  # 密码
                port=port,  # 端口，默认为3306,
                db=database,  # 数据库名称,
                charset='utf8')  # 字符编码
            self.cursor = self.conn.cursor(cursor=pymysql.cursors.DictCursor)
        except Exception as e:
            print(e)

    # 返回执行execute()方法后影响的行数 
    def execute(self, sql):
        self.cursor.execute(sql)
        rowcount = self.cursor.rowcount
        return rowcount

    # 删除并返回影响行数
    def delete(self, **kwargs):
        table = kwargs['table']

        where = kwargs['where']
        sql = 'DELETE FROM %s where %s' % (table, where)
        print(sql)
        try:
            # 执行SQL语句
            self.cursor.execute(sql)
            # 提交到数据库执行
            self.conn.commit()
            # 影响的行数
            rowcount = self.cursor.rowcount
        except:
            # 发生错误时回滚
            self.conn.rollback()
        return rowcount

    # 新增并返回新增ID
    def insert(self, **kwargs):
        table = kwargs['table']
        del kwargs['table']
        sql = 'insert into %s(' % table
        fields = ""
        values = ""
        for k, v in kwargs.items():
            fields += "%s," % k
            values += "'%s'," % v
        fields = fields.rstrip(',')
        values = values.rstrip(',')
        sql = sql + fields + ")values(" + values + ")"
        print(sql)
        res = []
        try:
            # 执行SQL语句
            self.cursor.execute(sql)
            # 提交到数据库执行
            self.conn.commit()
            # 获取自增id
            res = self.cursor.lastrowid
        except:
            # 发生错误时回滚
            self.conn.rollback()
        return res

    # 修改数据并返回影响的行数

    def update(self, **kwargs):
        table = kwargs['table']
        # del kwargs['table']
        kwargs.pop('table')
        where = kwargs['where']
        kwargs.pop('where')
        sql = 'update %s set ' % table
        for k, v in kwargs.items():
            sql += "%s='%s'," % (k, v)
        sql = sql.rstrip(',')
        sql += ' where %s' % where
        print(sql)
        rowcount = 0
        try:
            # 执行SQL语句
            self.cursor.execute(sql)
            # 提交到数据库执行
            self.conn.commit()
            # 影响的行数
            rowcount = self.cursor.rowcount
        except:
            # 发生错误时回滚
            self.conn.rollback()
        return rowcount

    # 查-一条条数据
    def getOne(self, **kwargs):
        table = kwargs['table']
        field = 'field' in kwargs and kwargs['field'] or '*'
        where = 'where' in kwargs and 'where ' + kwargs['where'] or ''
        order = 'order' in kwargs and 'order by ' + kwargs['order'] or ''
        sql = 'select %s from %s %s %s limit 1' % (field, table, where, order)
        print(sql)
        data = []
        try:
            # 执行SQL语句
            self.cursor.execute(sql)
            # 使用 fetchone() 方法获取单条数据.
            data = self.cursor.fetchone()
        except:
            # 发生错误时回滚
            self.conn.rollback()
        return data

    # 查所有数据
    def getAll(self, **kwargs):
        table = kwargs['table']
        field = 'field' in kwargs and kwargs['field'] or '*'
        where = 'where' in kwargs and 'where ' + kwargs['where'] or ''
        order = 'order' in kwargs and 'order by ' + kwargs['order'] or ''
        sql = 'select %s from %s %s %s ' % (field, table, where, order)
        print(sql)
        try:
            # 执行SQL语句
            self.cursor.execute(sql)
            # 使用 fetchone() 方法获取单条数据.
            data = self.cursor.fetchall()
        except:
            # 发生错误时回滚
            self.conn.rollback()
        return list(data)

    def __del__(self):
        self.conn.close()  # 关闭连接



if __name__ == '__main__':
    db = MysqlDB()

    # asin = ''
    # for i in range(5):
    #     asin += random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    # 
    # # insert测试
    # cs = db.insert(table="asin", asin=asin, title="标题"+str(random.randint(100,999)), stars=4.3)
    # print(cs)

    # delete 测试
    # cs = db.delete(table="T1", where="Id = 2")
    # print(cs)

    # update 测试
    # cs = db.update(table="T1", Name="Python测试3", Sex="man", where="Id in(1,2)")
    # print(cs)

    # select 测试
    cs = db.getAll(table="asin", where="1")
    print(cs)

