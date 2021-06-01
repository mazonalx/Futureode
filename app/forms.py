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
iq9c=[('A','A'),('B','B'),('C','C'),('D','D'),('E','E')]

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

    submit = SubmitField('Submit')



