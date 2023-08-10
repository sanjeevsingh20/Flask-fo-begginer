import mysql.connector
username=input("Enter the user name: ")
# passwords=input("Enter password: ")

db=mysql.connector.connect(host='localhost',user='root',password='@#Sanjukumar123',database='profile')
mycur=db.cursor()
mycur.execute('select phone_no,Email from registered where phone_no=%s or Email=%s;' %(username,username))
         # result=mycur.fetchall()
for (phone_no,Email) in mycur:
    if phone_no==username or Email==username:
            print("{} done".format(username))
mycur.close()
db.commit()  