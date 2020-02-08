from flask import Flask, render_template, url_for, request, redirect, config
from werkzeug.utils import secure_filename

app = Flask(__name__)


posts = [
    {
        'author': 'Pepe',
        'title': 'PepePost1'
    }

]

import os


app.config["IMAGE_UPLOADS"]="/home/ec2-user/pneumonia_ML/static"

@app.route('/')
@app.route('/home') # Root page of a website
def home():
    return render_template('home.html', posts=posts)


@app.route('/upload-image', methods=['GET', 'POST'])
def upload_image():
    if request.method == "POST":
            if request.files:
                f = request.files['file']
                sfname='static/images/' + str(secure_filename(f.filename))
                f.save(os.path.join(app.config["IMAGE_UPLOADS"], secure_filename(f.filename)))
                return render_template('results.html', imgpath=sfname)

    return render_template('upload_image.html', title='Upload')






@app.route('/contact')
def contact():
    return render_template('contact.html')


if __name__ == '__main__':
    app.run('0.0.0.0',debug=1) # Debug mode activated



