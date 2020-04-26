#usr/bin/python3
# -*- coding: utf-8 -*-

import pymysql

class Content (object):

    def __init__(self,name,id,address):
        self.name = name
        self.id = id
        self.address = address

    def __str__(self):
        return "name is:{self.name}\t id is:{self.id}\t address is:{self.address}".format(self.name,self.id,self.address)



def main():

    #建立链接和选择数据库
    db = pymysql.connect(host='localhost', user='zhiqiang', password='123',database='test',cursorclass=pymysql.cursors.DictCursor)

    #打开游标
    #cursor = db.cursor()

    #如果想要fetch的内容是字典形式
    cursor=db.cursor()

    #创建表格
    # sql = "CREATE TABLE tb_test3 (
    # name VARCHAR(20),
    # ID int,
    # gender int,
    # address VARCHAR(100),
    # primary key(ID))" #这里发现有一个\xe的错误，需要加入 coding就解决了

    #删除表格
    #sql = "DROP TABLE IF EXISTS tb_test"

    #批量插入数据
    # sql = """INSERT INTO tb_test VALUES
    # ('zhiqiang',001,1,'Stockholm'),
    # ('deyuan',002,1,'Shanghai'),
    # ('kaige',003,1,'Shanghai'),
    # ('xiran',004,0,'Haerbin'),
    # ('siqi',005,0,'Gothenburg')"""   # 首先，如果把这个语句写在一行，是可以只用“  ”，但是发现字符串内换行出现错误，所以加入”“”  ”“” 这样的形式

    #删除某一行数据
    #sql = "DELETE FROM tb_test WHERE id='%d'" %3

    #格式化输出形式，会有sql注入攻击的风险
    #sql = "INSERT INTO tb_test values('%s','%d','%d','%s')" %("kaige",3,1,"Shanghai")  # ‘%s’ 的‘’ cannot be omitted.

    #更新表格数据
    # new_address = input("new address to be updated: ")
    # new_id = int(input ("new id"))
    sql = "UPDATE tb_test SET id = '%d', address = '%s' WHERE name = 'Kaige'" %(3,"Stockholm" )

    #查询表格
    # sql = "SELECT name as n, id as i, address as addr FROM tb_test"

    # fetchall() #获取查询内容，元组形式
    # fetchone() #获取查询一行
    # fetchmany(n) #获取n行
    #注意，执行过fetchone（），游标会到下一行，再用fetchall（）只能fetch剩下的行的内容


    try:
        cursor.execute(sql)
        db.commit()
        #利用默认游标
        # for row in cursor.fetchall():
        #     print("name is: {name}".format(name = row[0]))

        # #利用字典型游标
        # for row in cursor.fetchall():
        #     print(row['n'])  #在sql查询表格时，已经用了别名
        #     print(row['i'])
        #
        # # 利用字典解包将内容传递给对象
        # for row in cursor.fetchall():
        #     content_obj = Content(**row)
        #     print(content_obj)  #注意类的内置方法的应用 __str__

    except pymysql.MySQLError as error:
        print(error)
        db.rollback()

    finally:
        cursor.close()
        db.close()

if __name__=='__main__':
    main()
