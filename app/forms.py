from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField,TextAreaField,SelectField,RadioField
from wtforms import SelectMultipleField
from wtforms.validators import DataRequired, Length

Streams =[('science','Science'),('commerce','Commerce'),('humanities','Arts/Humanities')]
q1c=[('1','Yes, I have/had properly decided my choice of subject stream.'),('2','No, I will be selecting/selected the subject stream suggested by my parents/guardians/teachers.'),
('3','No, I may have/had to select a subject stream according to my marks.'),('4','No, I will be selecting/selected the subject stream opted by my friends.')]
class LoginForm(FlaskForm):
    name = StringField('Name',validators=[DataRequired()])
    uname = StringField('UserName',validators=[DataRequired()])
    submit = SubmitField('Submit')
class FeedbackForm(FlaskForm):#Step1
    stream = SelectField(u'Stream',[DataRequired()],choices=Streams)
    q1 = RadioField(u'',choices=q1c)
    submit = SubmitField('Submit')

grades =[('1','A+'),('2','A'),('3','B+'),('4','B'),('5','C'),('6','D'),('7','X')]
iq1c=[('A','44 triangles, 10 squares'),('B','43 triangles ,9  squares'),('C','44 traingles ,12 squares'),('D','40 traingles , 12 squares'),('E','None  of  the  above')]
iq2c=[('A','500'),('B','336'),('C','504'),('D','290'),('E','None of the above')]
iq3c=[('A','50'),('B','49'),('C','47'),('D','44'),('E','None of the above')]
iq4c=[('A','70'),('B','75'),('C','69'),('D','72'),('E','None of the above')]
iq5c=[('A','A'),('B','B'),('C','C'),('D','D'),('E','E')]
iq6c=[('A','84129'),('B','32418'),('C','47632'),('D','36119'),('E','67626'),('F','72927')]
iq7c=[('A','3/7'),('B','13/28'),('C','5/14')]
iq8c=[('A','A'),('B','B'),('C','C'),('D','D')]
iq9c=[('A','A'),('B','B'),('C','C'),('D','D'),('E','E'),('F','F'),('G','G')]

pq1c=[('1','I enjoy being the center of attention'),('2','I feel comfortable around people.'),('3','I take time out for others.'),('4','I usually feel others\' emotions.'),('5','I believe others have good intentions.')]
pq2c=[('1','I am concerned about how others feel.'),('2','I am considered kind and soft hearted.'),('3','I can easily start conversations.'),('4','I\'m skilled in handling social situations.'),('5','I sometimes speak without previous thinking.')]
pq3c=[('1','I pay attention to details.'),('2','I like keeping everything organized.'),('3','I never leave my belongings around.'),('4','I am always prepared.'),('5','I am more analytical than creative.')]
pq4c=[('1','I consider myself very creative.'),('2','I enjoy time spent in the nature.'),('3','I consider I have excellent ideas.'),('4','I believe in the importance of art.'),('5','I am quick to understand most things.')]
pq5c=[('1','I get irritated easily.'),('2','I am hardly able to relax.'),('3','I get upset frequently.'),('4','I am affected by disappointments in life.'),('5','I feel stressed out most time.')]    
skills =[('1','Creativity'),('2','Interpersonal Skills'),('3','Critical Thinking'),('4','Problem Solving'),('5','Public Speaking'),
('6','Customer Service Skills'),('7','Others')]
class DataForm(FlaskForm):#Step2 
    sub1 = SelectField(u'',[DataRequired()],choices=grades)
    sub2 = SelectField(u'',[DataRequired()],choices=grades)
    sub3 = SelectField(u'',[DataRequired()],choices=grades)
    sub4 = SelectField(u'',[DataRequired()],choices=grades)
    sub5 = SelectField(u'',[DataRequired()],choices=grades)
    sub6 = SelectField(u'',[DataRequired()],choices=grades)
    iq1 = RadioField(u'',choices=iq1c)
    iq2 = RadioField(u'',choices=iq2c)
    iq3 = RadioField(u'',choices=iq3c)
    iq4 = RadioField(u'',[DataRequired()],choices=iq4c)
    iq5 = RadioField(u'',[DataRequired()],choices=iq5c)
    iq6 = RadioField(u'',choices=iq6c)
    iq7 = RadioField(u'',choices=iq7c)
    iq8 = RadioField(u'',[DataRequired()],choices=iq8c)
    iq9 = RadioField(u'',[DataRequired()],choices=iq9c)
    iq10 = StringField(u'Ans',[DataRequired()])
    pq1 = SelectMultipleField('',[DataRequired()], choices=pq1c, render_kw={'style': 'height: fit-content; list-style: none;'})
    pq2 = SelectMultipleField('',[DataRequired()], choices=pq2c, render_kw={'style': 'height: fit-content; list-style: none;'})
    pq3 = SelectMultipleField('',[DataRequired()], choices=pq3c, render_kw={'style': 'height: fit-content; list-style: none;'})
    pq4 = SelectMultipleField('',[DataRequired()], choices=pq4c, render_kw={'style': 'height: fit-content; list-style: none;'})
    pq5 = SelectMultipleField('',[DataRequired()], choices=pq5c, render_kw={'style': 'height: fit-content; list-style: none;'})
    submit = SubmitField('Submit')
class SkillCertForm(FlaskForm):
    skill = TextAreaField('Skills',validators=[DataRequired(),Length(min=4,message=('Your message is too short.'))])
    certifications = TextAreaField('Certifications',validators=[DataRequired(),Length(min=4,message=('Your message is too short.'))])
    submit = SubmitField('Submit')


