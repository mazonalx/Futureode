from app import app
from flask import render_template,flash,redirect,url_for,request, session
from flask_session import Session
from app.forms import FeedbackForm,DataForm,SkillCertForm,LoginForm
from app.forms import grades,Streams
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import nltk,joblib,pickle
   

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html',title='Home')
@app.route('/login',methods=['GET','POST'])
def login():
    form = LoginForm()
    if request.method == "POST":
        session["uname"] = str(request.form.get("uname"))
        return redirect(url_for('explore'))
    return render_template('login.html',title='Login',form=form)
@app.route('/explore',methods=['GET','POST'])
def explore():#Feedback
    form = FeedbackForm()
    if form.validate_on_submit():
        if request.method == "POST":
            session["stream"] = dict(Streams).get(form.stream.data)
            #session["feedback"] = str(request.form.get("feedback"))
        if SentimentAnalyzer(form) == "P":
            flash('Positive feedback')
            return redirect(url_for(form.stream.data))
        else:
            flash('Negative feedback')
    return render_template('explore.html',title='Explore',form=form)
@app.route('/science',methods=['GET','POST'])
def science():
    form = DataForm()
    if form.validate_on_submit():
        if request.method == "POST":
            Test(form)
        return redirect(url_for('skillcert'))
    return render_template('science.html',title='Science',form=form)
@app.route('/commerce',methods=['GET','POST']) 
def commerce():
    form = DataForm()
    if form.validate_on_submit():
        if request.method == "POST":
            Test(form)
        return redirect(url_for('skillcert')) 
    return render_template('commerce.html',title='Commerce',form=form)
@app.route('/humanities',methods=['GET','POST'])
def humanities():
    form = DataForm()
    if form.validate_on_submit():
        if request.method == "POST":
            Test(form)
        return redirect(url_for('skillcert'))
    return render_template('humanities.html',title='Humanities',form=form)
@app.route('/skillcert',methods=['GET','POST'])
def skillcert():
    form = SkillCertForm()
    if form.validate_on_submit():
        if request.method == "POST":
            session["skill"] = request.form.get('skill')
            session["certifications"] = request.form.get('certifications')
        return redirect(url_for('result'))
    return render_template('skillcert.html',form=form,title='Skills and Certifications')
@app.route('/result')
def result():
    return render_template('result.html',title='Result')
@app.route("/logout")
def logout():
    session["uname"] = None
    return redirect("/")
def IQ(q1,q2):
    if(request.form.get(q1) == q2):
        session[q1] = q2
    else:
        session[q1] = request.form.get(q1)
def Test(form):
    Dg= dict(grades)
    session["sub1"] = Dg.get(form.sub1.data)
    session["sub2"] = Dg.get(form.sub2.data)
    session["sub3"] = Dg.get(form.sub3.data)
    session["sub4"] = Dg.get(form.sub4.data)
    session["sub5"] = Dg.get(form.sub5.data)
    session["sub6"] = Dg.get(form.sub6.data)
    L2 =('iq1','iq2','iq3','iq4','iq5','iq6','iq7','iq8','iq9','iq10')
    L3 =('A','B','E','B','A','C','B','B','E','10')
    for i,j in zip(L2,L3):
        IQ(i,j)
    session["pq1"] = request.form.getlist('pq1')
    session["pq2"] = request.form.getlist('pq2')
    session["pq3"] = request.form.getlist('pq3')
    session["pq4"] = request.form.getlist('pq4')
    session["pq5"] = request.form.getlist('pq5')
def SentimentAnalyzer(form):
    vader=SentimentIntensityAnalyzer()
    m=request.form['feedback']
    data=m.lower()
            # Remove Punctuations
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    data_after_clean=""
    for char in data:
        if char not in punctuations:
            data_after_clean = data_after_clean + char
    pos=0
    neg=0
    flag=0
    res = data_after_clean.split()
    for i in res:
        #Negation Handling
        if(i=='not'):
            flag=1      
        k=vader.polarity_scores(i)
        if(k['compound']>=0.05):
            pos=pos+1
        elif(k['neu']==1 or k['compound']==0):
            continue
        else:
            neg=neg+1
    if(pos>neg and flag==1):
        neg=pos+1
        flag=0
    if(neg>pos and flag==1):
        pos=neg+1
        flag=0
    if(pos>neg):
        return "P" 
    else:
        return "Q"

