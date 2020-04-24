#usr/bin/python3
# -*- coding: utf-8 -*-

import pymysql


def main():

    db = pymysql.connect('localhost', 'zhiqiang', '123','test')
    cursor = db.cursor()

    sql = "CREATE TABLE tb_test3 (
    name VARCHAR(20),
    ID int,
    gender int,
    address VARCHAR(100),
    primary key(ID))" #这里发现有一个\xe的错误，需要加入 coding就解决了

    #sql = "DROP TABLE IF EXISTS tb_test"

    # sql = """INSERT INTO tb_test2 VALUES
    # ('zhiqiang',001,1,'Stockholm'),
    # ('deyuan',002,1,'Shanghai'),
    # ('kaige',003,1,'Shanghai'),
    # ('xiran',004,0,'Haerbin'),
    # ('siqi',005,0,'Gothenburg')"""   # 首先，如果把这个语句写在一行，是可以只用“  ”，但是发现字符串内换行出现错误，所以加入”“”  ”“” 这样的形式

    #sql = "DELETE FROM tb_test WHERE id='%d'" %3
    #sql = "INSERT INTO tb_test values('%s','%d','%d','%s')" %("kaige",3,1,"Shanghai")  # ‘%s’ ->‘’ cannot be omitted.

    try:
        cursor.execute(sql)
        db.commit()

    except pymysql.MySQLError as error:
        print(error)
        db.rollback()

    finally:
        cursor.close()
        db.close()

if __name__=='__main__':
    main()
