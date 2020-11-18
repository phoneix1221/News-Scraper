from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField,BooleanField
from wtforms.validators import DataRequired,Email,Length,EqualTo,ValidationError
from blog.routes import User
from wtforms.fields.html5 import DateField

class Registrationform(FlaskForm):
    username = StringField('Username ', validators=[DataRequired(),Length(min=2,max=20)])
    email=StringField('Email ', validators=[DataRequired(),Length(min=2,max=30),Email()])
    password=PasswordField('Password',validators=[DataRequired(),Length(min=2,max=30)])
    confirm_password=PasswordField('Confirm Password',validators=[DataRequired(),EqualTo('password')])
    submit=SubmitField('Sign up')

    # fuction to check if user already exist in database compare to username



class loginform(FlaskForm):
   
    email=StringField('Email ', validators=[DataRequired(),Length(min=2,max=30),Email()])
    password=PasswordField('Password',validators=[DataRequired(),Length(min=2,max=30)]) 
    remember=BooleanField('remember me')   
    submit=SubmitField('login')
     # fuction to check if user already exist in database compare to email

class websiteform(FlaskForm):
    websitename=StringField('NAME')
    websiteurl=StringField('URL')
    date=DateField('DATE',format="%Y-%m-%d")
    total_no_post=StringField('URL')
    submit=SubmitField('save')


class viewform(FlaskForm):
    websitename=StringField('NAME')
    keyword=StringField('URL')
    datefrom=DateField('DATE',format="%Y-%m-%d")
    dateby=DateField('DATE',format="%Y-%m-%d")
    total_no_post=StringField('URL')
    language=StringField('Language')
    submit=SubmitField('save')