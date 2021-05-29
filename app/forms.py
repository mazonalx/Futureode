from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField,TextAreaField,SelectField,RadioField
from wtforms import SelectMultipleField
from wtforms.validators import DataRequired

Streams =[('science','Science'),('commerce','Commerce'),('humanities','Humanities')]
class LoginForm(FlaskForm):
    name = StringField('Full Name',validators=[DataRequired()])
    uname = StringField('username',validators=[DataRequired()])
    submit = SubmitField('Submit')
class FeedbackForm(FlaskForm):#Step1
    stream = SelectField(u'Stream',[DataRequired()],choices=Streams)    
    submit = SubmitField('Submit',render_kw={'data-toggle':'value: '})

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
skillsc = [('C','C'),('Cpp','Cpp'),('Python','Python'),('Java','Java'),('JavaScript','JavaScript'),('Swift','Swift'),('Csharp','C#'),('HTML','HTML'),('CSS','CSS'),('ASP','ASP'),('Bootstrap','Bootstrap'),('jQuery','jQuery'),('MySQL','MySQL'),('Perl','Perl'),('PostgreSQL','PostgreSQL'),('Ruby','Ruby')
,('Creativity','Creativity'),('Interpersonal Skills','Interpersonal Skills'),('Critical Thinking','Critical Thinking'),('Problem Solving','Problem Solving'),('Public Speaking','Public Speaking'),('Verbal and nonverbal communication','Verbal and nonverbal communication')]
certificationsc = [('AWS Certified Solutions Architect','AWS Certified Solutions Architect'),('Certified Cloud Security Professional','Certified Cloud Security Professional'),('Certified Data Privacy Solutions Engineer','Certified Data Privacy Solutions Engineer'),('Certified Data Professional','Certified Data Professional'),('Certified Ethical Hacker','Certified Ethical Hacker'),('Certified Information Security manager','Certified Information Security manager'),
('Certified Information Systems Security Professional','Certified Information Systems Security Professional '),('Cisco Certified Internetwork Expert','Cisco Certified Internetwork Expert'),('Cisco Certified Network Associate','Cisco Certified Network Associate'),('Cisco Certified Professional Network Professional','Cisco Certified Professional Network Professional'),('Microsoft Certified Azure Solutions Architect','Microsoft Certified Azure Solutions Architect'),('Microsoft Certified Solutions Associate','Microsoft Certified Solutions Associate'),
('Oracle Certified MySQL Database Administrator','Oracle Certified MySQL Database Administrator'),('Project Management Professional','Project Management Professional ')]
aoec=[('Teaching','Teaching'),('Photo and video editing','Photo and video editing'),('Photography','Photography'),('Dance or music','Dance or music'),('Acting or drama','Acting or drama'),('Coding and programming','Coding and programming'),('Blogging and content','Blogging and content'),('Writing or reading','Writing or reading'),('Network Architecture','Network Architecture'),('Computer Graphics','Computer Graphics'),('Big Data','Big Data'),('Cloud Computing','Cloud Computing'),('Nanocomputing','Nanocomputing'),('Robotics','Robotics'),('Quantum Computing','Quantum Computing')]
class DataForm(FlaskForm):#Step2 
    sub1 = SelectField(u'',[DataRequired()],choices=grades)
    sub2 = SelectField(u'',[DataRequired()],choices=grades)
    sub3 = SelectField(u'',[DataRequired()],choices=grades)
    sub4 = SelectField(u'',[DataRequired()],choices=grades)
    sub5 = SelectField(u'',[DataRequired()],choices=grades)
    sub6 = SelectField(u'',[DataRequired()],choices=grades)
    
    iq1 = RadioField(u'',[DataRequired()],choices=iq1c)
    iq2 = RadioField(u'',[DataRequired()],choices=iq2c)
    iq3 = RadioField(u'',[DataRequired()],choices=iq3c)
    iq4 = RadioField(u'',[DataRequired()],choices=iq4c)
    iq5 = RadioField(u'',[DataRequired()],choices=iq5c)
    iq6 = RadioField(u'',[DataRequired()],choices=iq6c)
    iq7 = RadioField(u'',[DataRequired()],choices=iq7c)
    iq8 = RadioField(u'',[DataRequired()],choices=iq8c)
    iq9 = RadioField(u'',[DataRequired()],choices=iq9c)
    iq10 = StringField(u'Ans',[DataRequired()])

    pq1 = SelectMultipleField('',[DataRequired()], choices=pq1c, render_kw={'style': 'height: fit-content; list-style: none;'})
    pq2 = SelectMultipleField('',[DataRequired()], choices=pq2c, render_kw={'style': 'height: fit-content; list-style: none;'})
    pq3 = SelectMultipleField('',[DataRequired()], choices=pq3c, render_kw={'style': 'height: fit-content; list-style: none;'})
    pq4 = SelectMultipleField('',[DataRequired()], choices=pq4c, render_kw={'style': 'height: fit-content; list-style: none;'})
    pq5 = SelectMultipleField('',[DataRequired()], choices=pq5c, render_kw={'style': 'height: fit-content; list-style: none;'})
    submit = SubmitField('Submit')

class SkillCertBookForm(FlaskForm):
    skills = SelectMultipleField('Skills',choices=skillsc ,render_kw={'style': 'list-style: none;'})
    skill_oth = TextAreaField('Others')
    certifications = SelectMultipleField('Certifications',choices=certificationsc ,render_kw={'style': 'list-style: none;'})
    certifications_oth = TextAreaField('Others')
    aoe = SelectMultipleField('Area Of Interest',[DataRequired()], choices=aoec,render_kw={'style': 'list-style: none;'})
    aoe_oth = TextAreaField('Others')
    submit = SubmitField('Submit')


