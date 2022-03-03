# -*- coding: utf-8 -*-
"""
Created on Thu Feb 17 11:12:22 2022

@author: jwang
"""

from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField,validators,BooleanField,IntegerField,TextAreaField,DateField,FieldList,SelectField,FormField,DateTimeField
from wtforms.validators import DataRequired,Length,Email,EqualTo,ValidationError
from app.models import User

class Registerform(FlaskForm):
    username = StringField('Username',validators=[DataRequired(),Length(min=1,max=20)])
    email=StringField('Email',validators=[DataRequired(),Email()])
    password = PasswordField('Password', validators=[DataRequired(),Length(min=8,max=40)])
    confirm = PasswordField('Repeat password',validators=[DataRequired(),EqualTo('password')])
    submit = SubmitField('Register')
    
    def Validate_username(self,username):
        user = User.query.filter_by(username=username).first()
        if user:
            raise ValidationError('username exist, please change a new one')

    def Validate_email(self,email):
        user = User.query.filter_by(email=email).first()
        if user:
            raise ValidationError('email exist, please change a new one')
            
class Loginform(FlaskForm):
    username = StringField('Username',validators=[DataRequired(),Length(min=1,max=20)])
    password = PasswordField('Password', validators=[DataRequired(),Length(min=8,max=40)])
    remember = BooleanField('Remember')
    submit = SubmitField('Sign in')
  
class Projetform(FlaskForm):
    projetname = StringField('Projet name',validators=[DataRequired(),Length(min=1,max=200)])
    projetid = IntegerField('Projet id', validators=[DataRequired()])
    contractno = IntegerField('Contract id', validators=[DataRequired()])
    companyref = StringField('Company ref',validators=[DataRequired(),Length(min=1,max=200)])

    
    submit = SubmitField('Add new projet info')
    
    
class Reporttaskform(FlaskForm):
    reporttaskname = SelectField('Report task',coerce=str)
    reporttasktimestart = DateTimeField('Start time(heur:minute)',format='%H:%M')
    reporttasktimeend= DateTimeField('End time(heur:minute)',format='%H:%M')
    submit = SubmitField('Add new task to report')
    
class Reportform(FlaskForm):
    reportname = StringField('Report name',validators=[DataRequired(),Length(min=1,max=200)])
    reportdate = DateField('Date:D-M-Y',format='%d-%m-%Y')
    reportoffshoreconstructionmanager = StringField('Offshore Construction Manager',validators=[DataRequired(),Length(min=1,max=200)])
    reportvesselname = StringField('Vessel name',validators=[DataRequired(),Length(min=1,max=200)])
    reportvesselmaster = StringField('Vessel Master',validators=[DataRequired(),Length(min=1,max=200)])
    reportcompanyname = StringField('Company name',validators=[DataRequired(),Length(min=1,max=200)])
    reportcompanyrepresentative = StringField('Company Representative',validators=[DataRequired(),Length(min=1,max=200)])
    reportasafety = TextAreaField('A - Safety - Summary of incidents and accidents during the last 24 hrs',validators=[DataRequired(),Length(min=1,max=1000)])
    reportlasttimeinjuries = IntegerField('Lost Time Injuries ', validators=[DataRequired()])
    reportrestrictedworkcases = IntegerField('Restricted Work Cases ', validators=[DataRequired()])
    reportmedicaltreatmentcase = IntegerField('Medical Treatment Case ', validators=[DataRequired()])
    reportfirstaidinjury = IntegerField('First Aid Injury ', validators=[DataRequired()])
    reportequipmentassetdamage = IntegerField('Equipment / Asset Damage ', validators=[DataRequired()])
    reportnearmiss = IntegerField('Near Miss ', validators=[DataRequired()])
    reporthazardobservations = IntegerField('Hazard Observations ', validators=[DataRequired()])
    reportsafetysuggestions = IntegerField('Safety Suggestions ', validators=[DataRequired()])
    reportncr = IntegerField('NCR ', validators=[DataRequired()])
    reporttaskriskassessments = IntegerField('Task Risk Assessments ', validators=[DataRequired()])
    reportdrill = IntegerField('Drill ', validators=[DataRequired()])
    reportntoolboxtalk = IntegerField('Tool Box Talk ', validators=[DataRequired()])
    reportsafetybsafecard = IntegerField('Safety B-Safe Card', validators=[DataRequired()])
    reportmanagementofchange = IntegerField('Management of Change ', validators=[DataRequired()])
    reportbsummary = TextAreaField('B - Summary Progress in previous 24 hrs',validators=[DataRequired(),Length(min=1,max=1000)])
    reportcwork = TextAreaField('C - Work Schedule for next 24 hrs ',validators=[DataRequired(),Length(min=1,max=1000)])
    #reporttask = FieldList(Reporttaskform)
    
    submit = SubmitField('Add new report')
    
class Taskform(FlaskForm):
    taskname = StringField('Task name',validators=[DataRequired(),Length(min=1,max=200)])
    submit = SubmitField('Add new task')
       