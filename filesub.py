from flask import Flask, render_template,request,send_from_directory,url_for,redirect
from werkzeug.utils import secure_filename



app = Flask(__name__)
@app.route('/uploads/<name>')
def download_file(name):
    return send_from_directory('uploaded/rachna_artists.png', name)
@app.route('/')
def first():
    return render_template('uploads.html')
@app.route('/file_upload',methods=['GET','POST'])
def process():
    if request.method== 'POST':
        f=request.files['my_file']
        f.save(f'uploaded/{secure_filename( f.filename)}')
        return "File uplpoaded succesfully"


if __name__== '__main__':
    app.run(debug=True)
