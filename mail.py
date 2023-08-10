from flask import Flask, render_template,request,send_from_directory,url_for,redirect
from flask_mail import Mail,Message
import random
import json
import keys

with open('config.json','r') as c:
   parameter=json.load(c)["parameter"]


app = Flask(__name__)

mail= Mail(app)
app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = keys.email_user
app.config['MAIL_PASSWORD'] = keys.email_pass
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
mail = Mail(app)
users=[{'name':'sanjeev','email':'sk2747267@gmail.com'}]
num=random.randint(10000,100000)

@app.route('/')
def send_mail():
    #SENDING BULK MESSAGES
    with mail.connect() as con:
         for user in users:
             msg="Thank You %s for giving your time for my help..\n\nHave a good day" %(user['name'])
             mess=Message(subject="Thanking Message From Sanjeev",sender="manojkumarsinghy30@gmail.com",recipients=[user['email']],body=msg)      
             con.send(mess) #PENDING NOW--->
    #SENDING SINGLE MESAGE with attachment file
    # msg = Message('Hello', sender = 'jkljlgjdf@gmail.com', recipients = ['sk2747267@gmail.com'])\

    #Creating OTP By sing random module
    # num=random.randint(10000,100000)
    # msg.body = "Your One-Time-Password is %s" %num
    
    # with app.open_resource('C:/Users/91875/OneDrive/Desktop/Flask20/fees.jpeg') as file:
        # msg.attach('slip.png','image/png',file.read())
        # mail.send(msg)
             
             #,{'name':'Sanju Baba Vines','email':'sanjuvines20@gmail.com'},{'name':'Nitin Saroj','email':'smsng2289@gmail.com'},{'name':'Gourav Yadav','email':'gauravyadav29112003@gmail.com'},{'name':'Arun Babara','email':'arunbabra51@gmail.com'},{'name':'Om Raghav Yadav M','email':'raksvaom@gmail.com'},{'name':'Nikhil Yadav','email':'01212nikhil@gmail.com'},{'name':'Risabh Katiyar','email':'rishabhkatiyar2003@gmail.com'},{'name':'Vinay Singh','email':'vinaysingh15052004@gmail.com'},{'name':'Ansh Mishra','email':'drakrai18@gmail.com'}


    return "Sent successfully"

if __name__== '__main__':
    app.run(debug=True)
