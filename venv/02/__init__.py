#将 0001 题生成的 200 个激活码（或者优惠券）保存到 MySQL 关系型数据库中。
import mysql.connector
def gen():
    conn=mysql.connector.connect(host="localhost",port="3306",user="root",password="123456",database="test",charset="utf8")
    cursor=conn.cursor()
    with open("tt") as file:
        for line in file:
            cursor.execute('insert into user(name) values(%s)',[line])
    conn.commit()
    cursor.close()
    conn.close

if __name__=="__main__":
    gen()