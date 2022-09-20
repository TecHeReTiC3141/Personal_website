from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField,\
    EmailField, PasswordField, BooleanField, TextAreaField, SelectField
from wtforms.validators import Email, Length, DataRequired, EqualTo

class CommentForm(FlaskForm):
    label = 'Please, add your comment'
    name = StringField(label='UserName')
    mark = SelectField(label='Your mark for game', choices=range(1, 6))
    text = TextAreaField(label='Your comment', validators=[DataRequired()])
    submit = SubmitField('Send')
