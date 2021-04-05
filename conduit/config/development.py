import os

basedir = os.path.abspath(os.path.dirname(__file__))
db_path = os.path.join(basedir,'../data-dev.sqlite')

DEBUG=True
SECRET_KEY='hard to guess'

SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URI') or 'sqlite:///' + db_path
SQLALCHEMY_TRACK_MODIFICATIONS=False