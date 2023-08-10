from flask import Flask, render_template
# from flask_sqlalchemy import SQLAlchemy

app=Flask(__name__)


@app.route('/mac.du.ac.in')
def home():
    return render_template('index.html',titles="Home | Maharaja Agrasen College")
@app.route('/')

def hello_world():
   
    title="Hotel"
    return "<a href='/mac.du.ac.in' >Redirect to main page</a> "

@app.route('/hostel')
def hostel():
    title="Home | MAHARAJA AGRASEN COLLEGE"
    return render_template('urs.html',titles="Hostel-MAC")


if __name__ == "__main__":
    app.run(debug=True,port=8500)