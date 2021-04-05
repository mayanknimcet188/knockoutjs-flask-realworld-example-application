import os

basedir = os.path.abspath(os.path.dirname(__file__))
db_path = os.path.join(basedir,'../data-test.sqlite')

DEBUG=True
TESTING=True
SECRET_KEY='hard to guess'
SERVER_NAME='example.com'
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + db_path
SQLALCHEMY_TRACK_MODIFICATIONS=False