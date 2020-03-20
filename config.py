import os

basedir = os.path.abspath(os.path.dirname(__file__))
SQLACHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')

SECRET_KEY = "#d#JCqTTW\nilK\\7m\x0bp#\tj~#H"
FB_APP_ID = 2308376082795952