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

@app.route('/', methods=['GET',"POST"])
def decrypt():
     form = UploadFileForm()
     if request.method == 'POST':
        file = form.file.data
        filename = secure_filename(file.filename)
        filesave =(os.path.join(os.path.abspath(os.path.dirname(__file__)),app.config['UPLOAD_FOLDER'],filename))
        file.save(filesave)

        with open (filesave,'rb') as encrypted_file:
            encrypted = encrypted_file.read()

        decrypted = f.decrypt(encrypted)

        decrypted_file = f"dec_{filename}"
        d_path = os.path.join(os.path.abspath(os.path.dirname(__file__)),app.config['UPLOAD_FOLDER'],filename)
        with open(d_path, 'wb') as dec_file:
                dec_file.write(decrypted)

        return f"""file has been uploaded and encypted .</h3>
        <a href="/download/{decrypted_file}">download encrypted file</a>"""
     
     return render_template('dex.html',form=form)
    



     

    


if __name__ == '__main__':
    app.run(debug=True)
