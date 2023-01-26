import os

from flask import Flask, redirect, render_template, request, url_for
from werkzeug.utils import secure_filename

# Folder where images are stored
UPLOAD_FOLDER = 'static/data/'

app = Flask(__name__)
app.secret_key = "Ur3a*22%^AvS4&&n8p3ag&24rf8&pf^2"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])


def allowed_file(filename):
    """Function to validate if data upload contains a allowed extensions

    Arguments:
        filename -- Filename of the file uploaded

    Returns:
        Return a bool if it allowed or not
    """
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/', methods=['GET', 'POST'])
def upload_image():
    """Function to upload a image and save in UPLOAD FOLDER with secure filename

    Returns:
        index.html rendered if method is GET and index.html with parameter filename if method is POST
    """
    if request.method == 'POST':
        if 'file' not in request.files:
            return redirect(request.url)
        file = request.files['file']
        if file.filename == '':
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return render_template('index.html', filename=filename)
        else:
            return redirect(request.url)
    else:
        return render_template('index.html')


@app.route('/display/<filename>')
def display_image(filename):
    """Function to generate url for display image

    Arguments:
        Filename

    Returns:
        redirect function
    """
    return redirect(url_for('static', filename='data/' + filename), code=301)


if __name__ == "__main__":
    app.run()
