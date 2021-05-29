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
                count=count+1
                Course.append(data['Title'][i])
                Course.append(data['Stars'][i])
                Course.append(str(round(sim_score[0][1]*100,)))
        session["Cdata"]=Course
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
                count=count+1
                Course.append(data['Title'][i])
                Course.append(data['Stars'][i])
                Course.append(str(round(sim_score[0][1]*100,)))
        session["Cdata"]=Course
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
                count=count+1
                Course.append(data['Title'][i])
                Course.append(data['Stars'][i])
                Course.append(str(round(sim_score[0][1]*100,)))
        session["Cdata"]=Course
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
                count=count+1
                Course.append(data['Title'][i])
                Course.append(data['Stars'][i])
                Course.append(str(round(sim_score[0][1]*100,)))
        session["Cdata"]=Course
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
                count=count+1
                Course.append(data['Title'][i])
                Course.append(data['Stars'][i])
                Course.append(str(round(sim_score[0][1]*100,)))
        session["Cdata"]=Course        
class Recommender1:
    def __init__(self,INP):
        self.INP = INP
    def ReadSfiles(self):
        print("***SCIENCE***")
        with open('app/recommenderfiles/SCIENCE/AERO.txt', encoding="utf8") as file:
            aero = file.read()
        print("AERONAUTICAL =",self.CosineSim(aero))
        with open('app/recommenderfiles/SCIENCE/ARCHI.txt', encoding="utf8") as file:
            archi= file.read()
        print("ARCHITECTURAL =",self.CosineSim(archi))
        with open('app/recommenderfiles/SCIENCE/AUTOM.txt', encoding="utf8") as file:
            autom= file.read()
        print("AUTOMOBILE =",self.CosineSim(autom))
        with open('app/recommenderfiles/SCIENCE/BIOMED.txt', encoding="utf8") as file:
            biomed= file.read()
        print("BIOMEDICAL =",self.CosineSim(biomed))
        with open('app/recommenderfiles/SCIENCE/ME.txt', encoding="utf8") as file:
            me= file.read()
        print("MECHANICAL ENGINEERING =",self.CosineSim(me))
        with open('app/recommenderfiles/SCIENCE/CE.txt', encoding="utf8") as file:
            ce= file.read()
        print("CIVIL =",self.CosineSim(ce))
        with open('app/recommenderfiles/SCIENCE/CHE.txt', encoding="utf8") as file:
            che= file.read()
        print("CHEMICAL =",self.CosineSim(che))
        with open('app/recommenderfiles/SCIENCE/CSE.txt', encoding="utf8") as file:
            cse= file.read()
        print("COMPUTER SCIENCE =",self.CosineSim(cse))
        with open('app/recommenderfiles/SCIENCE/ECE.txt', encoding="utf8") as file:
            ece= file.read()
        print("ELECTRONICS AND COMMUNICATION =",self.CosineSim(ece))
        with open('app/recommenderfiles/SCIENCE/EEE.txt', encoding="utf8") as file:
            eee= file.read()
        print("ELECTRICAL AND ELECTRONICS =",self.CosineSim(eee))
        with open('app/recommenderfiles/SCIENCE/ENV.txt', encoding="utf8") as file:
            env= file.read()
        print("ENVIRONMENTAL =",self.CosineSim(env))
        with open('app/recommenderfiles/SCIENCE/B.SC.txt', encoding="utf8") as file:
            bsc= file.read()
        print("B.SC =",self.CosineSim(bsc))
        with open('app/recommenderfiles/SCIENCE/MBBS.txt', encoding="utf8") as file:
            mbbs= file.read()
        print("MBBS =",self.CosineSim(mbbs))
        with open('app/recommenderfiles/SCIENCE/NURSING.txt', encoding="utf8") as file:
            nurs= file.read()
        print("NURSING =",self.CosineSim(nurs))
        with open('app/recommenderfiles/SCIENCE/BDS.txt', encoding="utf8") as file:
            bds= file.read()
        print("NURSING =",self.CosineSim(bds))
        with open('app/recommenderfiles/SCIENCE/BAMS.txt', encoding="utf8") as file:
            bams= file.read()
        print("NURSING =",self.CosineSim(bams))
    def ReadCfiles(self):
        print("***COMMERCE***")
        with open('app/recommenderfiles/COMMERCE/STCS.txt', encoding="utf8") as file:
            stcs= file.read()
        print("BCom in STATISTICS=",self.CosineSim(stcs))
        with open('app/recommenderfiles/COMMERCE/TOTRM.txt', encoding="utf8") as file:
            totrm= file.read()
        print("BCom in TOURISM & TRAVEL MANAGEMENT =",self.CosineSim(totrm))
        with open('app/recommenderfiles/COMMERCE/BUAD.txt', encoding="utf8") as file:
            buad= file.read()
        print("BCom in BUSINESS & ADMINISTRATION =",self.CosineSim(buad))
        with open('app/recommenderfiles/COMMERCE/MAIF.txt', encoding="utf8") as file:
            maif= file.read()
        print("BCom in MANAGEMENT ACCOUNTING & INTERNATIONAL FINANCE =",self.CosineSim(maif))
        with open('app/recommenderfiles/COMMERCE/MARK.txt', encoding="utf8") as file:
            mark= file.read()
        print("BCom in MARKETING=",self.CosineSim(mark))
        with open('app/recommenderfiles/COMMERCE/BAFI.txt', encoding="utf8") as file:
            bafi= file.read()
        print("BCom in BANKING & FINANCE =",self.CosineSim(bafi))
        with open('app/recommenderfiles/COMMERCE/ACC.txt', encoding="utf8") as file:
            acc= file.read()
        print("BCom in ACCOUNTING =",self.CosineSim(acc))
        with open('app/recommenderfiles/COMMERCE/ACTA.txt', encoding="utf8") as file:
            acta= file.read()
        print("BCom in ACCOUNTING & TAXATION=",self.CosineSim(acta))
        with open('app/recommenderfiles/COMMERCE/APPE.txt', encoding="utf8") as file:
            appe= file.read()
        print("BCom in APPLIED ECONOMICS =",self.CosineSim(appe))
    def ReadHfiles(self):
        print("***HUMANITIES***")
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
