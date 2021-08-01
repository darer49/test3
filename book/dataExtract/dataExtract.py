import pymssql as sql
import datetime
from threading import Timer
import os
import time
'''
#创建数据库连接pymysql.Connect()参数说明
host(str):      MySQL服务器地址
port(int):      MySQL服务器端口号
user(str):      用户名
passwd(str):    密码
db(str):        数据库名称
charset(str):   连接编码，存在中文的时候，连接需要添加charset='utf8'，否则中文显示乱码。

connection对象支持的方法
cursor()        使用该连接创建并返回游标
commit()        提交当前事务，不然无法保存新建或者修改的数据
rollback()      回滚当前事务
close()         关闭连接

cursor对象支持的方法
execute(op)     执行SQL，并返回受影响行数
fetchone()      取得结果集的下一行
fetchmany(size) 获取结果集的下几行
fetchall()      获取结果集中的所有行
rowcount()      返回数据条数或影响行数
close()         关闭游标对象
'''
WTIME = time.localtime(os.path.getmtime("addfile.txt"))
WAITTIME = 60*60*1000
host = "127.0.0.1"  # 源数据库的地址
user = "root"  # 源数据库的用户名
pswd = "123qwe"  # 源数据库的密码
DBname = "testdb"  # 源数据库名称
tbname = "student"  # 源数据需要被同步的表格名称

host2 = "127.0.0.1"  # 同步数据库地址
user2 = "root"  # 同步数据库用户名
pswd2 = "123qwe"  # 同步数据库密码
DBname2 = "todb"  # 同步数据库名称
tbname2 = "student_async"  # 同步数据库中储存同步数据的表格名称



def timea_b(timea,timeb):
    timea = time.strftime("%Y-%m-%d %H:%M:%S",timea)
    timeb = time.strftime("%Y-%m-%d %H:%M:%S",timeb)
    timea = datetime.datetime.strptime(timea,"%Y-%m-%d %H:%M:%S")
    timeb = datetime.datetime.strptime(timeb,"%Y-%m-%d %H:%M:%S")
    return (timea-timeb).seconds


def write_addinfo(info):
    with open("addfile.txt","w") as f:
        f.write(info)
    WTIME = time.ctime(os.path.getmtime("addfile.txt"))


def get_addinfo():
    with open("addfile.txt","r") as f:
        return f.read()


def mysql_synchroDB():

    time_now = time.localtime()
    if timea_b(time_now,WTIME)<(WAITTIME-10*1000):  # 表示修改了，需要重新导入
        # 读取新增的数据
        conn1 = sql.connect(host=host, user=user, password=pswd, database=DBname, charset="utf8")
        info = get_addinfo()
        idlist = info.split(",")[0:-1]
        print(idlist)
        str1 = "select * from " + tbname + " where "
        for id in idlist:
            if idlist.index(id) == len(idlist) - 1:
                str1 += "id=" + id
            else:
                str1 += "id=" + id + " or "
        cursor1 = conn1.cursor()
        cursor1.execute(str1)
        results = cursor1.fetchall()

        # 同步新增的数据
        conn2 = sql.connect(host=host2, user=user2, password=pswd2, database=DBname2, charset="utf8")
        str2 = "insert into "+tbname2+" (id,name,age) values "
        for res in results:
            if results.index(res)==len(results)-1:
                str2 += str(res)
            else:
                str2 += str(res)+","
        cursor2 = conn2.cursor()
        cursor2.execute(str2)
        conn2.commit()

        # 关闭连接和游标
        cursor1.close()
        conn1.close()
        cursor2.close()
        conn2.close()

        t = Timer(WAITTIME, mysql_synchroDB)
        t.start()


def mysql_changeDB():
    insert_info = [["6","anna","21"],["7","bob","23"],["8","cindy","20"]]
    sqlstr = "insert into "+tbname+" (id,name,age) values ('{0[0]}','{0[1]}','{0[2]}');"
    conn = sql.connect(host=host,user=user,password=pswd,database=DBname,charset="utf8")
    cursor = conn.cursor()
    info=""  # 记录修改的关键key
    for inser in insert_info:
        str1 = sqlstr.format(inser)
        print(str1)
        cursor.execute(str1)
        info += inser[0]+","
        conn.commit()
    write_addinfo(info)
    # deletestr = "delete from "+tbname+" where id=6 or id=7 or id=8"
    # cursor.execute(deletestr)
    # conn.commit()
    cursor.close()
    conn.close()




if __name__=="__main__":
    # mysql_connction()
    # get_addinfo()
    # with open("addfile.txt","r") as f:
    #     f.read()
    # a = time.localtime(os.path.getctime("addfile.txt"))
    # b = time.localtime(os.path.getmtime("addfile.txt"))
    # list = "1,2,3,4,".split(",")
    #
    # print("insert into "+str((1,2,3)))
    # mysql_synchroDB()
    t = Timer(WAITTIME, mysql_synchroDB)
    t.start()