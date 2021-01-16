from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,PasswordField,BooleanField,SubmitField,FloatField
from wtforms.validators import DataRequired,Length,ValidationError,Email,EqualTo,NumberRange
from app.models import registration


class RegistrationForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    username = StringField('Username', validators=[DataRequired()])
    contact=StringField('Contact',validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    password2 = PasswordField(
        'Repeat Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Register')

    def validate_username(self, username):
        user = registration.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError('Please use a different username.')

    def validate_email(self, email):
        user = registration.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError('Please use a different email address.')

class LoginForm(FlaskForm):
    email=StringField('email',validators=[DataRequired()])
    password=PasswordField('Password',validators=[DataRequired()])
    remember_me=BooleanField('Keep me logged in')
    submit=SubmitField('Sign In')
