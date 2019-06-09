#!/Library/Frameworks/Python.framework/Versions/3.7/bin/python
import pymysql

host = '127.0.0.1'
name = 'root'
passwd = '129670'
db  =  'my_test'
db = pymysql.connect(host,name,passwd,db)
cursor = db.cursor()
cursor.execute('select * from users');
data = cursor.fetchall()

for i in data:
    print(i)

db.close()