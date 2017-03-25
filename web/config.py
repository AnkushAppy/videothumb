import os
basedir = os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')
SECRET_KEY = "my_secret_key"
UPLOAD_FOLDER = os.path.join(basedir, 'app/static/files')
UPLOAD_FOLDER_IMAGES = os.path.join(basedir, 'app/static/images')
ALLOWED_EXTENSIONS = set(['mpg'])
ALLOWED_EXTENSIONS_IMAGES = set(['jpeg'])





