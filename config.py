# -*- coding: utf-8 -*-
"""
Created on Thu Feb 17 10:28:10 2022

@author: jwang
"""
import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY = os.environ.get("SECRET_KEY") or  'A-VERT-LONG-SECRET-KEY'
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL") or  'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
    