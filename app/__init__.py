# -*- coding: utf-8 -*-
"""
Created on Thu Feb 17 10:11:58 2022

@author: jwang
"""

from flask import Flask
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from config import Config
from flask_login import LoginManager
from flask_mail import Mail

app = Flask(__name__)
app.config.from_object(Config)

bootstrap = Bootstrap(app)
db = SQLAlchemy(app)
bcrypt=Bcrypt(app)
mail=Mail(app)
login=LoginManager(app)
login.login_view='login'
login.login_message='You must login or you can register to login '
login.login_message_category='info'


from app.routes import *

