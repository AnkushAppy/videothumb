from app import app
from ffvideo import VideoStream
from werkzeug import secure_filename
import os
import PIL
from PIL import Image

ALLOWED_EXTENSIONS = app.config['ALLOWED_EXTENSIONS']
ALLOWED_EXTENSIONS_IMAGES = app.config['ALLOWED_EXTENSIONS_IMAGES']
UPLOAD_FOLDER_IMAGES = app.config['UPLOAD_FOLDER_IMAGES']
UPLOAD_FOLDER = app.config['UPLOAD_FOLDER']
MAX_CONTENT_LENGTH = app.config['MAX_CONTENT_LENGTH']


def allowed_file(filename):
    if '.' in filename and filename.split('.', 1)[1] in ALLOWED_EXTENSIONS:
        return True

def allowed_size(file):
    if file.size < MAX_CONTENT_LENGTH:
        return True
    return False


def create_thumbmail(filename, imagename):
    vs = VideoStream(filename,
                     frame_size=(128, None),  # scale to width 128px
                     frame_mode='L' # convert to grayscale
                     )
    image_name = imagename.split('.')[0]
    frame = vs.get_frame_at_sec(2)
    img = frame.image()
    img = img.resize((300,300), PIL.Image.ANTIALIAS)
    img.save('{0}.jpeg'.format(image_name))


def upload_file(file):
    filename = secure_filename(file.filename)
    full_pathname = os.path.join(UPLOAD_FOLDER, filename)
    full_pathname_image = os.path.join(UPLOAD_FOLDER_IMAGES, filename)
    file.save(full_pathname)
    create_thumbmail(full_pathname, full_pathname_image)


def print_info(vs):
    print '-' * 20
    print "codec: %s" % vs.codec_name
    print "duration: %.2f" % vs.duration
    print "bit rate: %d" % vs.bitrate
    print "frame size: %dx%d" % (vs.frame_width, vs.frame_height)
    print "frame_mode: %s" % vs.frame_mode


def find_images():

    file_list = os.listdir(UPLOAD_FOLDER_IMAGES)
    only_images = []
    for file in file_list:
        ext = file.split('.', 1)[1]
        if ext in ALLOWED_EXTENSIONS_IMAGES:
            imagename = app.config['UPLOAD_FOLDER_IMAGES'] + '/' + file
            only_images.append(file)

    return only_images
