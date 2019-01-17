import pymysql

conn = pymysql.Connect(host='127.0.0.1',user='root',password='',database='flaskdemo')
cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
cursor.execute('select * from userinfo where user =%(us)s and pwd =%(pw)s',{'us':'xiaoqiang','pw':'123123'})

result = cursor.fetchall()

cursor.close()
conn.close()
print(result)