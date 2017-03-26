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
ALLOWED_SIZE = app.config['ALLOWED_SIZE']


@app.route('/upload', methods=['POST'])
def upload():

    file = request.files['file']
    size =  request.content_length

    if not file:
        print "No File to Upload."
        return jsonify(
            status="No File to Upload."
        )
    elif size > ALLOWED_SIZE:
        print "File size more then 10Mb."
        return jsonify(
            status="File size more then 10Mb."
        )
    elif not allowed_file(file.filename):
        print "This file extesion not allowed."
        return jsonify(
            status="This file extesion not allowed."
        )
    elif file and allowed_file(file.filename):
        try:
            upload_file(file)
        except:
            print "Failed to upload. Some error occured."
            return jsonify(
                status="Failed to upload. Some error occured."
            )
    else:
        print "Some error occured."
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
