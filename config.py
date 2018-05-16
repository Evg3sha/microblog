import os
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.env'))


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite://' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    MAIL_SERVER = os.environ.get('MAIL_SERVER') or 'smtp.mail.ru'
    MAIL_PORT = int(os.environ.get('MAIL_PORT') or 465)
    MAIL_USE_TLS = True  # os.environ.get('MAIL_USE_TLS') is not None
    MAIL_USERNAME = 'zhopa_konya@inbox.ru'  # os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = 'qwertyuiop111'  # os.environ.get('MAIL_PASSWORD')
    ADMINS = ['evgeshamsk92@gmail.com']
    POSTS_PER_PAGE = 25
    LANGUAGES = ['en', 'es']
    YA_TRANSLATOR_KEY = os.environ.get('YA_TRANSLATOR_KEY')
    ELASTICSEARCH_URL = os.environ.get('ELASTICSEARCH_URL')
