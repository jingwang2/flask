# -*- coding: utf-8 -*-
"""
Created on Thu Feb 17 10:35:17 2022

@author: jwang
"""
#from app import db
from flask_login import UserMixin
from app import db,login
from datetime import datetime

@login.user_loader
def load_user(user_id):
    return User.query.filter_by(id=user_id).first()

class User(db.Model,UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100),unique=True,nullable=False)
    password = db.Column(db.String(120),unique=False,nullable=False)
    email = db.Column(db.String(200),unique=True,nullable=False)
    
    def __repr__(self):
        return '<User %r>' % self.username
    
class Projet(db.Model,UserMixin):
    projetid = db.Column(db.Integer, primary_key=True)
    projetname = db.Column(db.String(100),unique=True,nullable=False)
    contractno = db.Column(db.Integer,unique=False,nullable=False)
    companyref = db.Column(db.String(200),unique=False,nullable=False)
  
    reports = db.relationship('Report', backref=db.backref('projet',lazy=True,uselist=False))
    tasks = db.relationship('Task', backref=db.backref('projet',lazy=True,uselist=False))
   
    def __repr__(self):
        return '<Projet %r>' % self.projetname
    
class Report(db.Model):
    reportid = db.Column(db.Integer, primary_key=True)
    reportname = db.Column(db.String(100),unique=False,nullable=False) 
    reportdate = db.Column(db.DateTime,default=datetime.utcnow)
    reportoffshoreconstructionmanager = db.Column(db.String(140),unique=False,nullable=False)
    reportvesselname = db.Column(db.String(140),unique=False,nullable=False)
    reportvesselmaster = db.Column(db.String(140),unique=False,nullable=False)
    reportcompanyname = db.Column(db.String(140),unique=False,nullable=False)
    reportcompanyrepresentative = db.Column(db.String(140),unique=False,nullable=False)
    reportasafety = db.Column(db.String(1000),unique=False,nullable=False)
    reportlasttimeinjuries = db.Column(db.Integer)
    reportrestrictedworkcases = db.Column(db.Integer)
    reportmedicaltreatmentcase = db.Column(db.Integer)
    reportfirstaidinjury = db.Column(db.Integer)
    reportequipmentassetdamage = db.Column(db.Integer)
    reportnearmiss = db.Column(db.Integer)
    reporthazardobservations = db.Column(db.Integer)
    reportsafetysuggestions = db.Column(db.Integer)
    reportncr = db.Column(db.Integer)
    reporttaskriskassessments = db.Column(db.Integer)
    reportdrill = db.Column(db.Integer)
    reportntoolboxtalk = db.Column(db.Integer)
    reportsafetybsafecard = db.Column(db.Integer)
    reportmanagementofchange = db.Column(db.Integer)
    reportbsummary = db.Column(db.String(1000),unique=False,nullable=False)
    reportcwork = db.Column(db.String(1000),unique=False,nullable=False)
    reportprojetname = db.Column(db.String(100),db.ForeignKey('projet.projetname'),nullable=False)
    
    reporttasks = db.relationship('Reporttask', backref=db.backref('report',lazy=True,uselist=False))
    
    
    def __repr__(self):
        return '<Report %r>' % self.reportname

  
class Task(db.Model):
    taskid = db.Column(db.Integer, primary_key=True)
    taskname = db.Column(db.String(100),unique=False,nullable=False) 
    taskprojetname = db.Column(db.String(100),db.ForeignKey('projet.projetname'),nullable=False)
    
    def __repr__(self):
        return '<Task %r>' % self.taskname
    
    
class Reporttask(db.Model):
    reporttaskid = db.Column(db.Integer, primary_key=True)
    reporttaskname = db.Column(db.String(100),unique=False,nullable=False) 
    reporttasktimestart = db.Column(db.DateTime,default=datetime.utcnow)
    reporttasktimeend = db.Column(db.DateTime,default=datetime.utcnow)
    reporttasktimedur = db.Column(db.String(100),default=datetime.utcnow)
    reporttaskreportname = db.Column(db.String(100),db.ForeignKey('report.reportname'),nullable=False)
    
    def __repr__(self):
        return '<Task %r>' % self.reporttaskname
    

    