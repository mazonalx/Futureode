from typing import Final
from app import app
from flask import render_template,flash,redirect,url_for,request, session,jsonify
from app.forms import FeedbackForm,DataForm,LoginForm
from app.forms import grades,Streams
from app.systems import Recommender1,Recommender2,Sentiment
from app.books import Books
import pickle
import random
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
            FeedQ()
            s = Sentiment(m)
            if s.SentimentAnalyzer() == "P":
                del m
                flash('Positive feedback')
                session["interest"]=0
                session["interestedstream"]=session["stream"]
                return redirect(url_for(form.stream.data))
            else:
                flash('Negative feedback') 
                session["interest"]=1
                if(form.stream.data == 'science'):
                    return redirect(url_for('negative'))
                elif(form.stream.data == 'commerce'):
                    session["interestedstream"]='Commerce'
                    return redirect(url_for('humanities'))
                else:
                    session["interestedstream"]='Humanities'
                    return redirect(url_for('humanities'))
    return render_template('explore.html',title='Explore',form=form)
@app.route('/negative',methods=['GET','POST'])
def negative():
    if request.method == "POST":
        if(request.form.get('lstream') == 'science'):
            session["interestedstream"]='Science'
            return redirect(url_for('science'))
        elif(request.form.get('lstream') == 'commerce'):
            session["interestedstream"]='Commerce'
            return redirect(url_for('commerce'))
        else:
            session["interestedstream"]='Humanities'
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
    B = Books
    S1 = B.RetSBooks()
    C1 = B.RetCBooks()
    H1 = B.RetHBooks()
    AOE=['Teaching','Photo and video editing','Photography','Dance or music','Acting or drama','Coding and programming','Blogging and content creation',
    'Computer Graphics','Writing or reading','Robotics','Flying','Content Writer','investigation','Ethical Hacking','Interior Designs','Makeup','Modelling',
    'Fitness','Youtube','Real Estate','Stock Market','Travelling','Event Planning']
    AOE.sort()
    if request.method == 'POST':
        SCB()
        if(session["R2T"]):
            r = Recommender2(session["R2T"])
            r.technical()
        if(session["R2M"]):
            r = Recommender2(session["R2M"])
            r.marketing()
        if(session["R2D"]):
            r = Recommender2(session["R2D"])
            r.design()
        if(session["R2B"]):
            r = Recommender2(session["R2B"])
            r.business()
        if(session["R2F"]):
            r = Recommender2(session["R2F"])
            r.finance()
        return redirect(url_for('social'))
    return render_template('skillcert.html',title='Skills and Certifications',S1=S1,C1=C1,H1=H1,AOE=AOE)
@app.route('/social', methods=['GET','POST'])
def social():
    if request.method == "POST": 
        SEF()
        session["teamwork"] = int(request.form.get('teamwork'))
        session["competitive"] = int(request.form.get('competitive'))
        session["leadership"] = int(request.form.get('leadership'))
        session["worklife"] = int(request.form.get('worklife'))
        session["selflearn"] = int(request.form.get('selflearn'))
        scaling()
        return redirect(url_for('recommender'))
    return render_template('social.html',title='Social')
@app.route('/recommender',methods=['GET'])
def recommender():
    R = Recommender1(session["RData"])
    if(session["interestedstream"]=='Science'):
        if(session["prediction"]==[0]):
            FINAL = R.ReadS1files()
        elif(session["prediction"]==[1]):
            FINAL = R.ReadS2files()
        else:
            FINAL = R.ReadSpecialfiles()
    elif(session["interestedstream"]=='Commerce'):
        if(session["prediction"]==[0] or session["prediction"]==[1]):
            FINAL = R.ReadCfiles()
        else:
            FINAL = R.ReadSpecialfiles()
    else:
        if(session["prediction"]==[0] or session["prediction"]==[1]):
            FINAL = R.ReadHfiles()
        else:
            FINAL = R.ReadSpecialfiles()
    return render_template('recommender.html',title='Recommender',FINAL=FINAL)
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
    if(session["moves"] > 20):
        session["mscore"]= 0
    elif(session["moves"]>= 14 and session["moves"]<= 17):
        session["mscore"] = 1
    else:
        session["mscore"] = 2
def PQ():
    pqlist=[]
    for i in ['pq1','pq2','pq3','pq4','pq5']:
        pqlist.append(int((len(session[i])/5)*100))
    session["pqscore"]=pqlist
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
def SCB():
    session["Tskills"] = request.form.getlist('Tskills')
    session["Mskills"] = request.form.getlist('Mskills')
    session["Dskills"] = request.form.getlist('Dskills')
    session["Bskills"] = request.form.getlist('Bskills')
    session["Fskills"] = request.form.getlist('Fskills')
    session["oTskills"]=request.form.get('oTskills')
    session["oMskills"]=request.form.get('oMskills')
    session["oDskills"]=request.form.get('oDskills')
    session["oFskills"]=request.form.get('oFskills')
    session["oBskills"]=request.form.get('oBskills')
    session["certifications"]=request.form.get('certifications')
    if(session["certifications"]):
        session["certif"]=1
    else:
        session["certif"]=0#confirm this
    print("Certification",session["certif"])
    session["aoe"]=request.form.getlist('aoe')
    session["oaoe"]=request.form.get('oaoe')  
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
            Humanitiesbooklist.append("c{}{}".format(i,j))
    for i in Sciencebooklist:
        if(request.form.get(i)):
            R1+=request.form.get(i)+" "
    for j in Commercebooklist:
        if(request.form.get(j)):
            R1+=request.form.get(j)+" "
    for k in Humanitiesbooklist:
        if(request.form.get(k)):
            R1+=request.form.get(k)+" "
    R2=""
    AoE=""
    AoE= ' '.join(str(e) for e in session["aoe"])
    R2T = ' '.join(str(e) for e in session["Tskills"])
    R2T+=" "+session["oTskills"]
    session["R2T"]=R2T+AoE
    R2M = ' '.join(str(e) for e in session["Mskills"])
    R2M+=" "+session["oMskills"]
    session["R2M"]=R2M+AoE
    R2D = ' '.join(str(e) for e in session["Dskills"])
    R2D+=" "+session["oDskills"]
    session["R2D"]=R2D+AoE
    R2B = ' '.join(str(e) for e in session["Bskills"])
    R2B+=" "+session["oBskills"]
    session["R2B"]=R2B+AoE
    R2F = ' '.join(str(e) for e in session["Fskills"])
    R2F+=" "+session["oFskills"]
    session["R2F"]=R2F+AoE
    R2+=" "+R2T+R2M+R2D+R2B+R2F
    R2+=" "+session["oaoe"]
    R2+=" "+AoE
    session["RData"]=R1+R2
def FeedQ():
    global m
    p=0
    n=0
    L4 =('q1','q2','q3','q4','q5','q6','q7')
    for i in L4:
        if(int(request.form.get(i))==0 or int(request.form.get(i))==2):
            p+=1
        else:
            n+=1
    m=request.form.get("q8")
    session["satisfaction"]=(p*100)//7
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
    if(session["interestedstream"]=='Science'):
        pickle_in = open('app/models/science_model.pkl', 'rb')
    elif(session["interestedstream"]=='Commerce'):
        pickle_in = open('app/models/commerce_model.pkl', 'rb')
    else:
        pickle_in = open('app/models/humanities_model.pkl', 'rb')
    classifier = pickle.load(pickle_in)
    prediction = classifier.predict(INPUT)
    session["prediction"]=prediction
    print(session["prediction"])