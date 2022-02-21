from flask import Flask
from flask_mail import Mail
from .config import Config

app = Flask(__name__)
app.config.from_object(Config)

app.config['SECRET_KEY'] = 'removed'
app.config['MAIL_SERVER'] = 'smtp.mailtrap.io'
app.config['MAIL_PORT'] = '2525'
app.config['MAIL_USERNAME'] = 'removed'
app.config['MAIL_PASSWORD'] = 'removed'

mail = Mail(app)
from app import views

