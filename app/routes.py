# -*- coding: utf-8 -*-
"""
Created on Thu Feb 17 16:58:22 2022

@author: jwang
"""

from flask import Flask,render_template,flash,redirect,url_for,request
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from app.form import Registerform,Loginform,Projetform,Reportform,Taskform,Reporttaskform
from flask_bcrypt import Bcrypt
from app.models import User,Projet,Report,Task,Reporttask
from app import app,db,bcrypt
from flask_login import login_user,login_required,current_user,logout_user
from datetime import datetime, date
import pdfkit
from weasyprint import HTML
@app.route('/')
@login_required
def index():
    return render_template('index.html')

@app.route('/register', methods=['POST','GET'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form= Registerform()
    if form.validate_on_submit():
        username = form.username.data
        email = form.email.data
        password = bcrypt.generate_password_hash(form.password.data)
        user = User(username=username,email=email,password=password)
        db.session.add(user)
        db.session.commit()
        flash('Registion success',category='success')
        return redirect(url_for('login'))
        
    return render_template('register.html',form=form)

@app.route('/login', methods=['POST','GET'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    
    form = Loginform()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        remember = form.remember.data
        user = User.query.filter_by(username=username).first()
        if user and bcrypt.check_password_hash(user.password,password):
            login_user(user,remember=remember)
            flash('login success',category='info')
            if request.args.get('next'):
                next_page=request.args.get('next')
                return redirect(next_page)
                
            return redirect(url_for('index'))
            
        flash('user not exist or password not correct',category='danger')
                
    return render_template('login.html',form=form)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))

@app.route('/projet', methods=['GET', 'POST'])
@login_required
def projet():
    form= Projetform()
    Projets = Projet.query.all()
    if form.validate_on_submit():
        projetname = form.projetname.data
        projetid = form.projetid.data
        contractno = form.contractno.data
        companyref= form.companyref.data
       
        projet = Projet(projetid=projetid,projetname=projetname,contractno=contractno,companyref=companyref)
        db.session.add(projet)
        db.session.commit()
        flash('Register Projet success',category='success')
        return redirect(url_for('projet_task',projetname=projet.projetname))
        
    return render_template('projet.html',form=form,Projets=Projets)

  
@app.route('/projet_task/<projetname>', methods=['GET', 'POST'])
@login_required
def projet_task(projetname): 
    projet = Projet.query.filter_by(projetname=projetname).first()
    tasks = projet.tasks
    form = Taskform()
    
    if form.validate_on_submit():
        taskname = form.taskname.data
        task = Task(taskname=taskname)
        projet.tasks.append(task)
        db.session.add(task)
        db.session.commit()
        flash('Register Task success',category='success')
        return redirect(url_for('projet_task',projetname=projet.projetname))
    
    return render_template('projet_task.html',form=form,tasks=tasks,projet=projet)
                    
        


@app.route('/projet_report/<projetname>', methods=['GET', 'POST'])
@login_required
def projet_report(projetname):
    projet = Projet.query.filter_by(projetname=projetname).first()
    reports = projet.reports
    #tasklist = projet.tasks
    if projet:
        form = Reportform()
        #form.reporttask.choices=tasklist
        if form.validate_on_submit():
            reportname = form.reportname.data
            reportdate = form.reportdate.data
            reportoffshoreconstructionmanager = form.reportoffshoreconstructionmanager.data
            reportvesselname = form.reportvesselname.data
            reportvesselmaster  = form.reportvesselmaster .data
            reportcompanyname = form.reportcompanyname.data
            reportcompanyrepresentative = form.reportcompanyrepresentative.data
            reportasafety = form.reportasafety.data
            reportlasttimeinjuries = form.reportlasttimeinjuries.data
            reportrestrictedworkcases = form.reportrestrictedworkcases.data
            reportmedicaltreatmentcase  = form. reportmedicaltreatmentcase .data
            reportfirstaidinjury = form.reportfirstaidinjury.data
            reportequipmentassetdamage = form.reportequipmentassetdamage.data
            reportnearmiss = form.reportnearmiss.data
            reporthazardobservations  = form.reporthazardobservations.data
            reportsafetysuggestions = form.reportsafetysuggestions.data
            reportncr  = form.reportncr .data
            reporttaskriskassessments = form.reporttaskriskassessments.data
            reportdrill = form.reportdrill.data
            reportntoolboxtalk = form.reportntoolboxtalk.data
            reportsafetybsafecard = form.reportsafetybsafecard.data
            reportmanagementofchange = form.reportmanagementofchange.data
            reportbsummary = form.reportbsummary.data
            reportcwork = form.reportcwork.data
            #reporttask = form.reporttask.data
            reportprojetname = projet.projetname
            
            report = Report(reportname=reportname,reportdate=reportdate,reportprojetname=reportprojetname,
                            reportoffshoreconstructionmanager=reportoffshoreconstructionmanager,reportvesselname=reportvesselname,
                            reportvesselmaster=reportvesselmaster,reportcompanyname=reportcompanyname,reportcompanyrepresentative=reportcompanyrepresentative,
                            reportasafety=reportasafety,reportlasttimeinjuries=reportlasttimeinjuries,
                            reportrestrictedworkcases=reportrestrictedworkcases,reportmedicaltreatmentcase=reportmedicaltreatmentcase,
                            reportfirstaidinjury=reportfirstaidinjury,reportequipmentassetdamage=reportequipmentassetdamage,
                            reportnearmiss=reportnearmiss,reporthazardobservations=reporthazardobservations,
                            reportsafetysuggestions=reportsafetysuggestions,reportncr=reportncr,reporttaskriskassessments=reporttaskriskassessments,
                            reportdrill=reportdrill,reportntoolboxtalk=reportntoolboxtalk,reportsafetybsafecard=reportsafetybsafecard,
                            reportmanagementofchange=reportmanagementofchange,reportbsummary=reportbsummary,reportcwork=reportcwork)
                           
            projet.reports.append(report)
            db.session.add(report)
            db.session.commit()
            flash('You have created a new report',category='success')
            
        return render_template('projet_report.html',form=form,projet=projet,reports=reports)
        
    else:
        return '404'
    
    
@app.route('/report_task/<reportname>', methods=['POST','GET'])
def report_task(reportname):
    report = Report.query.filter_by(reportname=reportname).first()
    tasks = report.reporttasks
    tasklist = report.projet.tasks
    #tasklist = report.projet.tasks.taskname.all
    #projet = Projet.query.filter_by(projetname=report.projet).first()
    #tasklist = projet.tasks
    
    if report:
        form=Reporttaskform()
        form.reporttaskname.choices=tasklist
        if form.validate_on_submit():
            reporttaskname = form.reporttaskname.data
            reporttasktimestart = form.reporttasktimestart.data
            reporttasktimeend = form.reporttasktimeend.data
            reporttasktimedur = str(form.reporttasktimeend.data - form.reporttasktimestart.data)
            #reporttasktimedur = datetime.combine(date.min, form.reporttasktimeend.data) - datetime.combine(date.min, form.reporttasktimestart.data)
            reporttaskreportname = report.reportname
            report_task=Reporttask(reporttaskname=reporttaskname,reporttasktimestart=reporttasktimestart,
                                   reporttasktimeend=reporttasktimeend,reporttasktimedur=reporttasktimedur,
                                   reporttaskreportname=reporttaskreportname)
            report.reporttasks.append(report_task)
            db.session.add(report_task)
            db.session.commit()
            flash('You have created a new task to report',category='success')
            
        return render_template('report_task.html',form=form,report=report,tasks=tasks)
    
@app.route('/report/<reportname>', methods=['GET', 'POST'])
@login_required
def report(reportname, methods=['POST','GET']):
    report = Report.query.filter_by(reportname=reportname).first()

        
    
    if request.form.get('submit_button') == 'Download PDF':
        html_out= render_template('report.html',report=report)
        HTML(string=html_out).write_pdf('report.pdf')
    
        #pdfkit.from_url(render_template('report.html',report=report), 'out.pdf')
        #return render_template('report.html',report=report)
        
    return render_template('report.html',report=report)

    