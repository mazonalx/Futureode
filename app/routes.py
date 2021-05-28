from app import app
from flask import render_template,flash,redirect,url_for,request, session,jsonify
from app.forms import FeedbackForm,DataForm,SkillCertBookForm,LoginForm
from app.forms import grades,Streams
from app.systems import Recommender,Sentiment
from app.books import Books
import pickle
import random
import itertools
@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html',title='Home')
@app.route('/login',methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        session["name"] = request.form.get("name")
        session["uname"] = str(request.form.get("uname"))
        return redirect(url_for('explore'))
    return render_template('login.html',title='Login',form=form)
@app.route('/explore',methods=['GET','POST'])
def explore():#Feedback
    global m
    m=""
    form = FeedbackForm()
    if form.validate_on_submit():
        if request.method == "POST":
            session["stream"] = dict(Streams).get(form.stream.data)
            FeedQ1()
            s = Sentiment(m)
        if s.SentimentAnalyzer() == "P":
            del m
            flash('Positive feedback')
            session["interest"]=0
            return redirect(url_for(form.stream.data))
        else:
            flash('Negative feedback')
            session["interest"]=1
            if(form.stream.data == 'science'):
                return redirect(url_for('negative'))
            elif(form.stream.data == 'commerce'):
                return redirect(url_for('humanities'))
            else:
                return redirect(url_for('humanities'))
    return render_template('explore.html',title='Explore',form=form)
@app.route('/negative',methods=['GET','POST'])
def negative():
    if request.method == "POST":
        if(request.form.get('lstream') == 'commerce'):
            return redirect(url_for('commerce'))
        else:
            return redirect(url_for('humanities'))
    return render_template('negative.html',title='Negative Response')
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
    form = SkillCertBookForm()
    B = Books
    S1 = B.RetSBooks()
    C1 = B.RetCBooks()
    H1 = B.RetHBooks()
    if form.validate_on_submit():
        SCB(form)
        return redirect(url_for('social'))
    return render_template('skillcert.html',form=form,title='Skills and Certifications',S1=S1,C1=C1,H1=H1)
@app.route('/social', methods=['GET','POST'])
def social():
    if request.method == "POST":
        session["satisfaction"] = int(request.form.get('satisfaction'))
        SEF()
        session["teamwork"] = int(request.form.get('teamwork'))
        session["competitive"] = int(request.form.get('competitive'))
        session["leadership"] = int(request.form.get('leadership'))
        session["worklife"] = int(request.form.get('worklife'))
        session["certif"] = int(request.form.get('certif'))
        session["selflearn"] = int(request.form.get('selflearn'))
        scaling()
        session["intesub"] = request.form.get('ins')
        session["intefld"] = request.form.get('inf')
        r = Recommender(session["intesub"])
        if(session["intefld"] == 'Business'):
            r.business()
        elif(session["intefld"] == 'Designing'):
            r.design()
        elif(session["intefld"] == 'Finance'):
            r.finance()
        elif(session["intefld"] == 'Marketing'):
            r.marketing()
        else:
            r.technical()
        return redirect(url_for('recommender'))
    return render_template('social.html',title='Social')
@app.route('/recommender',methods=['GET','POST'])
def recommender():
    return render_template('recommender.html',title='Recommender')
@app.route("/logout")
def logout():
    session["uname"] = None
    for key in list(session.keys()):
        session.pop(key)
    return redirect("/")
def IQ():
    correct = 0
    L2 =('iq1','iq2','iq3','iq4','iq5','iq6','iq7','iq8','iq9','iq10')
    L3 =('A','B','E','B','A','C','B','B','E','10')
    for i,j in zip(L2,L3):
        if(request.form.get(i) == j):
            correct += 1
    session["iqscore"] = (140*correct)//10 # IQ score
def MeM():
    session["moves"] = int(request.form.get('moves'))
    if(session["moves"] > 69):
        session["mscore"]= 0
    elif(session["moves"]>= 45 and session["moves"]<= 69):
        session["mscore"] = 1
    else:
        session["mscore"] = 2
def PQ():
    pqlist=[]
    for i in ['pq1','pq2','pq3','pq4','pq5']:
        pqlist.append(int((len(session[i])/5)*100))
    session["pqscore"]=pqlist#Personality Score
def Test(form):
    Dg= dict(grades)
    session["sub1"] = Dg.get(form.sub1.data)
    session["sub2"] = Dg.get(form.sub2.data)
    session["sub3"] = Dg.get(form.sub3.data)
    session["sub4"] = Dg.get(form.sub4.data)
    session["sub5"] = Dg.get(form.sub5.data)
    session["sub6"] = Dg.get(form.sub6.data)
    MeM()
    IQ()
    PQlist=['pq1', 'pq2', 'pq3', 'pq4','pq5']
    for x in PQlist:
        session[x] = request.form.getlist(x)
    PQ()
def SCB(form):
    session["skills"]=form.skills.data
    session["skills_oth"]=form.skill_oth.data
    session["certifications"]=form.certifications.data
    session["certifications_oth"]=form.certifications_oth.data
    session["aoe"]=form.aoe.data
    session["aoe_oth"]=form.aoe_oth.data   
    Sciencebooklist = []
    Commercebooklist = []
    Humanitiesbooklist = []
    R1=""
    for i in range(1,13):
        for j in range(1,3):
            Sciencebooklist.append("b{}{}".format(i,j))
    for i in range(1,9):
        for j in range(1,3):
            Commercebooklist.append("c{}{}".format(i,j))
    for i in range(1,8):
        for j in range(1,3):
            Commercebooklist.append("c{}{}".format(i,j))
    for i in Sciencebooklist:
        if(request.form.get(i)):
            R1+=request.form.get(i)+" "
    R1+=" "
    for j in Commercebooklist:
        if(request.form.get(j)):
            R1+=request.form.get(j)+" "
    for k in Humanitiesbooklist:
        if(request.form.get(k)):
            R1+=request.form.get(k)+" "
    R2=""
    C = session["skills"]+session["certifications"]+session["aoe"]
    for i in C:
        R2+=i+" "
    R2+=session["skills_oth"]+" "+session["certifications_oth"]+" "+session["aoe_oth"]
    session["RData"]=R1+R2
def FeedQ2(x,y):
    global m
    if(request.form.get(x) == 'Other'):
        m+=request.form.get(y)
    elif(request.form.get(y)):
        m+=request.form.get(y)
    else:
        m+=request.form.get(x)
def FeedQ1():
    L4 =('q1','q2','q3','q4','q5','q6','q7','q8')
    L5 =('q11','q22','q33','q44','q55','q66','q77','q88')
    for i,j in zip(L4,L5):
        FeedQ2(i,j)
def SEF():
    if(request.form.get('sef') == 'Other'):
        session["sef"] = int(request.form.get('sef1'))
    elif(request.form.get('sef1')):
        session["sef"] = int(request.form.get('sef1'))
    else:
        session["sef"] = int(request.form.get('sef'))
def scaling():
    S=[]
    for y in ['sub1', 'sub2', 'sub3','sub4','sub5','sub6']:
        if(session[y]=='D'):
            S.append(random.randrange(45,60,1))
        elif(session[y]=='C'):
            S.append(random.randrange(60,70,1))
        elif(session[y]=='B'):
            S.append(random.randrange(70,75,1))
        elif(session[y]=='B+'):
            S.append(random.randrange(75,85,1))
        elif(session[y]=='A'):
            S.append(random.randrange(85,90,1))
        elif(session[y]=='A+'):
            S.append(random.randrange(90,100,1))
        else:
            S.append(0)
    INPUT=[[session["iqscore"],S[0],S[1],S[2],S[3],S[4],S[5],session["pqscore"][0],session["pqscore"][1],session["pqscore"][2],session["pqscore"][3],session["pqscore"][4],session["interest"],session["satisfaction"],session["sef"],session["mscore"],session["teamwork"],session["competitive"],session["leadership"],session["worklife"],session["certif"],session["selflearn"]]]
    prediction(INPUT)
def prediction(INPUT):
    if(session["stream"]=='Science'):
        pickle_in = open('app/models/science_model.pkl', 'rb')
    elif(session["stream"]=='Commerce'):
        pickle_in = open('app/models/commerce_model.pkl', 'rb')
    else:
        pickle_in = open('app/models/humanities_model.pkl', 'rb')
    classifier = pickle.load(pickle_in)
    prediction = classifier.predict(INPUT)
    #return prediction
    print(prediction)