from app import app
from flask import \
    render_template, \
    request, \
    jsonify

from helper import \
    find_images, \
    upload_file, \
    allowed_file

UPLOAD_FOLDER = app.config['UPLOAD_FOLDER']
ALLOWED_EXTENSIONS = app.config['ALLOWED_EXTENSIONS']


@app.route('/upload', methods=['POST'])
def upload():

    file = request.files['file']

    if not file:
        return jsonify(
            status="No File to Upload."
        )
    elif allowed_file(file.filename):
        return jsonify(
            status="This file extesion not allowed."
        )
    elif file and allowed_file(file.filename):
        try:
            upload_file(file)
        except:
            return jsonify(
                status="Some error occured."
            )
    else:
        return jsonify(
            status="Some error occured."
        )

    return jsonify(
        filename=file.filename,
        status="Uploaded"
    )


@app.route('/files', methods=['GET'])
def get_files():
    images = find_images()
    return jsonify(
        status='OK',
        files=images
    )


@app.route('/')
def show():
    images = find_images()
    return render_template('uploader.html',
                           files = images
                           )
