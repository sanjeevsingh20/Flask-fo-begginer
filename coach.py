from flask import Flask, render_template, request,redirect,url_for,session
from werkzeug import secure_filename

app = Flask(__name__)
app.config['uploaded']
app.config['100']

@app.route('/upload')
def upload_file():
   return render_template('uploads.html')
	
@app.route('/uploader', methods = ['GET', 'POST'])
def upload_file():
   if request.method == 'POST':
      f = request.files['file']
      f.save(secure_filename(f.upload))
      return 'file uploaded successfully'
		
if __name__ == '__main__':
   app.run(debug = True)