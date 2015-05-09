import os
basedir = os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'db', 'mturkdb-dev.db')

UPLOAD_FOLDER = os.path.join(basedir, 'tmp')

WTF_CSRF_ENABLED = True
SECRET_KEY = 'a5ee973e95d5812156ceb6669aa52414'
