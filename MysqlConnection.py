import mysql.connector
mydb=mysql.connector.connect(host="localhost",user="root",password="******",database="mydb")
print("connection success")
cursor=mydb.cursor()
cursor.execute("select *from employee ")
result=cursor.fetchone()
for on in result:
    print(on)

for i in cursor:
    print(i)

cursor2=mydb.cursor();
cursor2.execute("show databases")
for h in cursor2:
    print(h)
