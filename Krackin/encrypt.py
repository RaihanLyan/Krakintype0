from flask import Flask,render_template,send_file,request 
import os
from flask_wtf import FlaskForm
import os
from wtforms import FileField,SubmitField
from werkzeug.utils import secure_filename
from cryptography.fernet import Fernet

app = Flask(__name__)

app.config['SECRET_KEY']='supersecretkey'
app.config['UPLOAD_FOLDER']='static/files'

if not os.path.exists(app.config['UPLOAD_FOLDER']):
     os.makedirs(app.config['UPLOAD_FOLDER'])

k_path = os.path.join(app.config['UPLOAD_FOLDER'],'mykey')
if not os.path.exists(k_path):
     key = Fernet.generate_key()
     with open(k_path,'wb') as mykey:
          mykey.write(key)

else:
     with open(k_path,'rb') as mykey:
          key = mykey.read()
     

f = Fernet(key)
class UploadFileForm(FlaskForm):
    file=FileField("File")
    submit = SubmitField("Upload file")


@app.route('/',methods=['GET',"POST"])
@app.route('/home', methods=['GET',"POST"])
def home():
    form = UploadFileForm()
    if form.validate_on_submit():
        file = form.file.data
        filename = secure_filename(file.filename)
        filesave =(os.path.join(os.path.abspath(os.path.dirname(__file__)),app.config['UPLOAD_FOLDER'],filename))
        file.save(filesave)
        with open(filesave, 'rb') as original_file:
            original = original_file.read()


        encrypted =f.encrypt(original)

        encrypted_file = f"enc_{filename}"
        encrypt_path = os.path.join(app.config['UPLOAD_FOLDER'],encrypted_file)
        with open(encrypt_path, 'wb') as enc_file:
                enc_file.write(encrypted)
        
        
        
        return f"""file has been uploaded and encypted .</h3>
        <a href="/download/{encrypted_file}">download encrypted file</a>"""
    
   
    


    return render_template('index.html',form=form)
@app.route('/download/<filename>',methods={'GET'})
def download_file(filename ):
     filepath = os.path.join(app.config['UPLOAD_FOLDER'],filename)
     if os.path.exists(filepath):
          return send_file(filepath,as_attachment=True)


if __name__ == '__main__':
    app.run(debug=True)
