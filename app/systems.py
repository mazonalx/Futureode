import numpy as np
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import CountVectorizer
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from flask import session
import re
class Recommender:
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
                #print('Course => ',data['Title'][i])
                #print('Recommending_Score => '+str(sim_score[0][1]*100))
                #print('Course rating => ',data['Stars'][i])
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
