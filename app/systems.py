import numpy as np
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import CountVectorizer
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from flask import session
import re
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem.snowball import SnowballStemmer
class Recommender2:
    def __init__(self,inp1):
        self.inp1 = inp1
    def business(self):
        data=pd.read_csv('app/csv/udemy_business.csv')
        count=0
        Course =[]
        for i in range(0,9969):
            k=str(data['Title'][i])
            l=str(data['Summary'][i])
            new_data=k+' '+l
        
            data_s=new_data
            pattern = r'[0-9]'
            data_s = re.sub(pattern, '', data_s)
        
            text=[self.inp1,data_s]
            cv=CountVectorizer()
            count_matrix=cv.fit_transform(text)
            sim_score=cosine_similarity(count_matrix)
            if(sim_score[0][1]>0.3 and count<5):
                Course.append([])
                Course[count].append(data['Title'][i])
                Course[count].append(data['Stars'][i])
                Course[count].append(str(round(sim_score[0][1]*100,)))
                count=count+1
        session["CBdata"]=Course
    def design(self):
        data=pd.read_csv('app/csv/udemy_design.csv')
        count=0
        Course =[]
        for i in range(0,9961):
            k=str(data['Title'][i])
            l=str(data['Summary'][i])
            new_data=k+' '+l
        
            data_s=new_data
            pattern = r'[0-9]'
            data_s = re.sub(pattern, '', data_s)
        
            text=[self.inp1,data_s]
            cv=CountVectorizer()
            count_matrix=cv.fit_transform(text)
            sim_score=cosine_similarity(count_matrix)
            if(sim_score[0][1]>0.3 and count<5):
                Course.append([])
                Course[count].append(data['Title'][i])
                Course[count].append(data['Stars'][i])
                Course[count].append(str(round(sim_score[0][1]*100,)))
                count=count+1
        session["CDdata"]=Course
    def finance(self):
        data=pd.read_csv('app/csv/udemy_finance.csv')
        count=0
        Course=[]
        for i in range(0,5886):
            k=str(data['Title'][i])
            l=str(data['Summary'][i])
            new_data=k+' '+l
        
            data_s=new_data
            pattern = r'[0-9]'
            data_s = re.sub(pattern, '', data_s)
        
            text=[self.inp1,data_s]
            cv=CountVectorizer()
            count_matrix=cv.fit_transform(text)
            sim_score=cosine_similarity(count_matrix)
            if(sim_score[0][1]>0.3 and count<5):
                Course.append([])
                Course[count].append(data['Title'][i])
                Course[count].append(data['Stars'][i])
                Course[count].append(str(round(sim_score[0][1]*100,)))
                count=count+1
        session["CFdata"]=Course
    def marketing(self):
        data=pd.read_csv('app/csv/udemy_marketing.csv')
        count=0
        Course=[]
        for i in range(0,8787):
            k=str(data['Title'][i])
            l=str(data['Summary'][i])
            new_data=k+' '+l
        
            data_s=new_data
            pattern = r'[0-9]'
            data_s = re.sub(pattern, '', data_s)
        
            text=[self.inp1,data_s]
            cv=CountVectorizer()
            count_matrix=cv.fit_transform(text)
            sim_score=cosine_similarity(count_matrix)
            if(sim_score[0][1]>0.3 and count<5):
                Course.append([])
                Course[count].append(data['Title'][i])
                Course[count].append(data['Stars'][i])
                Course[count].append(str(round(sim_score[0][1]*100,)))
                count=count+1
        session["CMdata"]=Course
    def technical(self):
        data=pd.read_csv('app/csv/udemy_tech.csv')
        count=0
        Course=[]
        for i in range(0,9963):
            k=str(data['Title'][i])
            l=str(data['Summary'][i])
            new_data=k+' '+l
        
            data_s=new_data
            pattern = r'[0-9]'
            data_s = re.sub(pattern, '', data_s)
        
            text=[self.inp1,data_s]
            cv=CountVectorizer()
            count_matrix=cv.fit_transform(text)
            sim_score=cosine_similarity(count_matrix)
            if(sim_score[0][1]>0.3 and count<5):
                Course.append([])
                Course[count].append(data['Title'][i])
                Course[count].append(data['Stars'][i])
                Course[count].append(str(round(sim_score[0][1]*100,)))
                count=count+1
        session["CTdata"]=Course      
class Recommender1:
    def __init__(self,INP):
        self.INP = INP
    def ReadS1files(self):
        with open('app/recommenderfiles/SCIENCE/AERO.txt', encoding="utf8") as file:
            aero = file.read()
        with open('app/recommenderfiles/SCIENCE/ARCHI.txt', encoding="utf8") as file:
            archi= file.read()
        with open('app/recommenderfiles/SCIENCE/AUTOM.txt', encoding="utf8") as file:
            autom= file.read()
        with open('app/recommenderfiles/SCIENCE/BIOMED.txt', encoding="utf8") as file:
            biomed= file.read()
        with open('app/recommenderfiles/SCIENCE/ME.txt', encoding="utf8") as file:
            me= file.read()
        with open('app/recommenderfiles/SCIENCE/CE.txt', encoding="utf8") as file:
            ce= file.read()
        with open('app/recommenderfiles/SCIENCE/CHE.txt', encoding="utf8") as file:
            che= file.read()
        with open('app/recommenderfiles/SCIENCE/CSE.txt', encoding="utf8") as file:
            cse= file.read()
        with open('app/recommenderfiles/SCIENCE/ECE.txt', encoding="utf8") as file:
            ece= file.read()
        with open('app/recommenderfiles/SCIENCE/EEE.txt', encoding="utf8") as file:
            eee= file.read()
        with open('app/recommenderfiles/SCIENCE/ENV.txt', encoding="utf8") as file:
            env= file.read()
        with open('app/recommenderfiles/SCIENCE/B.SC.txt', encoding="utf8") as file:
            bsc= file.read()
        SR1={"AERONAUTICAL":self.CosineSim(aero),"ARCHITECTURAL":self.CosineSim(archi),"AUTOMOBILE":self.CosineSim(autom),
        "BIOMEDICAL":self.CosineSim(biomed),"MECHANICAL ENGINEERING":self.CosineSim(me),"CIVIL":self.CosineSim(ce),
        "CHEMICAL":self.CosineSim(che),"COMPUTER SCIENCE":self.CosineSim(cse),"ELECTRONICS AND COMMUNICATION":self.CosineSim(ece),
        "ELECTRICAL AND ELECTRONICS":self.CosineSim(eee),"ENVIRONMENTAL":self.CosineSim(env),"B.SC":self.CosineSim(bsc),
        "MBBS":self.CosineSim(mbbs),"NURSING":self.CosineSim(nurs),"BACHELOR OF DENTAL SURGERY":self.CosineSim(bds),
        "Bachelor of Ayurveda, Medicine, and Surgery":self.CosineSim(bams),"Bachelor of Pharmacy":self.CosineSim(bpharm)
        }
        SSR1 = sorted(SR1.items(), key=lambda x:x[1],reverse=True)
        RS1=[]
        for i in range(4):
            RS1.append(SSR1[i][0])
        return RS1
    def ReadS2files(self):
        with open('app/recommenderfiles/SCIENCE/MBBS.txt', encoding="utf8") as file:
            mbbs= file.read()
        with open('app/recommenderfiles/SCIENCE/NURSING.txt', encoding="utf8") as file:
            nurs= file.read()
        with open('app/recommenderfiles/SCIENCE/BDS.txt', encoding="utf8") as file:
            bds= file.read()
        with open('app/recommenderfiles/SCIENCE/BAMS.txt', encoding="utf8") as file:
            bams= file.read()
        with open('app/recommenderfiles/SCIENCE/BPHARM.txt', encoding="utf8") as file:
            bpharm= file.read()
        SR2={"MBBS":self.CosineSim(mbbs),"NURSING":self.CosineSim(nurs),"BACHELOR OF DENTAL SURGERY":self.CosineSim(bds),
            "Bachelor of Ayurveda, Medicine, and Surgery":self.CosineSim(bams),"Bachelor of Pharmacy":self.CosineSim(bpharm)
            }
        SSR2 = sorted(SR2.items(), key=lambda x:x[1],reverse=True)
        RS2=[]
        for i in range(4):
            RS2.append(SSR2[i][0])
        return RS2
    def ReadCfiles(self):
        with open('app/recommenderfiles/COMMERCE/STCS.txt', encoding="utf8") as file:
            stcs= file.read()
        with open('app/recommenderfiles/COMMERCE/TOTRM.txt', encoding="utf8") as file:
            totrm= file.read()
        with open('app/recommenderfiles/COMMERCE/BUAD.txt', encoding="utf8") as file:
            buad= file.read()
        with open('app/recommenderfiles/COMMERCE/MAIF.txt', encoding="utf8") as file:
            maif= file.read()
        with open('app/recommenderfiles/COMMERCE/MARK.txt', encoding="utf8") as file:
            mark= file.read()
        with open('app/recommenderfiles/COMMERCE/BAFI.txt', encoding="utf8") as file:
            bafi= file.read()
        with open('app/recommenderfiles/COMMERCE/ACC.txt', encoding="utf8") as file:
            acc= file.read()
        with open('app/recommenderfiles/COMMERCE/ACTA.txt', encoding="utf8") as file:
            acta= file.read()
        with open('app/recommenderfiles/COMMERCE/APPE.txt', encoding="utf8") as file:
            appe= file.read()
        CR={
            "BCom in STATISTICS":self.CosineSim(stcs),"BCom in TOURISM & TRAVEL MANAGEMENT":self.CosineSim(totrm),
            "BCom in BUSINESS & ADMINISTRATION":self.CosineSim(buad),"BCom in MANAGEMENT ACCOUNTING & INTERNATIONAL FINANCE":self.CosineSim(maif),
            "BCom in MARKETING":self.CosineSim(mark),"BCom in BANKING & FINANCE":self.CosineSim(bafi),
            "BCom in ACCOUNTING":self.CosineSim(acc),"BCom in ACCOUNTING & TAXATION":self.CosineSim(acta),
            "BCom in APPLIED ECONOMICS":self.CosineSim(appe)
            }
        SCR = sorted(CR.items(), key=lambda x:x[1],reverse=True)
        RC=[]
        for i in range(4):
            RC.append(SCR[i][0])
        return RC
    def ReadHfiles(self):
        with open('app/recommenderfiles/HUMANITIES/BA.txt', encoding="utf8") as file:
            ba= file.read()
        with open('app/recommenderfiles/HUMANITIES/BFA.txt', encoding="utf8") as file:
            bfa= file.read()
        with open('app/recommenderfiles/HUMANITIES/BBA.txt', encoding="utf8") as file:
            bba= file.read()
        with open('app/recommenderfiles/HUMANITIES/BALLB.txt', encoding="utf8") as file:
            ballb= file.read()
        with open('app/recommenderfiles/HUMANITIES/BJM.txt', encoding="utf8") as file:
            bjm= file.read()
        with open('app/recommenderfiles/HUMANITIES/BFD.txt', encoding="utf8") as file:
            bfd= file.read()
        with open('app/recommenderfiles/HUMANITIES/BHM.txt', encoding="utf8") as file:
            bhm= file.read()
        HR={
            "Bachelor of Arts":self.CosineSim(ba),"Bachelor of Fine Arts":self.CosineSim(bfa),
            "Bachelor of Business Administration":self.CosineSim(bba),"Integrated Law course(B.A + L.L.B.)":self.CosineSim(ballb),
            "Bachelor of Journalism and Mass Communication":self.CosineSim(bjm),"Bachelor of Fashion Design":self.CosineSim(bfd),
            "Bachelor of Hotel Management":self.CosineSim(bhm)
            }
        SHR = sorted(HR.items(), key=lambda x:x[1],reverse=True)
        RH=[]
        for i in range(4):
            RH.append(SHR[i][0])
        return RH
    def ReadSpecialfiles(self):
        with open('app/recommenderfiles/SPECIAL/CP.txt', encoding="utf8") as file:
            cp= file.read()
        with open('app/recommenderfiles/SPECIAL/CW.txt', encoding="utf8") as file:
            cw= file.read()
        with open('app/recommenderfiles/SPECIAL/DET.txt', encoding="utf8") as file:
            det= file.read()
        with open('app/recommenderfiles/SPECIAL/DI.txt', encoding="utf8") as file:
            di= file.read()
        with open('app/recommenderfiles/SPECIAL/EH.txt', encoding="utf8") as file:
            eh= file.read()
        with open('app/recommenderfiles/SPECIAL/ID.txt', encoding="utf8") as file:
            ide= file.read()
        with open('app/recommenderfiles/SPECIAL/MA.txt', encoding="utf8") as file:
            ma= file.read()
        with open('app/recommenderfiles/SPECIAL/MOD.txt', encoding="utf8") as file:
            mod= file.read()
        with open('app/recommenderfiles/SPECIAL/PGR.txt', encoding="utf8") as file:
            pgr= file.read()
        with open('app/recommenderfiles/SPECIAL/PT.txt', encoding="utf8") as file:
            pt= file.read()
        with open('app/recommenderfiles/SPECIAL/PY.txt', encoding="utf8") as file:
            py= file.read()
        with open('app/recommenderfiles/SPECIAL/REA.txt', encoding="utf8") as file:
            rea= file.read()
        with open('app/recommenderfiles/SPECIAL/SMP.txt', encoding="utf8") as file:
            smp= file.read()
        with open('app/recommenderfiles/SPECIAL/TC.txt', encoding="utf8") as file:
            tc= file.read()
        with open('app/recommenderfiles/SPECIAL/WP_EM.txt', encoding="utf8") as file:
            wp= file.read()
        SPECR={
            "Commercial Pilot":self.CosineSim(cp),"Content Writer":self.CosineSim(cw),"Detectives":self.CosineSim(det),"Dance Instructor":self.CosineSim(di),
            "Ethical hacker":self.CosineSim(eh),"Interior Designer":self.CosineSim(ide),"Makeup Artist":self.CosineSim(ma),"Modelling":self.CosineSim(mod),
            "Photographer":self.CosineSim(pgr),"Personal Trainer":self.CosineSim(pt),"Professional Youtuber":self.CosineSim(py),"Real Estate Agent":self.CosineSim(rea),
            "Stock Market Professional":self.CosineSim(smp),"Travel Consultant":self.CosineSim(tc),"Wedding Planner":self.CosineSim(wp),
            }
        SSPECR = sorted(SPECR.items(), key=lambda x:x[1],reverse=True)
        RSPEC=[]
        for i in range(4):
            RSPEC.append(SSPECR[i][0])
        return RSPEC
    def CosineSim(self,text):
        self.INP=self.INP.lower()

        self.INP= word_tokenize(self.INP)
        self.INP= [word for word in self.INP if not word in stopwords.words()]
        self.INP = (" ").join(self.INP)

        text=text.lower()
        text= word_tokenize(text)
        text= [word for word in text if not word in stopwords.words()]
        text = (" ").join(text)

        snow_stemmer = SnowballStemmer(language='english')
        self.INP=snow_stemmer.stem(self.INP)
        text=snow_stemmer.stem(text)

        X=self.INP 
        Y=text 

        text=[X,Y]
        cv=CountVectorizer()
        count_matrix=cv.fit_transform(text)
        sim_score=cosine_similarity(count_matrix)

        return sim_score[0][1]
class Sentiment:
    def __init__(self,m):
        self.m=m
    def SentimentAnalyzer(self):
        vader=SentimentIntensityAnalyzer()
        data=(self.m).lower()
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
