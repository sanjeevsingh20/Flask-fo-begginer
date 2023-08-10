from flask import Flask, render_template, request,redirect,url_for,session
import mysql.connector


app=Flask(__name__)

@app.route('/')
def results():
    db=mysql.connector.connect(host='localhost',user='root',password='@#Sanjukumar123',database='profile')
    mycur=db.cursor()
    mycur.execute('select * from registered;')
    details=mycur.fetchall()
    db.commit()

    
    
    return render_template('data.html',res=details)
    
if __name__=='__main__':
    app.run(debug=True)


