from flask import Flask, render_template, request,redirect,url_for,session
import mysql.connector
import json
from flask_mail import Mail,Message
import random
import config





with open('config.json','r') as c:
   parameter=json.load(c)["parameter"]

app = Flask(__name__)
app.secret_key='login'
mail= Mail(app)
app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = config.email_user
app.config['MAIL_PASSWORD'] = config.email_pass
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
mail = Mail(app)
num=random.randint(10000,100000)
#to get the data from the form
@app.route('/dashboard', methods = ['GET', 'POST'])
def dashboard():
   # try:
      if request.method =='POST':
         user=request.form.get('first')
         last_name=request.form.get('last')
         email=request.form.get('mail')
         phone=request.form.get('phone')
         passwords=request.form.get('passw')
         gender=request.form.get('gender')
         clas=request.form.get('classes')
         state=request.form.get('state')
         pin=request.form.get('pin')
        
         db=mysql.connector.connect(host='localhost',user='root',password='@#Sanjukumar123',database='profile')
         mycur=db.cursor()
         mycur.execute('insert into registered (first_name,last_name,Email,phone_no,password,Gender,class,state,pincode) values(%s,%s,%s,%s,%s,%s,%s,%s,%s)',(user,last_name,email,phone,passwords,gender,clas,state,pin))
         mycur.execute('select stu_id from registered where phone_no=%s and password=%s;',(phone,passwords))
         result=mycur.fetchall()
         db.commit()
         # msg = Message("Hello",
         #          sender=email,
         #          recipients=["manojkumarsinghy20.com"])
         # msg.body = "testing my Mail"
         # mail.send(msg)
         # return " %s!You are sucessfully registered to our institute with registration number %s <a href='/'>Log In Now</a>" %(user,result)
         mess='Hello %s To our Institute.\n From our Deep of Hear We Welcome you to our Institute.Please Verify your account.\n Your Verification Code is %s' %(user,num)
         msg=Message(subject='URS Verification',sender='URSadmin@gmail.com',recipients=[email],body=mess)
         mail.send(msg)
         return render_template('otp.html')
         

      else:
         user=request.args.get('first')
         return render_template('upload.html')
   # except:
   #    UserWarning("Email or phone number is already exist")
   #    return '%s or  %s already registered please use another email' %(email,phone)
@app.route('/verify',methods=['POST','GET'])
def verify():
    if request.method=='POST':
        otp=request.form.get('OTP')

        if otp==str(num):
            return " Congrats! You are sucessfully registered to our institute with a registration number <a href='/'>Log In Now</a>" 
        else:
            return "Wrong OTP"
    
@app.route('/login')
def login():
   return render_template('upload.html')

@app.route('/reset_password') #TO DO:- take phone number and send otp and than reset password
def reset():
   return "<a href='/login'>Click Here to reset your password</a>"
@app.route('/logout')
def logout():
   session.pop('username', None)
   return render_template('log.html')
@app.route('/')
def enter():
   return render_template('log.html')
  	
@app.route('/log' ,methods = ['POST']) #TO DO for login
def logi():
   
      if request.method =='POST':
         try:       
            username=request.form['user']
            # phone=request.form.get('user')
            passwords=request.form['passw']
            db=mysql.connector.connect(host='localhost',user='root',password='@#Sanjukumar123',database='profile')
            mycur=db.cursor()
            mycur.execute("select first_name, phone_no,Email,password from registered where phone_no='%s' or Email=%s and password='%s';" %(username,username,passwords))
            result=mycur.fetchall()
            db.commit() 
            
            for(first_name,phone_no,Email,password) in result:
                     if (username==phone_no and passwords == password):
                        session['uemail']=first_name
                        return render_template('log.html',name=first_name,para=parameter)
                     else:
                        return render_template('log.html',msg='wrong Phone Number or Password')
  
         except:
               return render_template("log.html",msg='wrong Phone Number or Password')
            

if __name__ == '__main__':
   app.run(debug = True)