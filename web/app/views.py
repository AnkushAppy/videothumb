from app import app
from flask import \
    render_template, \
    request, \
    jsonify

from helper import \
    find_images_among_files, \
    upload_file, \
    allowed_file

UPLOAD_FOLDER = app.config['UPLOAD_FOLDER']
ALLOWED_EXTENSIONS = app.config['ALLOWED_EXTENSIONS']


@app.route('/upload', methods=['POST'])
def upload():

    file = request.files['file']
    if file and allowed_file(file.filename):
        upload_file(file)

    return jsonify(
        filename=file.filename,
        status="Uploaded"
    )


@app.route('/files', methods=['GET'])
def get_files():
    images = find_images_among_files()
    return jsonify(
        files=images
    )


@app.route('/')
def show():
    images = find_images_among_files()
    return render_template('uploader.html',
                           files = images
                           )
